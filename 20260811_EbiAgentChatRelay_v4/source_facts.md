# Source facts — Ebi Agent Chat Relay v4.0.0

Primary source: https://github.com/ebibibi/ebi-agent-chat-relay/releases/tag/v4.0.0

- v4.0.0 was published on 2026-08-11.
- Frontends: Discord and Microsoft Teams.
- Backends: Claude Code CLI, OpenAI Codex CLI, local OpenAI-compatible `/v1/responses`, AG-UI HTTP/SSE.
- The official CLIs can use existing subscriptions: Claude Code with Claude Pro/Max and Codex with ChatGPT Plus/Pro/Business. Direct API execution is not required for those two backends.
- Discord supports `/backend` switching and per-thread overrides. When a live thread switches between Claude and Codex, the relay creates a bounded text-only handoff from the previous CLI transcript; no manual summary or copy/paste is required.
- Multiple Discord threads can run independent AI sessions in parallel, including a mix of Claude Code and Codex across threads.
- Discord messages create or continue a persistent thread-bound AI session, so users can send follow-up instructions in the same conversation.
- All four backends are supported from both frontends.
- The recommended Teams path is Teams/Bot Framework → public receiver → Azure Storage Queue → private ActivityPuller → selected backend → Bot Connector → Teams.
- The public receiver verifies inbound identity and enqueues a bounded envelope. It has no bot client secret, repository access, or agent credentials and cannot run an agent.
- The private host polls outbound. It does not expose a Teams listener.
- `CCDB_FRONTENDS=discord,teams` runs Discord and the private ActivityPuller in one process. Omitting it keeps Discord-only behavior.
- Discord can persist per-conversation backend overrides. The normal Teams private queue path uses the configured/global backend.
- The normal Teams private queue path does not yet dispatch text commands such as `/backend` and does not bridge file-consent invokes.
- The official Teams setup guide defines eight setup sections: Entra application, Azure Bot, Azure Storage Queue, public receiver, private session host, Teams app package, upload/consent, and three-stage validation.
- AG-UI maps run lifecycle, text, reasoning, tool call, and tool result events into the common stream.
- AG-UI rejects URL credentials and redirects, bounds SSE frames, and strips its token from child CLI environments.
- Durable HITL resume, state/activity, protobuf, and client tools are not presented as supported AG-UI features.
- A customer-tenant Entra application alone does not guarantee that data remains in that tenant. The data path also includes Bot Framework, receiver, queue, private host, and backend.
- Compatibility retained: `ccdb`, `CCDB_*`, Python package/import, REST routes, and stored data.
- PyPI distribution is not published yet; install from the GitHub tag or tagged Git URL.
- Validation: 2,536 local tests, ruff, pyright with zero errors, Python 3.12/3.13 CI, CodeQL, merge-after CI, and translation workflow succeeded.
- Production verification before the release: Discord and Teams ran together; a Teams personal-chat request travelled through Azure relay to a real Codex backend and returned to Teams.
- The repository is licensed under the MIT License.
- This presentation is the YouTube promotion deck for v4.0.0 and is paired with a note article that explains its design and Teams setup.

Supporting sources:

- https://github.com/ebibibi/ebi-agent-chat-relay/blob/v4.0.0/README.md
- https://github.com/ebibibi/ebi-agent-chat-relay/blob/v4.0.0/docs/teams-setup.md
- https://github.com/ebibibi/ebi-agent-chat-relay/blob/v4.0.0/docs/backends.md
- https://github.com/ebibibi/ebi-agent-chat-relay/blob/v4.0.0/docs/ARCHITECTURE.md
- https://github.com/ebibibi/ebi-agent-chat-relay/blob/v4.0.0/docs/agui-backend.md
