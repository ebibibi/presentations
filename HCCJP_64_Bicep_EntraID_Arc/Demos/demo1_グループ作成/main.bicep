extension microsoftGraphV1

resource exampleGroup 'Microsoft.Graph/groups@v1.0' = {
  displayName: 'hccjp demo group by bicep'
  mailEnabled: false
  mailNickname: 'hccjp-demo-group'
  securityEnabled: true
  uniqueName: 'hccjp-demo-group'
}

