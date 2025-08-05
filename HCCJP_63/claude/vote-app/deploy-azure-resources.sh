#!/bin/bash

# 変数設定
RESOURCE_GROUP="rg-vote-demo"
LOCATION="japaneast"
SIGNALR_NAME="signalr-vote-demo-$(date +%s)"
FUNCTION_APP_NAME="func-vote-demo-$(date +%s)"
STORAGE_ACCOUNT_NAME="stvotedemo$(date +%s | tail -c 8)"

echo "Azure リソースの作成を開始します..."

# リソースグループ作成
echo "1. リソースグループを作成中..."
az group create --name $RESOURCE_GROUP --location $LOCATION

# SignalR Service作成
echo "2. Azure SignalR Serviceを作成中..."
az signalr create \
  --name $SIGNALR_NAME \
  --resource-group $RESOURCE_GROUP \
  --sku Free_F1 \
  --service-mode Serverless \
  --location $LOCATION

# SignalR接続文字列を取得
echo "3. SignalR接続文字列を取得中..."
SIGNALR_CONNECTION_STRING=$(az signalr key list --name $SIGNALR_NAME --resource-group $RESOURCE_GROUP --query primaryConnectionString -o tsv)

# ストレージアカウント作成
echo "4. ストレージアカウントを作成中..."
az storage account create \
  --name $STORAGE_ACCOUNT_NAME \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --sku Standard_LRS

# Function App作成
echo "5. Function Appを作成中..."
az functionapp create \
  --resource-group $RESOURCE_GROUP \
  --name $FUNCTION_APP_NAME \
  --storage-account $STORAGE_ACCOUNT_NAME \
  --consumption-plan-location $LOCATION \
  --runtime node \
  --runtime-version 18 \
  --functions-version 4

# Function AppにSignalR接続文字列を設定
echo "6. Function Appの設定を更新中..."
az functionapp config appsettings set \
  --name $FUNCTION_APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --settings "AzureSignalRConnectionString=$SIGNALR_CONNECTION_STRING"

# CORS設定
echo "7. CORS設定を更新中..."
az functionapp cors add \
  --name $FUNCTION_APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --allowed-origins "*"

echo ""
echo "============================================"
echo "Azure リソースの作成が完了しました！"
echo "============================================"
echo "リソースグループ: $RESOURCE_GROUP"
echo "SignalR Service: $SIGNALR_NAME"
echo "Function App: $FUNCTION_APP_NAME"
echo "ストレージアカウント: $STORAGE_ACCOUNT_NAME"
echo ""
echo "次のステップ:"
echo "1. backend/local.settings.json のAzureSignalRConnectionStringを更新してください"
echo "2. cd vote-app/backend && func azure functionapp publish $FUNCTION_APP_NAME"
echo "3. Static Web Appを手動で作成し、frontendフォルダをデプロイしてください"
echo ""
echo "SignalR接続文字列:"
echo "$SIGNALR_CONNECTION_STRING"