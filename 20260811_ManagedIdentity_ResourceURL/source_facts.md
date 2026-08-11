# 公式ソース抽出事実

取得日: 2026-08-11

## 1. Power Platform カスタムコネクタのチュートリアル

Source: https://learn.microsoft.com/ja-jp/connectors/custom-connectors/azure-active-directory-authentication

- このチュートリアルは、Azure Resource Manager API の1つをカスタムコネクタとして登録し、Power Automateから接続する例である。
- セキュリティ設定の「リソース URL」には `https://management.core.windows.net/` を入力し、末尾のスラッシュを含めて正確に入力するよう記載されている。
- サンプル OpenAPI が含む操作は Resource Manager の `List all subscriptions` である。
- 同ページの「マネージド ID の認証」は、カスタムコネクタがユーザー委任認証のクライアントシークレットの代わりにマネージドIDを使えることを説明している。

## 2. アクセストークンの所有者と audience

Source: https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens

- アクセストークンを要求するクライアントと、アクセストークンを受け入れるリソース（Web API）が存在する。
- トークンの対象リソース（audience）は `aud` クレームで定義される。
- クライアントはトークンを利用し、リソースがトークンを受け入れる。
- リソースは `aud` によって自分向けのトークンを所有する。

Source: https://learn.microsoft.com/en-us/entra/identity-platform/access-token-claims-reference

- `aud` はトークンの意図された受信者を識別する。
- API は `aud` が意図した audience と一致しないトークンを拒否しなければならない。
- v1.0トークンでは `aud` がクライアントIDまたは要求に使ったリソースURIになり得る。v2.0トークンではAPIのクライアントIDになる。

## 3. マネージドIDの token request における resource

Source: https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-to-use-vm-token

- マネージドIDのIMDSエンドポイントでは、`resource` クエリパラメーターが対象リソースの App ID URI を示す。
- 指定した resource は、発行されたトークンの `aud` クレームにも現れる。
- 同ページの新しい Azure Resource Manager 例は `resource=https://management.azure.com/` を使う。

## 4. management.core.windows.net と実際のARMエンドポイント

Source: https://learn.microsoft.com/en-us/rest/api/gettingstarted/

- OAuthの `resource` は、呼び出すREST APIが公開する identifier URI である。
- 同ページには、Azure Resource Manager provider API の例として `https://management.core.windows.net/` が記載されている。
- 同ページは実際の Azure Resource Manager provider API の呼び出し先を `https://management.azure.com/`、classic Azure Service Management API の呼び出し先を `https://management.core.windows.net/` と区別している。

Source: https://learn.microsoft.com/en-us/entra/msal/msal-acquire-cache-tokens

- Azure Resource Manager API のような一部APIは、アクセストークンの `aud` に末尾スラッシュを期待する。
- scope の形式は、トークンを受け取るAPIと、そのAPIが受け入れる `aud` の値に依存する。

Source: https://learn.microsoft.com/en-us/entra/msal/dotnet/how-to/differences-adal-msal-net

- ADAL（v1系）は対象APIを `resource` で指定し、MSAL（v2系）は `scopes` で指定する。
- v1リソースの静的スコープ一式やクライアント資格情報フローをMSALで要求する場合は、Resource IDに `/.default` を付けたscopeを使う。

## 5. Azure AI Search の endpoint と token scope

Source: https://learn.microsoft.com/en-us/azure/search/search-get-started-rbac

- Azure AI Searchへのキーレス接続では Microsoft Entra ID とRBACを利用する。
- Azure CLIでSearch用トークンを取得する例は `az account get-access-token --scope https://search.azure.com/.default` である。
- Search REST API の実際の接続先はサービス固有の `https://<service-name>.search.windows.net` である。

Source: https://learn.microsoft.com/en-us/rest/api/searchservice/documents/search-get

- Azure AI Search data-plane REST APIのOAuthスコープは `https://search.azure.com/.default` である。
- リクエストURLの例は `https://myservice.search.windows.net/indexes('myindex')/docs?...` である。

Source: https://github.com/Azure/azure-sdk-for-net/blob/29aeb7697476ff4b6e55a26735ecee6e5d707d59/sdk/search/Azure.Search.Documents/src/SearchAudience.cs

- MicrosoftのAzure SDK for .NETは、Azure Public CloudのSearch audience定数を `https://search.azure.com` と定義している。
- Search audienceはクラウドごとに異なり、Azure Governmentは `https://search.azure.us`、Azure Chinaは `https://search.azure.cn` である。

Source: https://learn.microsoft.com/en-us/azure/search/search-how-to-managed-identities

- Searchサービス自体の作成・更新を行うmanagement REST APIの例は `https://management.azure.com/subscriptions/.../providers/Microsoft.Search/searchServices/...` を使用する。
- Searchサービスは、インデクサーやベクター化などのために他のAzureリソースへ接続するマネージドIDを持てる。

Source: https://learn.microsoft.com/en-us/azure/search/keyless-connections

- Azure AI Searchで403が返る典型例として、IDに必要なロールがない場合が記載されている。
- Search Index Data ReaderやSearch Index Data Contributorなどの適切なロールを割り当てるよう案内されている。
- ロール割り当ての反映には最大10分かかる場合があると記載されている。

## 6. 値は正確一致させる

Source: https://learn.microsoft.com/en-us/azure/logic-apps/authenticate-with-managed-identity

- Audienceには対象Azureサービスの resource ID を指定する。
- 対象 resource ID は Microsoft Entra ID が期待する値と正確に一致させる必要があり、不一致では 400 または401になり得る。
- 末尾スラッシュが含まれる場合は含め、含まれない場合は追加しない。
- 例として Key Vault は `https://vault.azure.net`、Azure Storage全体は `https://storage.azure.com/` と記載されている。

## この資料で行う整理（作者の説明）

- UI上の「リソースURL」は、ブラウザーで開く住所ではなく、トークンを受け取るAPIを識別する audience / resource identifier と説明する。
- 「endpoint（通信先）」「audience/resource（トークンの宛先）」「Azure resource ID（RBACのスコープに使う `/subscriptions/...`）」を別概念として整理する。
- `resource=<URI>`、カスタムコネクタの「リソースURL」、`scope=<URI>/.default` は、OAuthのバージョンやツールによって表記が異なるが、いずれも対象APIを指定する文脈として説明する。ただし末尾スラッシュを含む正確な文字列は各API・ツールの公式ドキュメントどおりに指定する。
- Azure Resource Managerについては新旧ドキュメント・フローで `management.core.windows.net/` と `management.azure.com/` の双方が登場するため、推測で置換せず、利用中の製品・認証フローの公式手順に従うと注意喚起する。
