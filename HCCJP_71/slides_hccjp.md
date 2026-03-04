---
marp: true
theme: gaia
paginate: true
backgroundColor: #fff
style: |
  section {
    font-family: 'Meiryo', 'Segoe UI', sans-serif;
    font-size: 36px;
  }
  h1 {
    color: #0078d4;
    font-size: 1.8em;
  }
  h2 {
    color: #0078d4;
    font-size: 1.5em;
  }
  .speaker {
    font-size: 0.85em;
    color: #666;
  }
  table {
    font-size: 0.75em;
  }
  th {
    background-color: #0078d4;
    color: white;
  }
  code {
    font-size: 0.9em;
  }
  li {
    font-size: 0.95em;
  }
  section.small {
    font-size: 28px;
  }
  section.small h1 {
    font-size: 1.3em;
  }
  section.small h2 {
    font-size: 1.1em;
  }
  section.small code {
    font-size: 0.85em;
  }
  section.x-small {
    font-size: 24px;
  }
  section.x-small h1 {
    font-size: 1.2em;
  }
  section.x-small h2 {
    font-size: 1.0em;
  }
  section.x-small code {
    font-size: 0.6em;
  }
  section.x-small li {
    font-size: 0.9em;
  }
  section.lead h1 {
    font-size: 2.0em;
  }
  section.lead h2 {
    font-size: 1.3em;
  }
  section.lead .speaker {
    font-size: 1.0em;
  }
  section.point {
    font-size: 42px;
  }
  section.point h1 {
    font-size: 1.6em;
  }
  section.point h2 {
    font-size: 1.3em;
    color: #333;
  }
  .arch-box {
    font-family: 'MS Gothic', monospace;
    font-size: 0.7em;
    line-height: 1.3;
    background: #f8f8f8;
    padding: 15px;
    border-radius: 8px;
  }
  .arch-box pre, .arch-box code {
    font-family: 'MS Gothic', monospace !important;
  }
---

<!-- _class: lead -->

![bg right:30% 80%](../Images/hcc-logo02f.png)

# HCCJP 第71回勉強会

## ハイブリッドクラウド研究会

**2026年3月13日（金）14:00開始**

---

<!-- _class: lead -->

# AI時代の
# 「本当の」ハイブリッドクラウド

## エージェントが実現した、あの頃の夢

---

<!-- _class: lead -->

![bg right:30% 80%](../Images/hcc-logo02f.png)

# オープニング

**司会：胡田 昌彦**
<span class="speaker">日本ビジネスシステムズ株式会社<br>Microsoft MVP for Cloud and Datacenter Management, Microsoft Azure</span>

---

<!-- _class: small -->

# タイムテーブル

| 時刻 | 内容 | スピーカー |
|------|------|------------|
| 14:00 (5分) | オープニング | 胡田 昌彦（JBS / MVP） |
| 14:05 (40分) | AI時代の「本当の」ハイブリッドクラウド | 胡田 昌彦 |
| 14:45 (10分) | Q&A | 全員 |
| 14:55 (20分) | Microsoft "Adaptive Cloud" 最新動向 | 高添 修 氏（日本マイクロソフト） |
| 15:15 (10分) | Q&A | 高添 修 氏 |
| 15:25 (5分) | クロージング | 胡田 昌彦 |

---

<!-- _class: small -->

![bg right:20% 60%](../Images/hcc-logo02f.png)

# HCCJPとは

## ハイブリッドクラウド研究会

- 毎月第2金曜日 14時から開催
- Azure + ハイブリッドクラウド関連の最新情報
- オンライン配信（YouTube HCCJPチャンネル）

📺チャンネル登録お願いします！

---

# 本日の注意事項

- 📹 配信は録画されています（アーカイブ視聴可）
- 💬 質問・コメント大歓迎！
- 📝 Q&Aセッションでまとめてお答えします

---

# 質問・コメント方法

## 💬 YouTubeチャットで質問・コメント大歓迎！

- 右側のライブチャット欄から投稿してください
- セッション中でもお気軽にどうぞ
- 固定コメントに各種リンクを掲載します

---

<!-- _class: lead -->

# セッション①

## AI時代の「本当の」ハイブリッドクラウド
## エージェントが実現した、あの頃の夢

**胡田 昌彦**

⏱️ 14:05 - 14:45（40分）

---

<!-- _class: x-small -->

# 👨‍💻 自己紹介

## 胡田 昌彦（えびすだ まさひこ）

- 🏢 **日本ビジネスシステムズ株式会社（JBS）**
- 🏆 **Microsoft MVP** — Cloud and Datacenter Management / Microsoft Azure
- 📖 著書: **「Windowsインフラ管理者入門」**
- 📺 YouTube: https://youtube.com/@ebibibi
- 🌐 Web: https://ebisuda.net/
- 🎵 趣味: ベース、ドラム、セッション、将棋

---

<!-- _class: point -->

# 問いかけ

## 「ハイブリッドクラウド」「マルチクラウド」

## 本当に実現してましたか？

---

# 2018年〜 HCCJPの頃

- 「ハイブリッドクラウド」は**ホットワード**だった
- Azure Stack、AWS Outposts、Google Anthos…
- 各ベンダーが「ハイブリッドこそ未来」と言っていた

**でも…**

---

<!-- _class: point -->

# 正直なところ

- 1つのシステムは**1箇所にまとまって動く**のが普通
- オンプレはオンプレ、クラウドはクラウド
- 「ハイブリッド」はネットワーク接続がメイン
- ワークロードの分散ではなかった

→ **本当にハイブリッドに跨って動くシステムは少なかった**

---

<!-- _class: point -->

# 2025-2026年、AIエージェントの時代

- コーディングエージェント
  （Claude Code, Cursor, GitHub Copilot, Windsurf, Devin 2.0, Replit Agent…）
- 自律的にタスクを遂行するAI
- **1つのエージェントが、複数の場所を跨いで動く**

→ これ、**本当のハイブリッドクラウド**じゃない？

---

<!-- _class: lead -->

# 3つの軸で整理する

---

# AIエージェント時代のハイブリッドを整理する

| 軸 | 問い |
|----|------|
| **1. 実行環境** | エージェントを**どこで**動かすか？ |
| **2. コンテキスト** | 情報を**どこに**持つか？ |
| **3. モデル** | **どのAI**で推論するか？ |

この3軸の組み合わせで、無数のパターンが生まれる

---

<!-- _class: small -->

# 3軸でツールを分類してみる

| ツール | 実行環境 | コンテキスト | モデル |
|--------|---------|-------------|--------|
| Claude Code | ローカル | ローカル+クラウドAPI | Anthropic |
| Claude on Web | クラウド | クラウド | Anthropic |
| Cursor / Windsurf | ローカル | ローカル | マルチ選択可 |
| GitHub Copilot CLI | ローカル | ローカル+GitHub | マルチ選択可 |
| Copilot Coding Agent | クラウド | GitHub | マルチ選択可 |
| Devin 2.0 | クラウド | クラウド | マルチ |

**全部バラバラ。これが現実のマルチクラウド。**

---

<!-- _class: lead -->

# 具体例で見てみよう

---

# 例1: 私の環境（Claude Code）

<div class="arch-box">

```
+-------------------+          +------------------------+
|    ローカル       |          |       クラウド         |
|                   |          |                        |
| +---------------+ |          | Anthropic API (推論)   |
| | Obsidian      | |   API    | Todoist API            |
| | CLAUDE.md     |<|--------->| Google Calendar API    |
| | ソースコード  | |          | GitHub                 |
| | skills/       | |          | Azure                  |
| +---------------+ |          | Discord API            |
|        |          |          +------------------------+
|   Claude Code     |
|  (エージェント)   |
+-------------------+
```
</div>

→ **ハイブリッド（ローカル + マルチクラウド）**

---

# 例2: GitHub Copilot CLI

<div class="arch-box">

```
+-------------------+          +------------------------+
|    ローカル       |          |    GitHub (クラウド)   |
|                   |          |                        |
| +---------------+ |          | Repository             |
| | ソースコード  | |   API    | Issues / Discussions   |
| | copilot-      |<|--------->| Copilot Spaces         |
| | instructions  | |          +------------------------+
| +---------------+ |          | モデル選択             |
|        |          |          |  GPT-4o / Claude /     |
|   Copilot CLI     |          |  Gemini                |
|  (エージェント)   |          +------------------------+
+-------------------+
```
</div>

→ **マルチクラウド × ハイブリッド**

---

<!-- _class: point -->

# 例3: Claude Code のセッション引き継ぎ

| | Remote Control | Cloud on the Web |
|--|---|---|
| 実行場所 | **ローカルPC** | AnthropicクラウドVM |
| 移動するもの | メッセージのみ | 会話履歴＋ブランチ |
| ローカルファイル | ✅ アクセス可 | ❌ GitHub経由のみ |
| 並列実行 | ❌ 1セッション1接続 | ✅ 何タスクでも |

**共通点: VMを引っ越すより圧倒的に軽い**
→ これが「本当のハイブリッド」を可能にする

---

<!-- _class: point -->

# 例4: 複数エージェントで同じ知識を共有

```
CLAUDE.md
  ├── symlink → AGENTS.md (Codex CLI)
  └── symlink → GEMINI.md (Gemini CLI)
```

- Claude Code / Gemini CLI / Codex CLI が
  **同じ設定ファイル**を読む
- どのエージェントでも同じルールで動く

→ **マルチエージェント × 共有コンテキスト**

---

<!-- _class: lead -->

# なぜ今「本当のハイブリッド」なのか

---

<!-- _class: small -->

# 昔と今の決定的な違い

| | VM時代 | AIエージェント時代 |
|--|--------|-----------------|
| 移動対象 | VM（数十GB〜） | 会話・設定ファイル（数KB〜MB） |
| 移動コスト | 高い（ダウンタイム） | ほぼゼロ |
| 構成の自由度 | ベンダーロックイン | ツール・モデル・場所を自由選択 |
| 標準化 | 各社独自 | MCP, OpenAI互換API等 |

**モビリティが圧倒的に高いから、ハイブリッドが「自然に」実現する**

---

# 標準化の波

- **MCP** — コンテキスト接続の標準化
- **OpenAI互換API** — 異なるプロバイダーを同じIFで
- **CLAUDE.md / copilot-instructions.md** — エージェント設定のファイル化
- **Skills / Custom Instructions** — 再利用可能な知識パッケージ

標準化 = ポータビリティ = ハイブリッド/マルチクラウドの基盤

---

<!-- _class: lead -->

# AIエージェントの動力源 = API

---

<!-- _class: small -->

# エージェントが仕事をする仕組み

## 外部サービスへのアクセス = すべてAPI経由

| 操作 | 手段 |
|------|------|
| ファイル読み書き | OS API（ローカル） |
| Git操作 | コマンド / GitHub API |
| タスク管理 | Todoist REST API |
| カレンダー | Google Calendar API |
| クラウドリソース | Azure Resource Manager API |

**APIがない場所 = エージェントが「触れない場所」**

---

<!-- _class: small -->

# 💬 Kelsey Hightower（Google / Kubernetes）

## "No one wants to manage infrastructure.<br>They want to consume it via API."

- Kubernetes の生みの親の一人
- 「インフラはAPIで消費するもの」という思想を一貫して主張

> この哲学がそのままAIエージェント時代の答えになっている

**インフラをAPIで整えることの意味が、初めて全員に伝わる時代**

---

<!-- _class: small -->

# クラウドとオンプレを同じAPIで（Azure Arc）

<div class="arch-box">

```
AIエージェント（Claude Code / Cursor / Copilot...）
              ↓ 同じ API
┌─────────────────────────────────────┐
│       Azure Resource Manager        │
├──────────────────┬──────────────────┤
│   Azure (クラウド) │   オンプレミス    │
│   - VMs          │   - Azure Local  │
│   - AKS          │   - Arc Servers  │
│   - Databases    │   - AKS Arc      │
│   - Functions    │   - Arc Data Svc │
└──────────────────┴──────────────────┘
```
</div>

**エージェントは場所を気にしない。APIがあるかどうかだけを気にする。**

---

<!-- _class: point -->

# これが「本当のハイブリッドクラウド」

## エージェントが縦横無尽に動ける環境

---

<!-- _class: lead -->

# これからの考え方

---

<!-- _class: small -->

# AI エージェントの4層モデル

```
┌─────────────────────────────────────────────────┐
│ 📜 コンテキスト（魂）                            │ ← 自分で作る・育てる
│    CLAUDE.md / skills / rules / MCP設定          │   （組織の競争優位）
├─────────────────────────────────────────────────┤
│ 🤖 エージェントSW                                │ ← 選ぶ・使う
│    Claude Code / Copilot / Codex / Gemini CLI    │   （現時点はClaude Codeが頭1つ抜けている）
├─────────────────────────────────────────────────┤
│ 🧠 頭脳（モデル）                                │ ← 借りる・差し替える
│    Claude / GPT-4o / DeepSeek / OSS LLM          │   （最強を選ぶ）
├─────────────────────────────────────────────────┤
│ 🏃 実行環境（肉体）                              │ ← インフラとして整備
│    ローカル / クラウドVM / エッジ                │   （APIがあれば何でもいい）
└─────────────────────────────────────────────────┘
```

---

<!-- _class: point -->

# 組織が向かうべき方向

## マルチモデル × マルチクラウド × エージェントガバナンス

- 🧠 **頭脳**: その時々の最強・最コスパに自由に切り替え
- 🏃 **実行環境**: ローカル・クラウドどこでも動く
- 📜 **コンテキスト**: 自分たちが育てた資産として保持
- 🛡️ **ガバナンス**: デバイスではなく、**エージェントの行動**で制御

この4つを同時に実現した組織が、
**圧倒的な生産性で次の時代を作る**

---

# まとめ

1. 昔の「ハイブリッドクラウド」は**理想だけど現実味が薄かった**
2. AIエージェントの登場で**本当にハイブリッドが当たり前に**
3. **3軸**（実行環境・コンテキスト・モデル）で整理できる
4. **4層モデル**（コンテキスト・エージェントSW・モデル・実行環境）で企業の注力点が見えてくる
5. 本当のハイブリッドを生かすには**APIと行動ベースのガバナンス**が鍵

---

<!-- _class: x-small -->

# 参考・引用リソース

| 内容 | 出典 |
|------|------|
| Kubernetes = "platform for building platforms" / API as infrastructure | Kelsey Hightower (Google) |
| Agentic AI × マルチクラウド × マルチモデルの3軸アーキテクチャ | [Equinix Blog (2025/03)](https://blog.equinix.com/blog/2025/03/19/how-to-do-agentic-ai-inference-in-a-multicloud-multi-model-world/) |
| AI Agentsが動くためのインフラ要件を体系化した論文 | [arXiv 2501.10114 "Infrastructure for AI Agents"](https://arxiv.org/html/2501.10114v2) |
| 実際にマルチクラウドを跨ぐAIエージェントを構築した開発者の記録 | [InfoWorld (2025)](https://www.infoworld.com/article/3959533/i-built-an-agentic-ai-system-across-multiple-public-cloud-providers.html) |
| Gartner 2026 I&O Top Trends — Hybrid Computing × Agentic AI | [Gartner (2025/12)](https://www.gartner.com/en/newsroom/press-releases/2025-12-11-gartner-identifies-the-top-trends-impacting-infrastructure-and-operations-for-2026) |

---

<!-- _class: lead -->

# Q&A

## 💬 質問にお答えします！

- どんな質問でも大歓迎です

⏱️ 14:45 - 14:55（10分）

---

<!-- _class: lead -->

![bg right:30% 80%](../Images/hcc-logo02f.png)

# セッション②

## Microsoft "Adaptive Cloud" 最新動向

**高添 修 氏**
<span class="speaker">日本マイクロソフト株式会社</span>

⏱️ 14:55 - 15:15（20分）

---

<!-- _class: lead -->

# Q&A

## 💬 質問にお答えします！

⏱️ 15:15 - 15:25（10分）

---

<!-- _class: lead -->

![bg left:28% 82%](../Images/hcc-logo02f.png)

# クロージング

## 本日のご参加ありがとうございました！

- アーカイブはYouTubeチャンネルから視聴可能
- 資料は後日公開予定
- ハッシュタグは **#HCCJP**

---

![bg right:30% 90%](../Images/hcc-logo02f.png)

# 📺 チャンネル登録を！

## 目指せ 1000人！

**YouTube HCCJPチャンネル**

毎月第2金曜日の最新情報をお見逃しなく！

---

<!-- _class: lead -->

# 次回予告

## 📅 2026/4/10（金）14:00〜

次回の内容は調整中です！
希望あればコメントで！

最新情報は YouTube・X でお知らせ！

---

<!-- _class: lead -->

![bg left:28% 82%](../Images/hcc-logo02f.png)

# ご参加ありがとうございました！

## また次回お会いしましょう！
