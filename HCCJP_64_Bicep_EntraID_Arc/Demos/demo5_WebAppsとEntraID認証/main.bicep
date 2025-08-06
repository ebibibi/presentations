extension microsoftGraphV1

param location string = resourceGroup().location
param appName string = 'mywebapp-${uniqueString(resourceGroup().id)}'
param appServicePlanName string = 'asp-${appName}'
param tenantId string = tenant().tenantId
param redirectUri string = 'https://${appName}.azurewebsites.net/.auth/login/aad/callback'

@description('App Service Plan SKU')
@allowed([
  'F1'
  'B1'
  'B2'
  'S1'
  'S2'
  'P1v2'
  'P2v2'
])
param appServicePlanSku string = 'B1'

// Entra ID アプリケーション登録
resource entraApp 'Microsoft.Graph/applications@v1.0' = {
  uniqueName: appName
  displayName: 'WebApp ${appName}'
  signInAudience: 'AzureADMyOrg'
  web: {
    redirectUris: [
      redirectUri
    ]
    implicitGrantSettings: {
      enableIdTokenIssuance: true
      enableAccessTokenIssuance: false
    }
  }
  requiredResourceAccess: [
    {
      // Microsoft Graph
      resourceAppId: '00000003-0000-0000-c000-000000000000'
      resourceAccess: [
        {
          // User.Read
          id: 'e1fe6dd8-ba31-4d61-89e7-88639da4683d'
          type: 'Scope'
        }
        {
          // profile
          id: '14dad69e-099b-42c9-810b-d002981feec1'
          type: 'Scope'
        }
        {
          // openid
          id: '37f7f235-527c-4136-accd-4a02d197296e'
          type: 'Scope'
        }
      ]
    }
  ]
}

// サービスプリンシパル
resource servicePrincipal 'Microsoft.Graph/servicePrincipals@v1.0' = {
  appId: entraApp.appId
}

// App Service Plan
resource appServicePlan 'Microsoft.Web/serverfarms@2023-01-01' = {
  name: appServicePlanName
  location: location
  sku: {
    name: appServicePlanSku
  }
  kind: 'windows'
  properties: {
    reserved: false
  }
}

// Web App
resource webApp 'Microsoft.Web/sites@2023-01-01' = {
  name: appName
  location: location
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      netFrameworkVersion: 'v6.0'
      metadata: [
        {
          name: 'CURRENT_STACK'
          value: 'dotnet'
        }
      ]
    }
  }
  identity: {
    type: 'SystemAssigned'
  }
}

// 認証設定
resource authSettings 'Microsoft.Web/sites/config@2023-01-01' = {
  parent: webApp
  name: 'authsettingsV2'
  properties: {
    platform: {
      enabled: true
    }
    globalValidation: {
      requireAuthentication: true
      unauthenticatedClientAction: 'RedirectToLoginPage'
    }
    identityProviders: {
      azureActiveDirectory: {
        enabled: true
        registration: {
          openIdIssuer: 'https://sts.windows.net/${tenantId}/v2.0'
          clientId: entraApp.appId
        }
        validation: {
          allowedAudiences: [
            'api://${entraApp.appId}'
          ]
        }
      }
    }
    login: {
      tokenStore: {
        enabled: true
      }
    }
  }
}

// アプリケーション設定
resource appSettings 'Microsoft.Web/sites/config@2023-01-01' = {
  parent: webApp
  name: 'appsettings'
  properties: {
    MICROSOFT_PROVIDER_AUTHENTICATION_APPID: entraApp.appId
    WEBSITE_AUTH_AAD_ALLOWED_TENANTS: tenantId
  }
}

output webAppUrl string = 'https://${webApp.properties.defaultHostName}'
output applicationId string = entraApp.appId
output tenantId string = tenantId
output webAppName string = webApp.name
output appServicePlanName string = appServicePlan.name
