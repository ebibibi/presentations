# サインイン
az login -t 7b54e7bc-acb0-4a9b-ad82-7421b9e4e2d9

# リソースグループ作成
az group create --name hccjp-bicep-entra-arc --location japaneast

# 展開
az deployment group create --resource-group hccjp-bicep-entra-arc --template-file main.bicep
