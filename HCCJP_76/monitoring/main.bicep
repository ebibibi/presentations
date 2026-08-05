@description('Public HTTP or HTTPS endpoint exposed by Cloudflare Tunnel.')
param endpointUrl string

@description('Unique text that must appear in a healthy response.')
param expectedContent string = 'Ubuntu 24.04 LTS'

@description('Azure region for the workspace and Application Insights resource.')
param location string = 'japaneast'

@description('Enable paid Standard availability test executions and its metric alert.')
param monitoringEnabled bool = false

@description('Optional Action Group resource ID. Leave empty when only the portal view is needed.')
param actionGroupId string = ''

var prefix = 'hccjp76'
var workspaceName = 'log-${prefix}'
var appInsightsName = 'appi-${prefix}-web'
var webTestName = '${prefix}-arclnx01-web'

resource workspace 'Microsoft.OperationalInsights/workspaces@2023-09-01' = {
  name: workspaceName
  location: location
  properties: {
    retentionInDays: 30
    features: {
      enableLogAccessUsingOnlyResourcePermissions: true
    }
    sku: {
      name: 'PerGB2018'
    }
  }
}

resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: appInsightsName
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
    WorkspaceResourceId: workspace.id
    RetentionInDays: 30
    publicNetworkAccessForIngestion: 'Enabled'
    publicNetworkAccessForQuery: 'Enabled'
  }
}

resource webTest 'Microsoft.Insights/webtests@2022-06-15' = {
  name: webTestName
  location: location
  kind: 'standard'
  tags: {
    'hidden-link:${appInsights.id}': 'Resource'
  }
  properties: {
    Name: webTestName
    Description: 'HCCJP 76 on-premises nginx availability through Cloudflare Tunnel'
    Enabled: monitoringEnabled
    Frequency: 300
    Timeout: 30
    Kind: 'standard'
    RetryEnabled: false
    SyntheticMonitorId: webTestName
    Locations: [
      {
        Id: 'apac-jp-kaw-edge'
      }
    ]
    Request: {
      RequestUrl: endpointUrl
      HttpVerb: 'GET'
      FollowRedirects: true
      ParseDependentRequests: false
    }
    ValidationRules: {
      ExpectedHttpStatusCode: 200
      IgnoreHttpStatusCode: false
      SSLCheck: startsWith(toLower(endpointUrl), 'https://')
      ContentValidation: {
        ContentMatch: expectedContent
        IgnoreCase: false
        PassIfTextFound: true
      }
    }
  }
}

resource availabilityAlert 'Microsoft.Insights/metricAlerts@2018-03-01' = {
  name: '${webTestName}-failed'
  location: 'global'
  tags: {
    'hidden-link:${appInsights.id}': 'Resource'
    'hidden-link:${webTest.id}': 'Resource'
  }
  properties: {
    description: 'The HCCJP 76 on-premises web endpoint failed its Azure Monitor availability test.'
    severity: 1
    enabled: monitoringEnabled
    scopes: [
      webTest.id
      appInsights.id
    ]
    evaluationFrequency: 'PT1M'
    windowSize: 'PT5M'
    criteria: {
      'odata.type': 'Microsoft.Azure.Monitor.WebtestLocationAvailabilityCriteria'
      webTestId: webTest.id
      componentId: appInsights.id
      failedLocationCount: 1
    }
    actions: empty(actionGroupId) ? [] : [
      {
        actionGroupId: actionGroupId
      }
    ]
  }
}

output applicationInsightsResourceId string = appInsights.id
output webTestResourceId string = webTest.id
output standardTestBillingEnabled bool = monitoringEnabled
