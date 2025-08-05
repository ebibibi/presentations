const { app } = require('@azure/functions');

// グローバル投票データへの参照
global.votes = global.votes || {
    JavaScript: 0,
    Python: 0,
    'C#': 0,
    Java: 0
};

app.http('getResults', {
    methods: ['GET'],
    authLevel: 'anonymous',
    handler: async (request, context) => {
        return { body: JSON.stringify(global.votes) };
    }
});