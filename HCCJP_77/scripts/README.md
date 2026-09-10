# HCCJP 第77回 ─ デモスクリプト

2026-09-11 のセッション「サーバーが巻き戻ったとき、Azureはどうなる？」で実際に叩いたスクリプトです。
Azure Arc 接続マシン（Windows Server 2025）を Hyper-V のチェックポイントで巻き戻し、
マシン構成（Machine Configuration）が何分で何を直すかを測るために使いました。

スライド: https://presentations.ebisuda.net/decks/hccjp-77-arc-operations

## 前提

- 3階層のラボ。L0（物理 Hyper-V）→ L1 `nested-lab-01`（入れ子の Hyper-V ホスト）→ L2 `arcwin01`（Arc 接続マシン）
- 実機へは PowerShell Direct（`Invoke-Command -VMName`）で入る。SSH も WinRM も要らない
- **パスワードは含めていません。** 実行前に管理者パスワードを環境変数へ入れる

```powershell
$env:LABPWD = "<ラボの Administrator パスワード>"
```

## demo/ ─ 当日の進行（L1 `nested-lab-01` 上で実行）

Hyper-V マネージャーと同じ画面で完結するよう、L1 に置いて番号順に叩きます。

| スクリプト | 何をするか |
|---|---|
| `D0-precheck.ps1` | 開始前チェック。VM 状態・チェックポイント・Arc の接続 |
| `D1-before.ps1` | 巻き戻す前の姿。OS の実値と、実機が持っている割り当て（モード・評価間隔） |
| `D2-mark.ps1` | 巻き戻せたかを検証し、計測開始（T0）を記録する |
| `D3-status.ps1` | 起動直後。Azure は緑、OS はもう壊れている |
| `D4-assignments.ps1` | 割り当ては巻き戻しても消えないことの確認 |
| `D5-timeline.ps1` | `gc_agent.log` ─ 何をいつ評価したか |
| `D6-queue.ps1` | 評価は1台につき1本ずつ。誰が実行中で誰が順番待ちか |
| `D7-recover.ps1` | エージェント再起動。キューは空くが順番は制御できない（対症療法） |
| `D8-verify.ps1` | OS の値が書き戻されたか |
| `restart.ps1` | 次の評価サイクルへ強制的に入るためだけの1本 |
| `W-worker.ps1` | `gc_worker.log` ─ Test だけか Set まで走ったか、1件あたり何秒か |
| `P1-rebuild.ps1` | リハーサル前に、壊した状態のチェックポイント `T7-demo-start` を作り直す |

## host/ ─ 保険（L0 の物理ホスト上で実行）

GUI が固まったときや、配信後の後始末に使う一式です。

| スクリプト | 何をするか |
|---|---|
| `1-status.ps1` | チェックポイント一覧＋実機が持っている割り当て |
| `2-rollback.ps1` | 巻き戻し（起動まで自動） |
| `3-evict-ghost.ps1` | 実機に居残った割り当てを外して評価キューを空ける |
| `4-osstate.ps1` | OS 側の実値（タイムゾーン・TLS 1.2・Defender・エージェント状態） |
| `5-break.ps1` | 意図的に壊す（タイムゾーンを UTC に、TLS 1.2 の値を削除） |
| `6-checkpoint.ps1` | 壊れた状態でチェックポイントを作る |
| `7-tail.ps1` | `gc_agent.log` の直近を絞って読む |
| `8-ghosthunt.ps1` | 居残り割り当ての実体を探す |
| `8-recover.ps1` | マシン構成エージェントの再起動 |
| `9-restore.ps1` | 配信後に正常状態のチェックポイントへ戻す |

## 実機のどこに何があるか

| パス / サービス | 中身 |
|---|---|
| `himds` | Azure Hybrid Instance Metadata Service ─ Arc 本体。ハートビートとトークン |
| `gcarcservice` | Guest Configuration Arc Service ─ マシン構成を評価しているのはこれ |
| `ExtensionService` | Guest Configuration Extension Service ─ 拡張機能の配布と実行 |
| `C:\ProgramData\GuestConfig\Configuration\<割り当て名>\` | 割り当ての実体。`<名>.metaconfig.json` にモードと評価間隔が入っている |
| `C:\ProgramData\GuestConfig\arc_policy_logs\gc_agent.log` | タイマー発火・評価の開始と完了（順番待ちが見える） |
| `C:\ProgramData\GuestConfig\arc_policy_logs\gc_worker.log` | Test / Set の別と、1件あたりの所要秒 |
| `C:\ProgramData\AzureConnectedMachineAgent\Log\` | `himds.log` / `azcmagent.log` ─ 接続とハートビート |
