# リアルタイム投票システム設計書

## 概要
20分で実装できるシンプルなリアルタイム投票システム

## システム構成

### 使用するAzureサービス
1. **Azure Static Web Apps** - フロントエンドホスティング
2. **Azure SignalR Service** - リアルタイム通信
3. **Azure Functions** - サーバーレスAPI

### アーキテクチャ
```
[ブラウザ] <--> [Azure Static Web Apps] 
    |               |
    |               v
    |        [Azure Functions]
    |         - negotiate
    |         - sendVote
    |         - getResults
    |               |
    v               v
[Azure SignalR Service]
```

## 機能仕様

### 投票機能
- **質問**: 「好きなプログラミング言語は？」
- **選択肢**: 
  - JavaScript
  - Python
  - C#
  - Java
- **制限**: なし（同一ユーザーが複数回投票可能）
- **認証**: なし（匿名投票）

### リアルタイム更新
- 投票するとすべての接続クライアントに即座に反映
- 円グラフで結果表示
- 投票数と割合を表示

## 実装詳細

### フロントエンド（index.html）
- シンプルなHTML + JavaScript
- SignalR JavaScript クライアントライブラリ使用
- Chart.jsで円グラフ表示

### Azure Functions
1. **negotiate関数**
   - SignalR接続情報を返す
   - HTTPトリガー

2. **sendVote関数**
   - 投票を受け付ける
   - すべてのクライアントに結果を配信
   - HTTPトリガー + SignalR出力バインディング

3. **getResults関数**
   - 現在の投票結果を返す
   - HTTPトリガー

### データストレージ
- インメモリ（Functionsのstatic変数）
- 再起動で消える（デモには十分）

## デプロイ手順

### 1. リソース作成（5分）
```bash
# リソースグループ作成
az group create --name rg-vote-demo --location japaneast

# SignalR Service作成
az signalr create --name signalr-vote-demo --resource-group rg-vote-demo --sku Free_F1 --service-mode Serverless

# Function App作成
az functionapp create --resource-group rg-vote-demo --name func-vote-demo --consumption-plan-location japaneast --runtime node --runtime-version 18

# Static Web App作成（手動でポータルから）
```

### 2. Functions実装とデプロイ（10分）
- negotiate, sendVote, getResults関数を実装
- func azure functionapp publish コマンドでデプロイ

### 3. フロントエンド実装とデプロイ（5分）
- index.htmlを作成
- Static Web Appsにデプロイ

## セキュリティ考慮事項
- CORSの設定（Functions側で許可）
- 本番環境では認証・レート制限が必要（今回は省略）

## 拡張可能性
- Azure Cosmos DBを追加して永続化
- Azure AD B2Cで認証追加
- 複数の投票を管理
- 投票履歴の表示