# HCCJP 第76回 進行台本（2026-08-14）

本番の進行は **FlowAsk** で行う: https://flowask.ebisuda.net/e/964080 （eventId `964080`）
配信: YouTube Live https://www.youtube.com/watch?v=uPc6T-wL8-0
スライド原本: [`slides.md`](slides.md)（PDF/PPTXは配信が落ちたときの保険）

---

## 1. 事前準備（当日 12:00 までに終わらせる）

> ✅ 2026-08-13 12:0x に **監視は構築済み・可用性100%（緑）**、Quick Tunnel も稼働中。
> ただし Quick Tunnel のURLは cloudflared 再起動で変わり、**その時は可用性テストのURLも貼り替えが要る**
> （下の「1.6 監視」参照）。当日朝はまず両URLが生きているかを確認する。

| # | やること | 確認方法 | 状態 |
|---|---|---|---|
| 1 | Arc 2台が Connected | `az connectedmachine list -g rg-hccjp76-arc -o table` | ☐ |
| 2 | Web サイトが両方 200 | `webroot/deploy.sh` を流し直して確認 | ☐ |
| 3 | 公開URLを用意（Quick Tunnel。下の「公開経路」参照） | ブラウザで両URLが表示される | ☐ |
| 4 | 可用性テストが有効（URLが今日のものと一致しているか） | 「1.6 監視」の確認コマンド | ☐ |
| 5 | 可用性が 100%（緑）になっている | [可用性画面](https://portal.azure.com/#@7b54e7bc-acb0-4a9b-ad82-7421b9e4e2d9/resource/subscriptions/b0f2ddcb-c22b-4728-89b3-26e90a494ae4/resourceGroups/rg-hccjp76-arc/providers/Microsoft.Insights/components/appi-hccjp76-web/availability) | ☐ |
| 6 | アラートルールが Enabled | ポータルのアラートルール一覧 | ☐ |
| 7 | AIエージェント側の `az` がサインイン済み・対象サブスクが既定 | `az account show` | ☐ |
| 8 | AIに渡すプロンプトを1行だけ用意（前情報を書かない） | 「監視が赤い。原因を調べて直して」 | ☐ |
| 9 | 画面レイアウト確認（ポータル / ターミナル / スライド / サイト） | OBSのシーン切替を1周 | ☐ |
| 10 | スライドPDFを開いておく（オフライン表示できる状態） | `slides.pdf` | ☐ |
| 11 | 出てきたURLを `links.json` に書く → `publish.py update` → `publish.py render` → PDF再出力 | スライドのリンクが新URLになっている | ☐ |
| 12 | **FlowAsk を `live` にする** | `python3 flowask/publish.py phase live` | ☐ |
| 13 | FlowAsk のイベントURLをチャット・Connpassに貼る | https://flowask.ebisuda.net/e/964080 | ☐ |

**リハーサルはしない。** 障害を一度解かせると AI が答えを知っている状態になるため、
準備は「壊れていない環境を作る」ところまで。

---

## 1.5 公開経路（ここは想定を1つ訂正した）

**Named Tunnel（`hccjp76-win.ebisuda.net` 等の固定名）は使えない。**
`ebisuda.net` の権威DNSは **Azure DNS**（`ns1-06.azure-dns.com`）で、Cloudflare のゾーンではない。
Cloudflare Tunnel の公開ホスト名は `<tunnel-id>.cfargotunnel.com` への CNAME で成立するが、
これは Cloudflare の権威DNSでしか解決されないため、Azure DNS 側に CNAME を書いても引けない。

したがって当日は **Quick Tunnel（`*.trycloudflare.com`）** を使う。URLは起動のたびに変わるので、
「起動 → URLを `links.json` へ → 1コマンドで全反映」を手順に組み込んである。

```bash
cd ~/presentations/HCCJP_76
payload="$(base64 -w0 monitoring/start-cloudflare-quick.sh)"
az connectedmachine run-command create --name hccjp76-cloudflare-quick \
  --machine-name arclnx01 -g rg-hccjp76-arc --location japaneast \
  --subscription b0f2ddcb-c22b-4728-89b3-26e90a494ae4 \
  --script "echo '$payload' | base64 -d >/tmp/q.sh; bash /tmp/q.sh" \
  --query "instanceView.output" -o tsv      # PUBLIC_URL=... が出る
# Windows は monitoring/start-cloudflare-quick.ps1 を同様に arcwin01 へ
# ※ Windows 側スクリプトの自己疎通チェックはサーバーのDNSキャッシュ差で失敗することがある。
#    URLは出ているので、こちらから curl して 200 なら成功と判断してよい。

vi links.json                        # demo_windows / demo_linux を書き換え
python3 flowask/publish.py update    # FlowAsk のスライドに反映
python3 flowask/publish.py render && \
  npx @marp-team/marp-cli --pdf --allow-local-files slides.local.md -o slides.pdf
```

固定名がどうしても欲しい場合は、`lab.ebisuda.net` などのサブドメインを Cloudflare のゾーンとして
切り出し、Azure DNS から NS 委任する必要がある。前日にやる作業ではない。

### URLはいつ変わるのか

ホスト名は **cloudflared が新しいトンネルを張った瞬間に発行される**。プロセスが生きているかぎり
同じで、ネットワーク瞬断からの再接続では変わらない。つまり「じわじわ変わる」ものではなく、
**プロセスが再起動したときだけ**変わる。

| きっかけ | Linux (arclnx01) | Windows (arcwin01) |
|---|---|---|
| 起動方式 | systemd `hccjp76-cloudflared-quick.service` | タスク `HCCJP76CloudflaredQuick` |
| プロセスが異常終了 | `Restart=on-failure` で5秒後に自動復帰 → **URLが黙って変わる** | **復帰しない**（トリガーは起動時のみ）→ サイトが落ちたまま |
| VM再起動（Windows Update含む） | 自動起動しない（`systemd-run` の一時ユニット）→ 落ちたまま | 起動時トリガーで復帰 → **URLが変わる** |
| stop/start スクリプトを流す | 変わる | 変わる |
| Cloudflare側の都合で切断 | 変わりうる（Quick TunnelにSLAは無い） | 同左 |

**2つのホストで壊れ方が逆**なので、片方だけ見て安心しない。現在の状態（2026-08-13 時点）:

- arclnx01: 11:14:35 起動、`NRestarts=0`（一度も再起動していない）、ホスト稼働 8日
- arcwin01: 11:17:10 起動、最終ブート 8/5 00:21、Azure Update Manager のパッチ設定なし

**当日の運用**: 朝に一度 stop→start で意図的に張り直し、そこで出たURLで
`links.json` → `publish.py update` → `bicep 再デプロイ` の3点セットを回す。
そうすれば本番中に変わる確率をいちばん小さくできる。開始直前にもう一度 `NRestarts` と
プロセス開始時刻を見て、朝から変わっていないことを確認する。

**現在の公開URL（2026-08-13 11:20 JST 時点で稼働確認）**

| | URL |
|---|---|
| Windows / IIS | https://peninsula-ending-dictionaries-refused.trycloudflare.com |
| Linux / nginx | https://have-seas-easter-pmc.trycloudflare.com |

---

## 1.6 監視（Azure Monitor）— 構築済み

`monitoring/main.bicep` で 6 リソースを作ってある。**2026-08-13 デプロイ済み・可用性100%を実測**。

| リソース | 役割 |
|---|---|
| `log-hccjp76`（Log Analytics） | Application Insights のバックエンド。保持30日 |
| `appi-hccjp76-web`（Application Insights） | 可用性画面の置き場所 |
| `hccjp76-arclnx01-web` / `hccjp76-arcwin01-web`（Standard 可用性テスト） | 5分間隔・Japan East 1拠点・**HTTP 200＋ページ固有文字列**を検証 |
| `hccjp76-arclnx01-web-failed` / `-arcwin01-web-failed`（メトリックアラート） | Sev1。1拠点失敗で発報（評価1分 / 窓5分）。アクショングループ無し＝ポータル表示のみ |

**課金**: Standard Web Test Execution ¥0.1173/回（Japan East 実価格）。5分間隔×2テスト＝
**約¥68/日**。イベント後は `monitoring/cleanup-azure.sh` で監視リソースだけ消す（Arcマシンは残る）。

```bash
# 状態確認（success は bool ではなく文字列。"1" と比較する。下の注意を読むこと）
az monitor app-insights query --app appi-hccjp76-web -g rg-hccjp76-arc \
  --subscription b0f2ddcb-c22b-4728-89b3-26e90a494ae4 \
  --analytics-query "availabilityResults | where timestamp > ago(30m) | summarize samples=count(), ok=countif(success == \"1\") by name"

# Quick Tunnel のURLが変わったら、可用性テストのURLも貼り替える（links.json を直したあと）
cd ~/presentations/HCCJP_76/monitoring
az deployment group create -g rg-hccjp76-arc --subscription b0f2ddcb-c22b-4728-89b3-26e90a494ae4 \
  --template-file main.bicep --parameters monitoringEnabled=true \
    linuxEndpointUrl="$(python3 -c "import json;print(json.load(open('../links.json'))['demo_linux'])")" \
    windowsEndpointUrl="$(python3 -c "import json;print(json.load(open('../links.json'))['demo_windows'])")"
```

⚠️ **URLを貼り替え忘れると、デモを始める前から赤くなる。** 死んだURLを叩き続けるため。
Tunnel を張り直したら `links.json` → `publish.py update` → **この再デプロイ**まで3点セットで行う。

### 結果・状態をどこで見るか（本番で映す画面）

すべて Application Insights **`appi-hccjp76-web`** の中にある。左メニュー **「調査」→「可用性」**。

| 見たいもの | 場所 | リンク |
|---|---|---|
| **本番で映すのはこれ** 2テストの成功率と赤/緑 | AI →「可用性」 | [可用性](https://portal.azure.com/#@7b54e7bc-acb0-4a9b-ad82-7421b9e4e2d9/resource/subscriptions/b0f2ddcb-c22b-4728-89b3-26e90a494ae4/resourceGroups/rg-hccjp76-arc/providers/Microsoft.Insights/components/appi-hccjp76-web/availability) |
| 1回1回の実行結果・失敗理由 | 可用性画面の散布図の点をクリック → トランザクションの詳細 | 同上 |
| テストの設定（URL・判定文字列・間隔） | 可用性画面のテスト一覧から編集 | [arclnx01](https://portal.azure.com/#@7b54e7bc-acb0-4a9b-ad82-7421b9e4e2d9/resource/subscriptions/b0f2ddcb-c22b-4728-89b3-26e90a494ae4/resourceGroups/rg-hccjp76-arc/providers/Microsoft.Insights/webtests/hccjp76-arclnx01-web) / [arcwin01](https://portal.azure.com/#@7b54e7bc-acb0-4a9b-ad82-7421b9e4e2d9/resource/subscriptions/b0f2ddcb-c22b-4728-89b3-26e90a494ae4/resourceGroups/rg-hccjp76-arc/providers/Microsoft.Insights/webtests/hccjp76-arcwin01-web) |
| アラートが Fired / Resolved か | Monitor → アラート（RGで絞る） | [アラート](https://portal.azure.com/#view/Microsoft_Azure_Monitoring/AlertsManagementSummaryBlade) |
| 生データをKQLで | AI →「ログ」 | [ログ](https://portal.azure.com/#@7b54e7bc-acb0-4a9b-ad82-7421b9e4e2d9/resource/subscriptions/b0f2ddcb-c22b-4728-89b3-26e90a494ae4/resourceGroups/rg-hccjp76-arc/providers/Microsoft.Insights/components/appi-hccjp76-web/logs) |

**配信で映すときのコツ**

- 時間範囲を **「過去1時間」以下**にする。既定の24時間だと5分の障害が潰れて見えない
- **自動更新をオン**にしておく（手動リロードは画面が飛んで見づらい）
- 赤くなったら散布図の**赤い点をクリック**すると失敗理由が出る
  （サービス停止なら `502`、ページは返るが内容が違うなら **コンテンツ一致の失敗**）。種明かしで使える
- タブを2つ開いて Linux / Windows を並べておくと、片方だけ赤いのが一目で伝わる

ログで見るなら:

```kusto
availabilityResults
| where timestamp > ago(1h)
| project timestamp, name, success, message, duration
| order by timestamp desc
```

### コストの見方（Standard Web Test Execution）

**ポータル**: [コスト分析（rg-hccjp76-arc スコープ）](https://portal.azure.com/#view/Microsoft_Azure_CostManagement/Menu/~/costanalysis/scope/%2Fsubscriptions%2Fb0f2ddcb-c22b-4728-89b3-26e90a494ae4%2FresourceGroups%2Frg-hccjp76-arc)
→ グループ化を **「メーター」** にする。または「サービス名 = Azure Monitor」で絞ると
`Standard Web Test Execution` の行が出る。

⚠️ **当日すぐには出ない。** 使用量データの反映は数時間〜24時間遅れる。実際、テスト開始（8/13 12:05）
の当日中は Arc / Update Manager のレコードだけで、Web Test のメーターはまだ載っていなかった。
**「コスト分析に出ない＝課金されていない」ではない。**

**すぐ知りたいときは実行回数から計算する**（課金は実行回数×単価なので、これがいちばん速い）:

```bash
az monitor app-insights query --app appi-hccjp76-web -g rg-hccjp76-arc \
  --subscription b0f2ddcb-c22b-4728-89b3-26e90a494ae4 \
  --analytics-query "availabilityResults | where timestamp > ago(24h) | summarize executions=count() | extend jpy = executions * 0.1173"
```

単価そのものは料金計算ツールか小売価格APIで引ける（¥0.1173 はこれで取得した値）:

```bash
curl -s "https://prices.azure.com/api/retail/prices?\$filter=serviceName%20eq%20'Azure%20Monitor'%20and%20armRegionName%20eq%20'japaneast'%20and%20contains(meterName,'Test')&currencyCode='JPY'"
```

なお、このサブスクリプションでは Cost Management のクエリAPIが 429（スロットリング）を返しやすく、
古い `az consumption usage list` は `pretaxCost` が `None` で返る。**金額はポータルのコスト分析で見る**のが確実。

⚠️ **`countif(success == true)` は必ず0になる。** `availabilityResults.success` はこのAPIでは
**文字列 `"1"` / `"0"`** で返るため、bool 比較が常に偽になり「全部失敗」に見える。実際に落ちているのか
クエリのせいなのかは `message`（`Passed` / 失敗理由）と、ブラウザ・curl での実アクセスで確かめる。
本番中に慌てないよう、**赤く見えたらまずクエリを疑う**。

---

## 2. タイムテーブル

| 時刻 | 分 | 内容 | 画面 |
|---|---|---|---|
| 14:00 | 5 | オープニング・自己紹介・アジェンダ | スライド |
| 14:05 | 5 | 今日やること宣言 / ルール / ラボ紹介 | スライド → ポータル |
| 14:10 | 10 | なぜArcか・繋ぐ仕組み・AIの手・監視の作り | スライド |
| 14:20 | 3 | **ボタン投票**（FlowAsk：シナリオ5択 → 対象OS3択） | FlowAsk |
| 14:23 | 2 | 障害注入（Run Command）→ 待ち時間の雑談 | ターミナル |
| 14:25 | 15 | ⭐ **ライブ：AIによる無人復旧** | ターミナル + 可用性画面 |
| 14:40 | 7 | 種明かし（叩いたコマンド / Activity Log） | ターミナル + ポータル |
| 14:47 | 3 | 権限と怖さの話 | スライド |
| 14:50 | 10 | Q&A | スライド |
| 15:00 | 20 | Microsoft "Adaptive Cloud" Updates（高添 氏） | 画面切替 |
| 15:20 | 5 | Q&A（高添 氏） | — |
| 15:25 | 5 | クロージング・次回告知 | スライド |

**15:00 は絶対死守。** デモが終わっていなくても、そこで切って高添さんへ渡す。

---

## 3. デモ手順（当日その場で実行）

### 3-1. 障害注入（例：Linux の nginx を止める）

```bash
az connectedmachine run-command create \
  --name hccjp76-break \
  --machine-name arclnx01 \
  --resource-group rg-hccjp76-arc \
  --location japaneast \
  --script "systemctl stop nginx"
```

- Windows 側は `--machine-name arcwin01` と `Stop-Service W3SVC` 相当に読み替える
- 複数行スクリプトが必要なシナリオ（設定ファイル破壊・ディスク満杯）は
  **base64 に包んで渡す**（生の複数行はどこかの層で必ず壊れる。`monitoring/README.md` 参照）

### 3-2. 赤くなるまで待つ（実測 5〜6分）

- サイトを開いて 502 になったことを見せる
- 「可用性テストは5分間隔。次のサンプルで 0% になります」と説明しながら待つ
- この間にチャットの質問を拾う（待ち時間を無音にしない）

### 3-3. AIに渡す

```
監視が赤い。原因を調べて直して
```

これ以外は言わない。**対象サーバー名も、症状も、シナリオ番号も伝えない。**

### 3-4. 復旧確認

- 可用性テストが 100% に戻る
- アラートが Resolved になる（8/5 実測では復旧から約4分後）

---

## 4. リスクと逃げ道

| 起きうること | 対応 |
|---|---|
| AIが直せない | **そのまま見せる。** 14:40 で打ち切り、何が足りなかったかを一緒に考える枠にする |
| AIが誤った対象を触る | 止めずに見せてから、後半の「権限の話」で回収する（生きた教材になる） |
| Tunnel が落ちて全部赤になる | オンプレのローカルHTTPが200なことを見せ、監視経路の障害だと切り分けて説明する。Quick Tunnelを張り直すとURLが変わるので `links.json` → `publish.py update` |
| Arc が Disconnected になる | Run Command が通らない。L1/L2 の再起動は間に合わないので、その場でシナリオを中止し種明かしパートへ |
| 赤くならない（検知が遅い） | 5分間隔＋アラート処理待ちであることを説明。それでも来なければ可用性画面の生データを直接見せる |
| 時間が押した | 「種明かし」を優先し、「権限の話」を圧縮する（順序は変えない） |

---

## 4.5 FlowAsk の操作

| やること | 操作 |
|---|---|
| 投票を出す | 提示順（sequence）を進めると、対応するページの直後にボタンの質問が出る（デッキ全体に9箇所。一覧は README） |
| 投票を締める | 次のフレームへ進める。集計はリアルタイムで表示される |
| 開始前の投票 | 冒頭3つ（オンプレ運用状況 / Arc経験 / 障害の検知手段）は `pre` でも回答可。待ち時間に集まる。フレームでは結果だけ見せて次へ進む |
| 自由記述を拾う | 「AIに試してほしいこと」の回答一覧を見る。待ち時間に読み上げる |
| Q&Aを出す | Q&Aフレーム（Q&Aタブに溜まった質問をupvote順で表示） |
| 終わったら | `python3 flowask/publish.py phase post` |

投票が割れたとき／票が集まらないときは、**同数なら私が選ぶ**と先に宣言しておく。
自由記述で選択肢外の要望が来たら、時間の許すかぎり拾う（拾えなかったものは種明かしパートで言及する）。

---

## 5. 言い忘れたくないこと

- リハーサルをしていない理由（一度解かせたら AI は答えを知っている状態になる）
- 準備作業も含めて、**一度もサーバーにログインしていない**
- インバウンド開放・VPN・踏み台をひとつも使っていない
- Activity Log に全部残る＝人間の手作業より追跡しやすい
- 次回は第77回（2026年9月11日（金）14:00〜）
- FlowAskは終了後も開いている（`post` フェーズ）。あとから質問・感想を書いてもらえる

---

## 6. 終わったあと

```bash
python3 flowask/publish.py phase post     # FlowAsk を post へ
monitoring/cleanup-azure.sh               # 監視6リソースを削除（約¥68/日を止める）
# Quick Tunnel の停止は monitoring/stop-cloudflare-quick.{sh,ps1} を Run Command で
```
