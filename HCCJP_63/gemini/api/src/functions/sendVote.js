const { app, output } = require('@azure/functions');

const signalR = output.generic({
    type: 'signalR',
    name: 'signalR',
    hubName: 'serverless',
    connectionStringSetting: 'AzureSignalRConnectionString',
});

app.http('sendVote', {
    methods: ['POST'],
    authLevel: 'anonymous',
    extraOutputs: [signalR],
    handler: async (request, context) => {
        const vote = await request.text();
        context.extraOutputs.set(signalR, 
            {
                'target': 'newVote',
                'arguments': [vote]
            });
    }
});
