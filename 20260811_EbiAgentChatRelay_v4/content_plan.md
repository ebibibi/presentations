# Content plan — non-technical value story

## Audience starting point

Knows:

- Claude Code and Codex are AI tools that can do development work.
- Discord and Microsoft Teams are chat applications.

Does not need to know:

- Azure Bot, Storage Queue, ActivityPuller, SSE, or internal contracts.
- The implementation details of frontend and backend abstractions.

## One-sentence promise

Ebi Agent Chat Relay lets people use their existing Claude and ChatGPT subscriptions from the chat app they already use, while choosing Claude Code or Codex for each job.

## Slide questions and on-screen answers

1. What is this? → A relay from everyday chat to AI agents.
2. What did we build? → Ask Claude Code or Codex to work from Discord or Teams.
3. Why use the CLI subscriptions? → Reuse monthly Claude/ChatGPT plans; frequent use can be more economical than direct pay-per-use API billing.
4. Can I change AI midway? → On Discord, switch Claude Code and Codex while handing the text conversation across automatically.
5. Why have two AIs? → Use either one per task, and keep both available.
6. Where can I talk to it? → Choose Discord for personal/community use or Teams for organizational use.
7. What can I do from chat? → Request work, run parallel sessions, answer prompts, and receive results.
8. Does Teams really work? → A real Teams message reached a real Codex session and returned to Teams while Discord stayed online.
9. Is Teams setup instant? → It needs Microsoft 365/Azure administrator setup once; users then talk from Teams normally.
10. What changed in v4? → Monthly AI plans, selectable AI, and selectable chat entrance are now one product.

## Term introduction order

- AI agent: slide 1, an AI that can inspect files and carry out work.
- Relay: slide 2, the bridge between chat and the selected AI.
- Backend: avoided on the main slides; described as “which AI does the work.”
- API: slide 3, only as the alternative pay-per-use path.

## Takahashi-style beats

- Slide 2: “チャットから、AIに仕事を頼む”
- Slide 3: “月額プランを活かす”
- Slide 4: “会話の途中で、AIを交代”
- Slide 10: “選べるAI。選べるチャット。”

## Visual rule

- Dark navy background, white text, Microsoft-like blue as the single primary accent.
- Orange is used only for the monthly-subscription highlight and final call to action.
- No rainbow coding by component; the story is about user value, not system topology.
