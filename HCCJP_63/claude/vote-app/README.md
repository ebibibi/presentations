# リアルタイム投票システム

20分で構築できるシンプルなリアルタイム投票システムです。

## 構成要素
- **フロントエンド**: HTML + JavaScript (Chart.js, SignalR)
- **バックエンド**: Azure Functions (Node.js)
- **リアルタイム通信**: Azure SignalR Service

## ローカル実行方法

### 前提条件
- Node.js 18以上
- Azure Functions Core Tools v4
- Azureアカウント

### 手順

1. Azureリソースを作成
```bash
./vote-app/deploy-azure-resources.sh
```

2. SignalR接続文字列を設定
スクリプト実行後に表示される接続文字列を `backend/local.settings.json` に設定

3. Functions を起動
```bash
cd vote-app/backend
npm install
func start
```

4. 別ターミナルでフロントエンドを起動
```bash
cd vote-app/frontend
# Python 3の場合
python -m http.server 8080
# またはnpx
npx http-server -p 8080
```

5. ブラウザで `http://localhost:8080` を開く

## Azure へのデプロイ

### Functions のデプロイ
```bash
cd vote-app/backend
func azure functionapp publish <FUNCTION_APP_NAME>
```

### Static Web App の作成とデプロイ
1. Azure Portal で Static Web App を作成
2. frontend フォルダの内容をデプロイ
3. Functions の URL を環境変数に設定

## 機能
- 4つのプログラミング言語から選択して投票
- リアルタイムで全クライアントに結果を反映
- 円グラフで視覚的に結果を表示