const { app, output } = require('@azure/functions');

// インメモリでの投票データ保存
global.votes = global.votes || {
    JavaScript: 0,
    Python: 0,
    'C#': 0,
    Java: 0
};

const signalROutput = output.generic({
    type: 'signalR',
    name: 'signalRMessages',
    hubName: 'votehub',
    connectionStringSetting: 'AzureSignalRConnectionString'
});

app.http('sendVote', {
    methods: ['POST'],
    authLevel: 'anonymous',
    extraOutputs: [signalROutput],
    handler: async (request, context) => {
        const body = await request.json();
        const { language } = body;

        // 投票の検証
        if (!language || !global.votes.hasOwnProperty(language)) {
            return { status: 400, body: 'Invalid language' };
        }

        // 投票を記録
        global.votes[language]++;

        // 全クライアントに結果を送信
        context.extraOutputs.set(signalROutput, [{
            target: 'updateResults',
            arguments: [global.votes]
        }]);

        return { body: JSON.stringify({ success: true, votes: global.votes }) };
    }
});