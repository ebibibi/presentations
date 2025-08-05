extension microsoftGraphV1

param location string = resourceGroup().location

resource exampleGroup 'Microsoft.Graph/groups@v1.0' = {
  displayName: 'hccjp demo group by bicep'
  mailEnabled: false
  mailNickname: 'hccjp-demo-group'
  securityEnabled: true
  uniqueName: 'hccjp-demo-group'
  owners: {
    relationships: [managedIdentity.properties.principalId]
  }
}

resource managedIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2018-11-30' = {
  name: 'hccjpDemoManagedIdentity'
  location: location
}
