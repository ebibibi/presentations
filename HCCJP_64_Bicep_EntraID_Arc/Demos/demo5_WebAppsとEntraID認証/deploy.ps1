# リソースグループ名とロケーションの設定
$resourceGroupName = "demo5"
$location = "japaneast"

# リソースグループの作成
az group create --name $resourceGroupName --location $location

# Bicep テンプレートのデプロイ
az deployment group create `
    --resource-group $resourceGroupName `
    --template-file ".\main.bicep"