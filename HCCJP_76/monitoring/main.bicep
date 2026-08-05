@description('Public Linux HTTP or HTTPS endpoint exposed by Cloudflare Tunnel.')
param linuxEndpointUrl string

@description('Public Windows HTTP or HTTPS endpoint exposed by Cloudflare Tunnel.')
param windowsEndpointUrl string

@description('Azure region for the workspace and Application Insights resource.')
param location string = 'japaneast'

@description('Enable paid Standard availability test executions and metric alerts.')
param monitoringEnabled bool = false

@description('Optional Action Group resource ID. Leave empty when only the portal view is needed.')
param actionGroupId string = ''

var prefix = 'hccjp76'
var workspaceName = 'log-${prefix}'
var appInsightsName = 'appi-${prefix}-web'
var targets = [
  {
    name: 'arclnx01'
    endpointUrl: linuxEndpointUrl
    expectedContent: 'Ubuntu 24.04 LTS'
  }
  {
    name: 'arcwin01'
    endpointUrl: windowsEndpointUrl
    expectedContent: 'Windows Server 2025'
  }
]

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

resource webTests 'Microsoft.Insights/webtests@2022-06-15' = [for target in targets: {
  name: '${prefix}-${target.name}-web'
  location: location
  kind: 'standard'
  tags: {
    'hidden-link:${appInsights.id}': 'Resource'
  }
  properties: {
    Name: '${prefix}-${target.name}-web'
    Description: 'HCCJP 76 on-premises ${target.name} availability through Cloudflare Tunnel'
    Enabled: monitoringEnabled
    Frequency: 300
    Timeout: 30
    Kind: 'standard'
    RetryEnabled: false
    SyntheticMonitorId: '${prefix}-${target.name}-web'
    Locations: [
      {
        Id: 'apac-jp-kaw-edge'
      }
    ]
    Request: {
      RequestUrl: target.endpointUrl
      HttpVerb: 'GET'
      FollowRedirects: true
      ParseDependentRequests: false
    }
    ValidationRules: {
      ExpectedHttpStatusCode: 200
      IgnoreHttpStatusCode: false
      SSLCheck: startsWith(toLower(target.endpointUrl), 'https://')
      ContentValidation: {
        ContentMatch: target.expectedContent
        IgnoreCase: false
        PassIfTextFound: true
      }
    }
  }
}]

resource availabilityAlerts 'Microsoft.Insights/metricAlerts@2018-03-01' = [for (target, index) in targets: {
  name: '${prefix}-${target.name}-web-failed'
  location: 'global'
  tags: {
    'hidden-link:${appInsights.id}': 'Resource'
    'hidden-link:${webTests[index].id}': 'Resource'
  }
  properties: {
    description: 'The HCCJP 76 on-premises ${target.name} web endpoint failed its Azure Monitor availability test.'
    severity: 1
    enabled: monitoringEnabled
    scopes: [
      webTests[index].id
      appInsights.id
    ]
    evaluationFrequency: 'PT1M'
    windowSize: 'PT5M'
    criteria: {
      'odata.type': 'Microsoft.Azure.Monitor.WebtestLocationAvailabilityCriteria'
      webTestId: webTests[index].id
      componentId: appInsights.id
      failedLocationCount: 1
    }
    actions: empty(actionGroupId) ? [] : [
      {
        actionGroupId: actionGroupId
      }
    ]
  }
}]

output applicationInsightsResourceId string = appInsights.id
output webTestResourceIds array = [for (_, index) in targets: webTests[index].id]
output standardTestBillingEnabled bool = monitoringEnabled
