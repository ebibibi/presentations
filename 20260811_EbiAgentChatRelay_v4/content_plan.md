# Content plan

## Audience starting point

Knows:

- Claude Code or Codex can work on a local repository.
- Discord and Teams can host bots.

Does not yet know:

- Why a Teams app manifest is only one part of the deployment.
- Why the agent host should not be the public Bot Framework receiver.
- What AG-UI adds beside native CLI backends.
- Which Teams/Discord differences remain in v4.

## Slide questions and on-screen answers

1. What shipped? → v4 connects two chat frontends to four agent backends.
2. How is v4 structured? → Frontend and backend are independent axes.
3. Why is Teams setup hard? → The recommended path needs more than a Teams app package.
4. What is the key design rule? → Do not expose the agent host.
5. How does the message move? → Public receiver only verifies/enqueues; private ActivityPuller works outbound.
6. What combinations work? → Discord/Teams × Claude Code CLI/Codex CLI/local OpenAI-compatible `/v1/responses`/AG-UI HTTP/SSE.
7. What must an operator create? → Follow the eight official setup sections from the Entra app through three-stage validation.
8. Where is the real security boundary? → The entire data path, not only the tenant containing the app registration.
9. What does AG-UI mean here? → Standard HTTP/SSE events become the same internal stream.
10. What is not yet equal? → Teams text commands/file consent and advanced AG-UI features remain narrower.
11. Is it proven on real components? → 2,536 tests plus Teams→real Codex→Teams with Discord still live.
12. What should viewers do? → Read the release and setup guide, then choose the deployment boundary.

## Term introduction order

- Frontend: slide 2, the chat surface where a person talks.
- Backend: slide 2, the agent that performs the work.
- Public receiver: slide 3, the internet-reachable verifier/enqueuer.
- ActivityPuller: slide 5, the private outbound queue worker.
- AG-UI: slide 6, an HTTP/SSE backend.
- Data boundary: slide 8, every service through which content passes.

## Takahashi-style beats

- Slide 2: “2つのFrontendと4つのBackend”
- Slide 4: “Agent Hostを公開しない”
- Slide 8: “Tenant登録 ≠ Tenant内処理”
- Slide 12: “入口とAgentを、分けて選ぶ”
