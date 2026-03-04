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

<!-- _class: lead -->

# Part 1
# HCCJPの原点と「あの頃の夢」

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
- 「ハイブリッド」はネットワーク接続がメイン。管理コンソールの統合...までもなかなか行けなかった
- ワークロードの分散ではなかった

→ **本当にハイブリッドに跨って動くシステムは少なかった**

---

<!-- _class: lead -->

# Part 2
# 時代は変わった

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

# Part 3
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

# 軸1: エージェント実行環境

## どこで動かすか？

| パターン | 例 |
|---------|------|
| ローカル実行 | Claude Code、Cursor、Windsurf |
| クラウド実行 | GitHub Copilot Coding Agent、Devin 2.0、Replit Agent |
| ハイブリッド | ローカル ↔ クラウド切り替え |

- Claude Code: ローカルで作業 → Claude on the Web でセッション引き継ぎ
- GitHub Copilot: CLI（ローカル）と Coding Agent（クラウド）を同じエコシステムで使い分け
- Cursor / Windsurf: ローカルIDEから複数モデル（Claude / GPT-4o / Gemini）を切り替え
- **同じ目的のエージェントなのに、実行場所もモデルも選べる**

---

<!-- _class: small -->

# 軸2: コンテキストの置き場所

## 情報をどこに持つか？

| パターン | 例 |
|---------|------|
| ローカル | Obsidian Vault、CLAUDE.md |
| クラウド | GitHub Issues / Discussions / Copilot Spaces |
| ハイブリッド | ローカルファイル + クラウドAPI |

- Claude Code: ローカル（Obsidian）にコンテキスト集約 + クラウドAPI
- Copilot CLI: GitHub上にスペースを作りコンテキストを持たせる
- **異なるエージェントでも同じコンテキストを共有できる**

---

<!-- _class: small -->

# 軸3: モデルの選択

## どのAIで推論するか？

| パターン | 例 |
|---------|------|
| 単一プロバイダー | Claude Code → Anthropic API |
| マルチプロバイダー | Copilot CLI → GPT-4o / Claude / Gemini |
| セルフホスト | Azure AI Foundry にデプロイしたモデル |
| オンデバイス | Apple Intelligence、Ollama |

- Copilot CLIはモデルを**複数切り替えられる** → マルチクラウド
- Azure AI Foundry なら自分の管理下でモデルを動かせる
- ローカルLLM + クラウドLLM の使い分けも

---

<!-- _class: lead -->

# Part 4
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

# 例3: セッション引き継ぎ

## シームレスなハイブリッド

**自宅** → **外出先**

ローカル（Claude Code）で作業開始
→ 移動中にClaude on the Webに引き継ぎ

- VMのライブマイグレーション？
  いいえ、**会話の引き継ぎ**です
- データが軽いから簡単にできる

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
| Replit Agent | クラウド | クラウド | マルチ |
| Ollama / LM Studio | ローカル | ローカル | オンデバイス |

**全部バラバラ。これが現実のマルチクラウド。**

---

<!-- _class: lead -->

# Part 5
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

<!-- _class: point -->

# 人の数だけ構成がある

- Aさん: Claude Code + Obsidian + Azure
- Bさん: Copilot CLI + GitHub + AWS
- Cさん: Cursor + Notion + GCP
- Dさん: ローカルLLM + VS Code + オンプレ

**同じ「AIでコーディング」でも構成は十人十色**
**これ自体がマルチクラウドの証拠**

---

<!-- _class: lead -->

# 🧠 頭の体操タイム

---

# あなたの環境を整理してみよう

## 3つの軸で考えてみてください

1. **実行環境**: エージェントはどこで動いている？
2. **コンテキスト**: 情報はどこにある？
3. **モデル**: どのAIを使っている？

→ きっと、**あなたも既にハイブリッドクラウドを使っている**

---

<!-- _class: lead -->

# Part 6
# AIエージェントの動力源 = API

---

<!-- _class: point -->

# AIエージェントは
# APIがなければ
# 手も足も出ない

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

<!-- _class: point -->

# クラウドはAPIが当たり前

- Azure: Resource Manager API、Storage API、Kubernetes API…
- AWS / GCP: 全リソースがREST API経由
- **エージェントにとってクラウドは「天国」**
  - 作れる・消せる・設定できる → すべてAPIで自在に

---

<!-- _class: point -->

# オンプレミスは？
## APIが限定的だった

- 昔のシステム: GUIや独自プロトコルが中心
- 管理: 専用コンソールを人間が直接操作
- 自動化: スクリプト職人が個別に対応

**「手作業で困っていない」が通用した時代**

---

<!-- _class: small -->

# AIエージェントの目線で見ると

| 環境 | APIの充実度 | エージェントの働ける範囲 |
|------|------------|----------------------|
| クラウド | ◎ 全操作がAPI化 | 自在に仕事できる |
| API整備済みオンプレ | ○ | かなり仕事できる |
| 従来型オンプレ | △〜× | 手を出せる範囲が限定的 |

**インフラのAPI化 = エージェントへの「権限委譲」**

---

<!-- _class: small -->

# オンプレにAPIが整うと変わること

## Azure Arcで実現する世界

- **Azure Local** → オンプレのインフラをAzure APIで操作
- **Arc-enabled Servers** → 普通のサーバーもAzure Resource Managerで管理
- **AKS Arc** → オンプレのKubernetesもAzure APIで統合管理
- **Arc-enabled Data Services** → DBもAzure APIで運用

→ エージェントから見ると「クラウドとオンプレの差がなくなる」

---

<!-- _class: lead -->

# Azure Arc =
# AIエージェントにとって
# 最高の環境

---

<!-- _class: small -->

# クラウドとオンプレを同じAPIで

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

<!-- _class: small -->

# 「セルフサービス化・クラウドネイティブ化」の真の意味

| 時代 | 理解されにくかった理由 | AIエージェント時代の説明 |
|------|------------------|----------------------|
| 従来 | 「手作業で困ってません」 | ✗ 刺さらない |
| AI時代 | 「APIがないとエージェントが使えません」 | ✓ 即わかる |

**インフラを整えることの意味が、初めて全員に伝わる時代**

---

<!-- _class: lead -->

# Part 7
# これからのインフラ設計

---

# AIエージェント前提で考えると

- **コンテキストの設計**が最重要
  （どこに何を持たせるか）
- **モデル選択の柔軟性**を担保する
  （ベンダーロックイン回避）
- **実行場所を固定しない**
  （ローカル / クラウド / ハイブリッド）
- **セキュリティ境界**の再定義
  （エージェントがAPIを叩く世界のガバナンス）

---

# まとめ

1. 昔の「ハイブリッドクラウド」は**理想だけど現実味が薄かった**
2. AIエージェントの登場で**本当にハイブリッドが当たり前に**
3. **3つの軸**（実行環境・コンテキスト・モデル）で整理
4. **モビリティの高さ**と**標準化**が鍵
5. 人の数だけ構成がある — **可能性は無限大**

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

<!-- _class: small -->

# 🙌 HCCJPを一緒に盛り上げませんか？

HCCJPは**企業・個人を問わず、誰でも参加できるオープンなコミュニティ**です。

今、特に**こんな仲間**を募集しています！

- 🏢 **ユーザー企業の担当者** — 「うちはこう使ってる」というリアルな導入事例の共有
- 💬 **構成相談したい方** — 「こういう構成どう？」をみんなで議論しましょう
- 🤖 **生成AI × インフラに興味がある方** — AI活用事例を持ち寄りましょう
- 🎤 **登壇してみたい方** — 初登壇も大歓迎！発表の場を提供します

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
