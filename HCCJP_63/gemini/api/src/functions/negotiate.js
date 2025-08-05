const { app, input } = require('@azure/functions');

const signalRConnectionInfo = input.generic({
    type: 'signalRConnectionInfo',
    name: 'connectionInfo',
    hubName: 'serverless',
    connectionStringSetting: 'AzureSignalRConnectionString',
});

app.post('negotiate', {
    authLevel: 'anonymous',
    handler: (request, context) => {
        return { body: JSON.stringify(context.extraInputs.get(signalRConnectionInfo)) };
    },
    route: 'negotiate',
    extraInputs: [signalRConnectionInfo],
});
