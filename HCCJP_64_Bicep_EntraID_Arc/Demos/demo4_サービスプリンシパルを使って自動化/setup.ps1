# リソースグループの作成
az group create --name demo4 --location eastus

# サービスプリンシパルを作成し、Managed Identity Contributorロールを割り当てる
$mySubscriptionId = (az account show --query id -o tsv)
$myservicePrincipalName = "HCCJPServicePrincipaldemo1"
$myResourceGroupName = "demo4"
$output = az ad sp create-for-rbac --name $myservicePrincipalName --role "Managed Identity Contributor" --scopes "/subscriptions/$mySubscriptionId/resourceGroups/$myResourceGroupName"
$output

# outputから必要な情報を取得
$myServicePrincipalId = $output | ConvertFrom-Json | Select-Object -ExpandProperty appId
$myServicePrincipalSecret = $output | ConvertFrom-Json | Select-Object -ExpandProperty password
$myServicePrincipalTenant = $output | ConvertFrom-Json | Select-Object -ExpandProperty tenant


# Microsoft Graphのアクセス許可をサービスプリンシパルに割り当てる

# Microsoft Graph PowerShell SDKをインストールしていない場合は、以下のコマンドでインストール
# Install-Module Microsoft.Graph -Scope CurrentUser
Connect-MgGraph -Scopes "AppRoleAssignment.ReadWrite.All","Application.Read.All" # admin@ebibibigmail.onmicrosoft.comでログイン

# 作成済みのサービスプリンシパルを取得
$mySP = Get-MgServicePrincipalByAppId -AppId $myServicePrincipalId

# Microsoft GraphのService Principalを取得
$graphSP = Get-MgServicePrincipalByAppId -AppId "00000003-0000-0000-c000-000000000000"

# Assign Group.ReadWrite.All app-only permission
# サービスプリンシパルにGroup.ReadWrite.AllとUser.Read.Allを割り当てる
# 参考：https://learn.microsoft.com/ja-jp/graph/permissions-reference
New-MgServicePrincipalAppRoleAssignedTo -ResourceId $graphSP.Id -ServicePrincipalId $graphSP.Id -PrincipalId $mySP.Id -AppRoleId "62a82d76-70ea-41e2-9197-370581804d09"
New-MgServicePrincipalAppRoleAssignedTo -ResourceId $graphSP.Id -ServicePrincipalId $graphSP.Id -PrincipalId $mySP.Id -AppRoleId "df021288-bdef-4463-88db-98f22de89214"



# (デモのために)別のターミナルを開いて以下のコマンドを実行してサービスプリンシパルでログイン
Write-Host "az login --service-principal --username $myServicePrincipalId --password $myServicePrincipalSecret --tenant $myServicePrincipalTenant"

# bicepのデプロイ
az deployment group create --resource-group demo4 --template-file main.bicep

#------------------------------------------------------------------------------
# Azure PowerShell版
Write-Host "`$cred = New-Object System.Management.Automation.PSCredential -ArgumentList $myServicePrincipalId, (ConvertTo-SecureString $myServicePrincipalSecret -AsPlainText -Force)"
Write-Host "Connect-AzAccount -ServicePrincipal -Tenant $myServicePrincipalTenant -Credential `$cred"
# Azure PowerShellでのデプロイ
New-AzResourceGroupDeployment -ResourceGroupName demo4 -TemplateFile main.bicep
