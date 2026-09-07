# HCCJP 第77回 進行台本 ─ 実演カタログ（2026-09-11）

進行スライド: https://presentations.ebisuda.net/decks/hccjp-77-arc-operations （25枚・owner-only）
配信: YouTube Live https://www.youtube.com/watch?v=wk7hgvEM8Yw
Connpass: https://hybridcloud.connpass.com/event/406031/

**各スライドの「ここで何を見せるか」は、デッキのノート（発表者ビュー）にも同じ内容が入っている。**
このファイルは、そのノートを実行するための URL・コマンド・所要時間・保険をまとめた元帳。

対象環境（Azure MVP サブスクリプション / RG `rg-hccjp76-arc` / japaneast）

> このリポジトリは public なので、サブスクリプションIDは書かない。ターミナルで
> `export SUB=<サブスクリプションID>` を通してから、以下のコマンドをそのまま使う。

| 名前 | 中身 | 置き場所 |
|---|---|---|
| `arcwin01` | Windows Server 2025 | nestedhyperv > nested-lab-01 (10.20.0.20) 上のネスト VM |
| `arclnx01` | Ubuntu 24.04 | 同上 |

---

## 0. スライドとノートの出し方（2画面でやる）

**スライドを全画面にすると、デモ指示を書いたノートは自分からも見えなくなる。** 2窓に分けて出す。

1. デッキを開く → ヘッダーの **［ノート別窓］** を押す（ノートパネル付きの窓が開く）
2. ノート窓は手元の画面に置く。**投影・配信するのは元の窓**
3. 元の窓で **［全画面］**（スライドだけが全画面になる）を押し、その画面／ウィンドウを共有する
4. 送りはどちらの窓でしてもよい。**両方が同じスライドに追従する**（BroadcastChannel 同期）

投影側にノートは一切出ないので、そのまま配信して問題ない。1画面しかない場合は、
ノート窓の代わりにこのファイル（`run-of-show.md`）をスマホかタブレットで開いておく。

---

## 1. 画面の並べ方（開始20分前まで）

ブラウザのタブは左から固定する。デモのたびに探すと視聴者を待たせる。

| # | タブ | 何のため |
|---|---|---|
| 1 | Azure ポータル ─ Azure Arc / マシン一覧 | 2台が Connected であることの入口 |
| 2 | ポータル ─ `arcwin01` の概要 | 左メニューの棚卸し・Connected の緑 |
| 3 | ポータル ─ Azure Update Manager / マシン | Azure VM とオンプレが同じ一覧に並ぶ画 |
| 4 | ポータル ─ `arcwin01` / マシン構成 | 準拠・非準拠の実物 |
| 5 | ポータル ─ Resource Graph エクスプローラー | 復元後チェックの1本クエリ |
| 6 | ポータル ─ コスト管理 / コスト分析 | 課金の線引き |
| 7 | Microsoft Learn（Hotpatch の価格 / Hyper-V チェックポイント） | 一次情報 |
| 8 | `nested-lab-01` の Hyper-V マネージャー（RDP） | チェックポイント `T1-hccjp77` |

さらに、デッキの投影窓とノート窓（上の「0.」）を別々の画面に置く。

ターミナルは1枚だけ、文字サイズ18pt以上。`export SUB=<サブスクリプションID>` と `az account set -s $SUB` を先に通しておく。

---

## 2. 開始前の仕込み（13:50 ─ ここをサボると本番で待ち時間が発生する）

| # | やること | 理由 |
|---|---|---|
| 1 | Update Manager で `arcwin01` / `arclnx01` の**評価を実行**しておく | 評価は2〜4分かかる。デモ②で結果だけ見せるため |
| 2 | Run Command を**1回空打ち**しておく | **初回は10分近くかかる**（2026-09-07 実測: PUT から `Succeeded` まで約9分。RunCommand の初回セットアップが走るため）。温めておかないと本番で必ず待たされる |
| 3 | `az ssh arc` を使うなら**接続を1回試す** | 2026-09-07 時点で HybridConnectivity のエンドポイントが空。**今のままでは Arc SSH は通らない**ので、使うなら事前に作り直す（下の「5. 未確認・要リハーサル」参照） |
| 4 | 2台が Connected か確認 | `az connectedmachine list -g rg-hccjp76-arc --query "[].{name:name,status:status}" -o table` |

---

## 3. 実演カタログ

「LIVE」バッジがスライドの右下に出る回が、実機に切り替える回。

### デモ① ─ Arc 経由でコマンドが通る（スライド: PROOF／2〜3分）

見せるもの: インバウンドを1つも開けていないオンプレのサーバーに、Azure から命令が届くこと。

```bash
cat > /tmp/rc.json <<'EOF'
{"location":"japaneast","properties":{"source":{"script":"echo HOST=$(hostname); echo OS=$(. /etc/os-release; echo $PRETTY_NAME); echo UPTIME=$(uptime -p)"},"asyncExecution":false,"timeoutInSeconds":90}}
EOF
az rest --method put \
  --url "https://management.azure.com/subscriptions/$SUB/resourceGroups/rg-hccjp76-arc/providers/Microsoft.HybridCompute/machines/arclnx01/runCommands/hccjp77-live?api-version=2024-07-10" \
  --body @/tmp/rc.json
```

結果の取り出し（`instanceView.output` に出る）:

```bash
az rest --method get \
  --url "https://management.azure.com/subscriptions/$SUB/resourceGroups/rg-hccjp76-arc/providers/Microsoft.HybridCompute/machines/arclnx01/runCommands/hccjp77-live?api-version=2024-07-10" \
  --query "properties.instanceView.output" -o tsv
```

- 期待する出力: `HOST=arclnx01` / `OS=Ubuntu 24.04.4 LTS` / `UPTIME=...`
- 待っている間に話すこと: 「インバウンドのポートは1つも開けていません。エージェントが外向き443だけで取りに来ています」
- **保険**: 40秒たっても返らなければ深追いしない。既存の実行結果（`runCommands/hccjp77-check` / `hccjp77-markerpath`）を GET して見せるか、スライドの「42秒」に戻す。
- 2026-09-07 実測: 温まっていない状態からだと約9分。**開始前の空打ちが前提**。

### デモ② ─ Update Manager（スライド: AZURE UPDATE MANAGER／ASSESS RESULT／2分）

1. ポータル ＞ Azure Update Manager ＞ [マシン]。**Azure VM とオンプレが同じ一覧**に並ぶところが主役。
2. 開始前に仕込んだ評価結果を開き、Windows と Linux を並べる。
3. Linux の「Ubuntu Pro のサブスクリプションが必要」というエラー行を指差す。ここがいちばん実務的。

CLI で見せる場合（2026-09-07 に動作確認済み）:

```bash
az graph query -q "patchassessmentresources | where type =~ 'microsoft.hybridcompute/machines/patchassessmentresults' | project machine=split(id,'/')[8], status=properties.status, counts=properties.availablePatchCountByClassification" \
  --subscriptions "$SUB" -o json
```

前回（9/5）の実測値: `arcwin01` = security 2 / updates 2 / definition 2 / updateRollup 1、`arclnx01` = other 40。

### デモ③ ─ 課金の線引き（スライド: BILLING／30秒）

ポータル ＞ コスト管理 ＞ コスト分析。粒度＝**日別**、スコープをこのサブスクリプション、フィルターを RG `rg-hccjp76-arc`。
「繋ぐだけなら0円、Update Manager を有効にした日から線が立つ」を画面でなぞる。実測は **$0.162/台/日（2台で約48円/日）**。

### デモ④ ─ 実験の舞台（スライド: EXPERIMENT／1分）

`nested-lab-01`（10.20.0.20）へ RDP し、Hyper-V マネージャーで `arcwin01` / `arclnx01` と
チェックポイント **`T1-hccjp77`**（両VMに残置）を見せる。「この実験は本物の機械でやりました」を1回だけ見せる。

- 余裕があるときだけの上級編: その場で `arcwin01` を `T1-hccjp77` に巻き戻し、RESULT 1 の「Windows は約9分」をタイマーで回しながら進める。**進行が押していたらやらない。**
- ホスト側の確認コマンド（moviegen から）:
  ```bash
  ssh nestedhyperv 'powershell -NoProfile -Command "Get-VM | Format-Table Name,State -Auto"'
  ```

### デモ④.5 ─ 実機の marker を見る（スライド: RESULT 1／40秒）

巻き戻したあとに拡張機能が追いついた証拠。**Linux の実体は `/opt/hccjp77/marker.txt`、中身は `T2-updated-by-azure`（2026-09-07 に Run Command で確認）**。

```bash
cat > /tmp/rc-marker.json <<'EOF2'
{"location":"japaneast","properties":{"source":{"script":"cat /opt/hccjp77/marker.txt"},"asyncExecution":false,"timeoutInSeconds":60}}
EOF2
az rest --method put \
  --url "https://management.azure.com/subscriptions/$SUB/resourceGroups/rg-hccjp76-arc/providers/Microsoft.HybridCompute/machines/arclnx01/runCommands/hccjp77-marker-live?api-version=2024-07-10" \
  --body @/tmp/rc-marker.json
```

拡張機能のログ（`has new settings - enqueuing extension` / `already installed - Not enqueuing`）は
**事前に撮ったスクリーンショット**で見せる。ライブでログを掘りに行かない。

### デモ⑤ ─ 巻き戻しても Azure は緑のまま（スライド: RESULT 2／40秒）

ポータルの `arcwin01` 概要（**Connected**）→ [拡張機能]（`hccjp77-marker` = **Succeeded**）を続けて見せる。
「巻き戻している最中も、この画面はずっとこの色でした」。今日いちばんの持ち帰り。

### デモ⑥ ─ 構成ポリシーは直るものと直らないものがある（スライド: RESULT 3／1分）

ポータル ＞ `arcwin01` ＞ [マシン構成]。**2026-09-07 時点の実測**（当日もこの並びのはず）:

| 割り当て | 状態 |
|---|---|
| `SetWindowsTimeZone` | 非準拠（ApplyAndAutoCorrect なのに直らない） |
| `SetSecureProtocol` | 準拠 |
| `AuditSecureProtocol` | 準拠 |
| `AzureWindowsBaseline` / `WindowsDefenderExploitGuard` | 非準拠（監査系） |

CLI で見せる場合:

```bash
az rest --method get \
  --url "https://management.azure.com/subscriptions/$SUB/resourceGroups/rg-hccjp76-arc/providers/Microsoft.HybridCompute/machines/arcwin01/providers/Microsoft.GuestConfiguration/guestConfigurationAssignments?api-version=2022-01-25" \
  --query "value[].{name:name,status:properties.complianceStatus,checked:properties.lastComplianceStatusChecked}" -o table
```

### デモ⑦ ─ 戻し方チェックリストを1本のクエリにする（スライド: TAKE THIS HOME／1分）

Resource Graph エクスプローラーに貼る（2026-09-07 に動作確認済み）:

```kusto
resources
| where type =~ 'microsoft.hybridcompute/machines'
| project name, status=properties.status, agent=properties.agentVersion, lastSeen=properties.lastStatusChange
```

「復元したあと、これを流せば全台まとめて見られます」で締める。

---

## 4. 画面を見せるだけの場所（デモではないが、スライドから離れる）

| スライド | 見せるもの | 一言 |
|---|---|---|
| RECAP ─ 第76回 | https://www.youtube.com/@hccjp のサムネイル | 再生はしない。15秒 |
| INVENTORY | `arcwin01` の左メニューを上から下へ | 「この4分類は、実はこのメニューそのものです」 |
| HOTPATCH | Microsoft Learn の Hotpatch 価格ページ | 「2026年5月19日以降、Arc 接続マシンでは追加費用なし」を指す |
| CHECKPOINT | Learn の Hyper-V チェックポイントのページ | 「ダメなのはバックアップの代用にすること」 |
| BYPRODUCTS | 事前スクリーンショット（22日間 Disconnected のログ） | ライブで切断はしない |
| 告知 | connpass（10/3 ITと音楽の文化祭） | QRを出すなら5秒静止 |
| CLOSING | https://www.hccjp.org/ | 次回10月9日とアーカイブ |

---

## 5. 未確認・要リハーサル（9/11 までに潰す）

| # | 事項 | 状態 |
|---|---|---|
| 1 | **Arc SSH（`az ssh arc`）** | 2026-09-07 時点で HybridConnectivity のエンドポイントが**空**。8月に RG を消した影響とみられる。使うなら事前に作り直して疎通確認する。作り直せない場合は PROOF スライドの SSH 行は口頭で「前回の実測」と言う |
| 2 | **Run Command の初回コスト** | 2026-09-07 の実測で PUT から `Succeeded` まで**約9分**（初回セットアップ込み）。2回目が数十秒で返るかはリハーサルで確認する。いずれにせよ**開始前の空打ちを必須**にする |
| 3 | **Windows 側**の marker ファイルのパス | Linux は `/opt/hccjp77/marker.txt` と判明（2026-09-07）。Windows 側は未確認。Windows でも見せるならリハーサルで確認する |
| 4 | Update Manager の評価 | 当日に再実行する（9/5 の結果が残っているだけ） |
| 5 | チェックポイント `T1-hccjp77` の差分ディスク | 残置中。イベント前に容量を確認する |
| 6 | ポータルの深いリンク | ブレード名だけ記載してある。リハーサルでタブに開いてブックマークする |

---

## 6. 当日タイムライン

| 時刻 | やること |
|---|---|
| 13:30 | ラボ起動確認（`Get-VM`）・Arc 2台 Connected 確認 |
| 13:50 | Update Manager の評価を実行／Run Command を空打ち／タブ8枚を並べる／投影窓とノート窓を2画面に配置 |
| 14:00 | 配信開始・オープニング |
| 14:05 | 本編（前半＝棚卸しと Update Manager、後半＝万が一と戻し方） |
| 14:50 | Q&A |
| 15:00 | 高添さん「Adaptive Cloud 最新動向」 |
| 15:25 | 10/3 の告知 → クロージング（hccjp.org を見せて終わる） |

**デモが転んだときの原則**: 30秒粘って戻らなければスライドの実測値に戻る。今日の主題は「動くこと」ではなく
「壊れたあとに戻せること」なので、転んだこと自体を題材にしてよい。
