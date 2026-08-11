# 構成設計

## 想定視聴者

### 開始時点で知っていること

- マネージドIDやアプリ登録という言葉を見たことがある
- Microsoft Learnの手順に沿って設定しようとしている
- Azure AI Searchなど、呼び出したいAzureサービスが決まっている

### 開始時点で知らないこと

- 「リソースURL」が通信先URLではなく、アクセストークンの対象APIを表すこと
- endpoint、audience/resource、Azure resource IDの違い
- `resource=<URI>` と `scope=<URI>/.default` の関係
- Azure AI Searchの実URLとトークン用URIが異なる理由

## スライドごとの問いと答え

1. この動画で何が分かる？ → リソースURLの正体と探し方
2. なぜ混乱する？ → 1サービスに似たURLが複数あるから
3. リソースURLとは？ → APIの住所ではなくトークンの宛先
4. トークンはどう流れる？ → Entra IDに宛先を伝え、APIがaudを確認する
5. audとは？ → このトークンを受け取ってよいAPIの識別子
6. Learnのmanagement.coreはなぜ？ → サンプルがARM API用トークンを要求するから
7. URLとaudienceが違ってよい？ → 通信先とトークン受取先の識別子は役割が違う
8. Azure AI Searchでは？ → data planeのaudienceはsearch.azure.com、endpointはサービス固有
9. 管理と検索で違う？ → management planeとdata planeで対象APIが違う
10. `.default`は何？ → v2/MSAL系で対象APIの事前同意済み権限を要求する表記
11. 3種類をどう見分ける？ → endpoint / audience / Azure resource IDを分離する
12. 正しい値はどう探す？ → 対象操作とplaneを決め、公式認証欄を確認する
13. エラーの切り分けは？ → 取得失敗、401、403を順に見る
14. 最小実例は？ → Search用scopeで取得し、search.windows.netへ送る
15. 結論は？ → URLを推測せず、誰向けトークンかを考える
16. 参照先は？ → 公式ドキュメント一覧

## 専門用語の初出順

| 用語 | 初出 | 画面内の定義 |
|---|---:|---|
| リソースURL | 1 | トークンを受け取るAPIの識別子 |
| API | 2 | アプリがサービスを呼び出す受付窓口 |
| endpoint | 2 | 実際にHTTPリクエストを送る通信先 |
| アクセストークン | 3 | APIへ見せる期限付き通行証 |
| audience / aud | 3 | その通行証の宛先 |
| Microsoft Entra ID | 4 | 宛先を指定してトークンを発行する認証基盤 |
| Azure Resource Manager | 6 | Azureリソースを作成・設定する管理API |
| data plane | 8 | 検索・データ読み書きなどサービス機能を使うAPI側 |
| management plane | 9 | Azureリソースそのものを作成・設定する管理API側 |
| scope / .default | 10 | v2系のトークン要求で対象APIと事前同意済み権限を表す形式 |
| Azure resource ID | 11 | `/subscriptions/...` から始まるAzure上の個別リソース識別子 |

## 高橋メソッドで強調する節目

- 3: 「住所ではない」
- 7: 「違っていていい」
- 15: 「誰向けの通行証？」
