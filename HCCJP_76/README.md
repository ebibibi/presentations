# HCCJP 第76回勉強会

## 開催情報

- **日時**: 2026年8月14日（金）14:00-15:30
- **形式**: オンライン（YouTube Live）
- **テーマ**: オンプレのサーバー壊します。直すのはAIです。 — Azure Arc × AIによる無人障害復旧
- **Connpass**: https://hybridcloud.connpass.com/event/402528/

## 当日使うもの

| ファイル | 用途 |
|---|---|
| [`slides.md`](slides.md) | 本番スライド（Marp／HTMLコメントがそのまま発表者ノート） |
| `slides.pdf` / `slides.pptx` | 上記の書き出し（当日はPDFで投影する） |
| [`run-of-show.md`](run-of-show.md) | 進行台本・事前チェックリスト・分単位のタイムテーブル・リスクと逃げ道 |
| [`images/`](images/) | 構成図3枚（論理／物理／AIの操作経路）。生成元は [`diagrams/build_diagrams.py`](diagrams/build_diagrams.py) |

スライドの書き出し（Chromeのパスを明示しないと `No suitable browser found` になる）:

```bash
export CHROME_PATH=$(ls -d ~/.cache/puppeteer/chrome/*/chrome-linux64/chrome | head -1)
npx @marp-team/marp-cli --pdf  --allow-local-files slides.md -o slides.pdf
npx @marp-team/marp-cli --pptx --allow-local-files slides.md -o slides.pptx
```

## 概要

毎月第2金曜日14時からはHCCJPの勉強会！8月は**Azure Arc × AIエージェント**、しかも**一発勝負のライブデモ**でお届けします。

やることはシンプルです。

**手元のオンプレサーバーを、皆さんの目の前で壊します。そして、AIエージェントに直してもらいます。**

壊し方は当日**チャットで決めていただきます**（Webサービスを止める／設定ファイルを壊す／ファイアウォールで塞ぐ など）。AIには**何が起きたかを一切教えません**。渡すのは「監視が赤くなった。原因を調べて直して」という一言だけ。そこから先は、AIが自分で対象を特定し、Azure Arc 越しにコマンドを流し、ログを読み、原因を突き止め、復旧させます。

ポイントは、**誰もそのサーバーにログインしていない**ことです。Azure Arc でオンプレのサーバーを Azure に繋ぐと、**インバウンドのポート開放なし・VPNなし・踏み台なし**（通信はアウトバウンド443のみ）で、コマンド実行も構成変更もパッチ適用もSSHすら、Azureの Control Plane 経由で通ります。そして Azure 側の入口が `az` に統一されているということは——**AIエージェントがそのまま運用の手を持てる**ということです。

赤くなった画面が、緑に戻るかどうか。**うまくいかない場合も含めて**、そのままお見せします。

デモのあとは種明かしです。AIが実際に叩いたコマンドを全部並べて振り返り、そのうえで**一番大事な話**をします——**AIにここまでの権限を渡していいのか**。RBACの切り方、監査ログ、承認ゲート。「できる」と「やらせていい」の間にある線を、一緒に考えましょう。

「オンプレは残る。でも運用する場所は変えられる」——その実物を見に来てください！

## セッション内容

### 1. オンプレのサーバー、壊します。直すのはAIです。

**胡田 昌彦**（日本ビジネスシステムズ株式会社 / Microsoft MVP）

- **今日やること宣言** — このあとオンプレのサーバーを壊します
- **なぜ Azure Arc なのか** — オンプレは無くならない。無くせるのは「そこまで行く手間」のほう
- **繋ぐ仕組み** — Connected Machine agent / アウトバウンド443のみ / Arc Gateway
- **AIの手をどう作るか** — 入口が `az` に統一されている＝AIエージェントがそのまま運用の手を持てる
- ⭐ **ライブデモ：障害注入 → AIによる無人復旧**
  - 障害の種類は**チャットで決定**（複数シナリオを用意しています）
  - AIに伝えるのは「監視が赤い。調べて直して」だけ
  - 監視画面が **赤 → 緑** に戻るまで、そのままお見せします
- **種明かし** — AIが実際に何を叩いたのか、全コマンドを振り返る
- **権限と怖さの話** — RBACの切り方、監査ログ、承認ゲート。「できる」と「やらせていい」の線引き
- **まとめ** — 運用する場所が変わると、インフラエンジニアの仕事はどう変わるのか

### 2. Microsoft "Adaptive Cloud" 最新動向

高添 修 氏（日本マイクロソフト株式会社）

Microsoft高添さんからは毎月恒例のMicrosoft "Adaptive Cloud" の最新動向をお伝えいただきます！
Azure Local、Azure Arc、Windows Server関連の最新情報をお見逃しなく！

## スピーカー

- **胡田 昌彦** - 日本ビジネスシステムズ株式会社、Microsoft MVP for Cloud and Datacenter Management, Microsoft Azure
- **高添 修 氏** - 日本マイクロソフト株式会社

## タイムテーブル

| 時刻 | 時間 | セッション | スピーカー |
|------|------|------------|------------|
| 14:00 | 5分 | オープニング | 胡田 昌彦 |
| 14:05 | 45分 | オンプレのサーバー、壊します。直すのはAIです。（ライブデモ） | 胡田 昌彦 |
| 14:50 | 10分 | Q&A | 胡田 昌彦 |
| 15:00 | 20分 | Microsoft "Adaptive Cloud" Updates | 高添 修 氏 |
| 15:20 | 5分 | Q&A | 高添 修 氏 |
| 15:25 | 5分 | クロージング | 胡田 昌彦 |

### 45分の内訳（胡田セッション）

| 配分 | 内容 |
|---|---|
| 5分 | 今日やること宣言／デモ環境の紹介（第74回で建てたラボ） |
| 10分 | なぜArcか・繋ぐ仕組み・AIの手の作り方 |
| **15分** | ⭐ **ライブデモ：障害注入 → AIによる無人復旧** |
| 7分 | 種明かし（AIが叩いた全コマンドの振り返り） |
| 6分 | 権限と怖さの話（RBAC・監査ログ・承認ゲート） |
| 2分 | まとめ |

## デモ環境

第74回でご紹介した **Nested Hyper-Vラボ**（コードで建てた検証環境）の Windows Server / Linux を Azure Arc に接続して使用します。当日の状況により内容を調整する場合があります。

### 障害シナリオ候補（当日チャットで選択）

> ⚠️ **リハーサルはしない。** 事前にやるのは環境構築（Arc接続＋Webサイトが動く状態を作る）まで。
> 当日は動いている画面を見せてから、投票結果を見てその場で壊す。AIに解かせるのも本番が初回。
> リハーサルで一度解かせたシナリオを本番でもう一度解かせるなら、AIは答えを知っている状態になるため。
> 対象OS（Windows / Linux）も当日決める。下表のOS欄は想定であって確定ではない。

| # | 障害 | OS | 見た目の変化 | 難易度 |
|---|------|----|------|--------|
| 1 | Webサービス停止（nginx / W3SVC） | Linux / Windows | サイトが即エラー | 易 |
| 2 | 設定ファイルを壊してサービス起動失敗 | Linux | 再起動しても上がらない | 中 |
| 3 | ファイアウォールで80/443を塞ぐ | Windows | **サービスは正常なのに繋がらない** | 難（AIの推論が見える） |
| 4 | ログ肥大でディスク満杯 → サービス停止 | Linux | 書き込みエラーで停止 | 中 |
| 5 | サービスアカウントのパスワード変更でサービス起動不可 | Windows | イベントログに認証失敗 | 難 |

> 💡 難易度「難」を1つは混ぜたい。**症状と原因が一致しない障害**ほど、AIが"考えている"ことが伝わる。

## デモ環境の状態（2026-08-05 時点）

Nested Hyper-V ラボの L2 を Azure Arc に接続済み。どちらも**動いている Web サイト**を持っている
（当日はこれを壊す）。ページの実体と配布スクリプトは [`webroot/`](webroot/) にある。

| VM | OS / Web | IP | Azure Arc |
|---|---|---|---|
| arcwin01 | Windows Server 2025 / IIS | 10.10.0.51 | Connected（rg-hccjp76-arc / japaneast） |
| arclnx01 | Ubuntu 24.04 / nginx | 10.10.0.41 | Connected（同上） |

環境の再構築は `hyperv-nestlab` で `.\bootstrap.ps1 -L1 l1\standard-host.yml -L2 l2\arc-demo.yml`。
ページの再配布は `webroot/deploy.sh`（Arc の Run Command 経由）。

### 監視・復旧の流れ

専用ダッシュボードは作らず、**Azure Monitor / Application Insights の標準「可用性」画面**を使う。
オンプレ側にはパブリックIPやインバウンド開放を持たせず、Cloudflare Tunnel がアウトバウンドHTTPSで
Webサイトを公開する。Standard availability test が HTTP 200 とページ固有文字列を5分間隔で検証し、
失敗をAzure Monitorアラートとして赤表示する。AIはAzure Monitorの証拠を読み、Azure Arc Run Commandで
調査・復旧し、同じ可用性テストが緑へ戻るところまでを一続きで見せる。

ArcのConnected Machine heartbeatだけでは、切断判定に通常15〜30分かかるためWeb障害検知には使わない。
Standard availability testの検出目安は**停止から0〜5分＋アラート処理時間**。デモ用は日本1拠点・1失敗で
発報させるが、本番運用ではMicrosoft推奨の5拠点中3拠点失敗などへ強める。

検証用スクリプトとAzure構成は [`monitoring/`](monitoring/) に置く。Standard testは実行回数課金なので、
有効化前に課金承認を取る。

**2026-08-05実機検証済み**: Linux / Windowsとも正常時100% → サービス停止後0% → Azure Monitor
Active Alert（Sev1 / Fired）→ Arc Run Commandで復旧 → 100% → Alert Resolvedまで通った。停止から
アラート発火はLinux 6分12秒、Windows 5分27秒。検証後は一時監視リソースと公開Tunnelをすべて削除し、
両ArcマシンConnected・nginx/W3SVC稼働・ローカルHTTP 200へ戻した。詳細は [`monitoring/`](monitoring/)。

## 参考リンク

- [Azure Arc-enabled servers ドキュメント](https://learn.microsoft.com/azure/azure-arc/servers/)
- [Run Command（Arc対応サーバー）](https://learn.microsoft.com/azure/azure-arc/servers/run-command)
- [SSH access to Azure Arc-enabled servers](https://learn.microsoft.com/azure/azure-arc/servers/ssh-arc-overview)
- [Machine Configuration](https://learn.microsoft.com/azure/governance/machine-configuration/overview)
- [Application Insights 可用性テスト](https://learn.microsoft.com/azure/azure-monitor/app/availability)
- [第74回：コードで建てる検証環境](https://hybridcloud.connpass.com/event/396455/)

## 視聴方法

- **YouTube Live**: https://www.youtube.com/watch?v=uPc6T-wL8-0
- チャンネル登録してお待ちください！

## 主催

ハイブリッドクラウド研究会（HCCJP）

**主幹事**: 日本ビジネスシステムズ株式会社

**幹事**（50音順）:
- NTTコミュニケーションズ株式会社
- 日商エレクトロニクス株式会社
- 日本ヒューレット・パッカード株式会社
- 日本マイクロソフト株式会社
- VistaNet株式会社
- 株式会社ネットワールド
- 三井情報株式会社
- レノボ・エンタープライズ・ソリューションズ株式会社
