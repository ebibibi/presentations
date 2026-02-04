---
marp: true
theme: gaia
paginate: true
backgroundColor: #fff
style: |
  section {
    font-family: 'Meiryo', 'Segoe UI', sans-serif;
    font-size: 32px;
    color: #333;
  }
  h1 {
    color: #4285f4;
    font-size: 1.6em;
  }
  h2 {
    color: #4285f4;
    font-size: 1.3em;
  }
  h3 {
    font-size: 1.1em;
  }
  .speaker {
    font-size: 0.85em;
    color: #666;
  }
  table {
    font-size: 0.70em;
  }
  th {
    background-color: #4285f4;
    color: white;
  }
  code {
    font-size: 0.85em;
    background-color: #e8e8e8;
    color: #333;
    padding: 2px 6px;
    border-radius: 4px;
  }
  pre code {
    padding: 12px;
    color: #f5f5f5;
  }
  li {
    font-size: 0.95em;
  }
  section.lead h1 {
    font-size: 1.8em;
  }
  section.lead h2 {
    font-size: 1.4em;
  }
  section.small {
    font-size: 28px;
  }
  section.x-small {
    font-size: 24px;
  }
  section.xx-small {
    font-size: 22px;
  }
  .highlight {
    color: #ea4335;
    font-weight: bold;
    background-color: #fff3cd;
    padding: 2px 6px;
    border-radius: 4px;
  }
  .free {
    color: #34a853;
    font-weight: bold;
  }
  .warning {
    color: #ea4335;
    font-size: 0.85em;
  }
  .url {
    font-size: 0.7em;
    color: #666;
  }
---

<!-- _class: lead -->

![bg right:25% 90%](./images/ebi-icon-circle.png)

# 【無料でスタート！】
# Gemini CLI + VS Code
## AIエージェントで開発

**2026年2月8日**
胡田昌彦 / 第1回勉強会

---

# 本日のゴール

## 環境を整えて、AIに指示してアプリを作れるようになる！

- Gemini CLI と VS Code をインストール
- AIエージェントに話しかけて開発する体験
- GEMINI.md で AIの動きをカスタマイズ

## プログラム作成以外にも結構なんでもできることを理解/体験する！

- アプリケーションを起動/操作する
- TodoistでTodoを管理する

---

# 自己紹介

## 胡田 昌彦（えびすだ まさひこ）

- Microsoft MVP（Azure, Cloud and Datacenter Management）
- YouTube: https://www.youtube.com/@ebibibi
- Web: https://ebisuda.net/

---

# なぜ今回 Gemini CLI なのか？
- 胡田は Claude Code ユーザーです…。
- Gemini CLI は **無料枠が充実** している！
  - クレジットカード不要で始められる
  - 個人開発・学習には十分な量
  - 無料で一番始めやすい！(※個人の感想です)

---

# 本日の流れ

| 時間 | 内容 |
|------|------|
| 前半（約1時間） | 環境セットアップ |
| 後半（約1時間） | Todoアプリを作ってみる + α |

- ハンズオン形式で進めます
- 見ているだけでもOK！
- 質問はTeamsチャット or YouTubeコメントで
- 📺 **YouTubeライブなので好きな時に巻き戻せます！**

---

# 必要なもの

- ✅ Windows PC
- ✅ Googleアカウント（Gemini API用）
- ✅ インターネット接続

**今日インストールするもの:**
- Visual Studio Code
- Node.js（バージョン20以上）
- Gemini CLI
- Gemini CLI Companion（VS Code拡張機能）

---

<!-- _class: lead -->

![bg right:25% 90%](./images/ebi-icon-circle.png)

# Part 1
## 環境セットアップ

---

# Step 1: VS Code のインストール

1. https://code.visualstudio.com/ にアクセス
2. 「Download for Windows」をクリック
3. ダウンロードしたインストーラーを実行
4. デフォルト設定でインストール

---

# Step 2: Node.js のインストール

1. https://nodejs.org/ にアクセス
2. **LTS版**（推奨版）をダウンロード
3. インストーラーを実行（デフォルト設定でOK）

**確認（PowerShellで）:**
```powershell
node -v
npm -v
```

※ バージョン20以上が必要

---

# Step 3: Gemini CLI のインストール

**PowerShell（管理者として実行）で:**

```powershell
npm install -g @google/gemini-cli
```

※インストール後、PATHが通らない場合:
```powershell
setx PATH "%PATH%;%AppData%\npm"
```

---

# Step 4: Gemini CLI を起動

```powershell
gemini
```

1. テーマを選択（後で変更可能）
2. 認証方法で「Login with Google」を選択
3. ブラウザが開くのでGoogleアカウントでログイン

---

# Step 5: VS Code 拡張機能のインストール

## Gemini CLI Companion

1. VS Code のサイドバー → 拡張機能
2. 「Gemini CLI Companion」を検索
3. インストール

**これで VS Code と Gemini CLI が連携！**
- 開いているファイルを認識
- 選択中のコードを理解
- 差分ビューで変更を確認

---

# Step 6: 動作確認

VS Code のターミナルで:

```powershell
gemini
```

起動したら:
```
/ide status
```

「Connected to VS Code」と表示されればOK！

---

<!-- _class: small -->

# Gemini API の無料枠

## クレジットカード不要！

| モデル | リクエスト/分 | トークン/分 | リクエスト/日 |
|--------|--------------|-------------|--------------|
| Gemini 2.5 Pro | 5 RPM | 250,000 | 100 |
| Gemini 2.5 Flash | 10 RPM | 250,000 | 250 |
| Gemini 2.5 Flash-Lite | 15 RPM | 250,000 | 1,000 |

- 個人の学習・開発には十分な量
- コンテキストウィンドウ: **100万トークン**

---

# ⚠️ プライバシーに関する注意

## 無料版（個人Googleアカウント）の場合

コードや会話データが **Googleのモデルのトレーニングに使用される可能性** があります

**機密情報を含む場合は:**
- 有料プラン（Gemini Code Assist Standard/Enterprise）

を検討してください

---

<!-- _class: lead -->

![bg right:25% 90%](./images/ebi-icon-circle.png)

# Part 2
## Todoアプリを作ってみよう

---

# AIエージェントとは？

## 「指示を出すと、自分で考えて作業してくれるAI」

- ファイルを読む・書く
- コマンドを実行する
- コードを生成・修正する
- エラーを見て自分で直す

**あなたは「何を作りたいか」を伝えるだけ**

---

# デモ①: 1発プロンプトで作る

## まずはシンプルに指示してみる

```
ローカルで動くシンプルなTodoアプリを作って。
HTMLとJavaScriptだけで動くようにして。
タスクの追加、完了、削除ができるようにして。
```

**→ AIが勝手にファイルを作ってくれる！**
**→ 起動の仕方や使い方も質問すれば教えてくれる！**

---

# YOLOモード 🚀

## 確認なしで自動実行させる

通常: ファイル作成や実行のたびに確認が必要

**YOLOモード有効化:**
- 起動時: `gemini --yolo`
- 実行中: `Ctrl + Y` で切り替え

⚠️ 便利だけど、何をしているか把握しながら使おう

---

# デモ②: ドキュメントに書いてから作らせる

## 要件を先に書いておく方法

1. `requirements.md` に要件を記述
2. `@requirements.md` で参照させる

```
@requirements.md に従ってアプリケーションを作成してください。
```

**@ コマンド**: ファイルを参照させる
**→ より正確に意図が伝わる！**

---

<!-- _class: x-small -->

# requirements.md の例

```markdown
# Todo アプリ

## 技術スタック
- HTML / CSS / JavaScript
- ローカルストレージで永続化

## 画面一覧
### タスク一覧画面
- タスクの一覧を表示
- チェックボックス、タスク名、期限日、編集・削除ボタン
- 追加ボタンで詳細画面へ遷移

### タスク詳細画面
- タスク名と期限日の入力欄
- 決定ボタンで保存、戻るボタンで一覧へ
```

---

# デモ③: 計画させてから作る

## より良い結果を得るために

```
ローカルで動くTodoアプリを作りたい。
まず計画を立てて、私に確認してから作業を始めて。

要件:
- タスクの追加、完了、削除
- ローカルストレージに保存
- シンプルなデザイン
```

**→ 計画を見てから「OK」と言う**

---

# 3つのパターンの使い分け

| パターン | 向いているケース |
|----------|------------------|
| ①1発プロンプト | 簡単なもの、試作 |
| ②ドキュメントベース | 要件が明確、再現性が必要 |
| ③計画してから | 複雑なもの、段階的に進めたい |

**慣れてきたら②③を使おう！**

---

# プログラムを作るだけじゃない！

## AIエージェントは「なんでもできる相棒」

- コマンドを実行できる → **アプリの操作もできる**
- APIを叩ける → **外部サービスとの連携もできる**
- ファイルを読み書きできる → **ドキュメント作成もできる**

**実際にやってみましょう！**

---

# デモ④: アプリケーションを操作する

## AIはコマンドを実行できる = アプリも操作できる

```
メモ帳を起動して、「Hello from Gemini!」と入力して、
デスクトップに hello.txt として保存して閉じて。
```

- PowerShellスクリプトを生成して実行してくれる
- キー送信でアプリを操作できる
- **知らない人が多いけど、スクリプトで普通にできること**

---

<!-- _class: small -->

# デモ⑤: Todoist と API 連携する

## 外部サービスのAPIも呼べる

```
Todoist に「勉強会の資料を作る」というタスクを追加して。
期限は明日にして。
```

**準備:**
1. https://todoist.com/ でアカウント作成
2. 設定 → 連携 → APIトークンを取得
3. トークンをAIに伝える

**→ タスクの追加・一覧表示・削除もAIに任せられる！**

---

# コンテキストの量を意識せよ 📊

## AIには「記憶の限界」がある

**コンテキストウィンドウ** = AIが一度に見られる情報量

- Gemini CLI: **100万トークン**（約75万文字）
- 十分大きいが、無限ではない

---

# コンテキストが増えると起きること

## 会話が長くなると…

- ⚠️ 古い指示を忘れる
- ⚠️ レスポンスが遅くなる
- ⚠️ 重要な情報が埋もれる
- ⚠️ 矛盾した回答が出やすくなる

**「なんか言うこと聞かないな…」→ コンテキスト溢れかも**

---

<!-- _class: small -->

# 対策: 定期的にリセットする

## 新しいセッションを始める

```powershell
# 一度終了して
exit

# 新しく始める
gemini
```

**目安:**
- 大きな作業が一段落したら
- AIの反応がおかしくなったら

---

<!-- _class: lead -->

![bg right:25% 90%](./images/ebi-icon-circle.png)

# Part 3
## GEMINI.md でカスタマイズ

---

# GEMINI.md とは？

## プロジェクトの「取扱説明書」をAIに渡す

プロジェクトのルートに `GEMINI.md` を置くと、
AIが自動的に読み込んで従ってくれる

```
プロジェクト/
├── GEMINI.md    ← これ！
├── index.html
└── script.js
```

---

<!-- _class: x-small -->

# GEMINI.md の例（日誌機能付き）

## これを書いて、この後の作業を続けましょう！

```markdown
# プロジェクト概要
シンプルなTodoアプリです。

# 技術スタック
- HTML / CSS / JavaScript
- ローカルストレージで永続化

# コーディング規約
- 変数名は日本語コメントで説明
- console.logは残さない

# ルール
- 回答は必ず日本語で行ってください。
- 作業が完了したら、notes/YYYY-MM-DD.md に以下の形式で追記してください:
  ## HH:MM - 作業内容 - 変更したファイル
```

**→ この後の作業で、AIが勝手に日誌を書いてくれるはず…！**

---

# GEMINI.md の階層

```
~/.gemini/GEMINI.md        ← グローバル（全プロジェクト共通）
プロジェクト/GEMINI.md     ← プロジェクト固有
プロジェクト/src/GEMINI.md ← サブディレクトリ固有
```

すべて読み込まれて結合される

---

# 便利なコマンド

| コマンド | 説明 |
|----------|------|
| `/ide status` | VS Code との接続状態を確認 |
| `/memory show` | 現在読み込まれているGEMINI.mdの内容を表示 |
| `/memory refresh` | GEMINI.mdを再読み込み |
| `/memory add <テキスト>` | グローバルGEMINI.mdに追記 |

---

<!-- _class: lead -->

![bg right:25% 90%](./images/ebi-icon-circle.png)

# Part 4
## さらに活用するなら知るべきこと(今日は知るだけ)

---

# AIエージェントの高度な機能

## 今日は入口！まだまだ奥がある

今日やったこと:
- ✅ 基本的なプロンプト
- ✅ GEMINI.md（プロジェクト設定）

**今後深掘りしていく機能:**
- Extensions（拡張機能）
- MCP（外部ツール連携）
- Hooks（自動化）
- Skills（再利用可能な技）

---

<!-- _class: small -->

# Extensions（拡張機能）

## AIの能力を拡張するパッケージ

```
gemini extension install @google/search
```

- プロンプト、MCPサーバー、スキル、コマンドをまとめたパッケージ
- チームで共有して環境を統一できる
- 公式・コミュニティ製の拡張機能が多数

**例:** データベース連携、Terraform、SonarQube など

---

# MCP（Model Context Protocol）

## AIと外部ツールをつなぐ標準規格

```json
// ~/.gemini/settings.json
{
  "mcpServers": {
    "github": { "command": "mcp-github" },
    "database": { "command": "mcp-postgres" }
  }
}
```

- GitHub、Slack、データベースなどと連携
- `@github PRを一覧表示して` のように使える
- **Claude Code と共通の規格！**

---

# Hooks（フック）

## 特定のタイミングで自動実行

```
ファイル保存時 → 自動フォーマット
コミット前 → テスト実行
```

- AIの動作の「前後」にスクリプトを挟める
- セキュリティポリシーの強制
- チームルールの自動適用

---

# Skills（スキル）

## 再利用可能な「技」を定義

```markdown
# /deploy
本番環境にデプロイする

## 手順
1. テスト実行
2. ビルド
3. サーバーにアップロード
```

- Markdownで定義するだけ
- `/deploy` と打つだけで実行
- チームで共有・再利用できる

---

<!-- _class: x-small -->

# 他のAIエージェントとの互換性

## 実は似た仕組みを持っている

| 機能 | Gemini CLI | Claude Code |
|------|------------|-------------|
| プロジェクト設定 | GEMINI.md | CLAUDE.md |
| 拡張機能 | Extensions | Plugins |
| 外部ツール連携 | MCP ✅ | MCP ✅ |
| フック | Hooks | Hooks |
| スキル | Skills | Skills |

**MCP は共通規格** → 同じサーバーが使える！

---

# AGENTS.md: 共通標準の動き

## 複数のAIエージェントで共通の設定ファイル

```
プロジェクト/
├── AGENTS.md    ← どのAIでも読める！
├── GEMINI.md    ← (シンボリックリンク)
└── CLAUDE.md    ← (シンボリックリンク)
```

- Gemini CLI、Claude Code、Codex、Cursor、GitHub Copilot…
- 1つのファイルで複数のAIに指示できる未来
- https://agents.md/ で標準化が進行中

---

<!-- _class: small -->

# AIエージェントの選択肢

| ツール | 特徴 |
|--------|------|
| **Gemini CLI** | 無料枠が充実、オープンソース、100万トークン |
| **Claude Code** | 高い推論能力、エンタープライズ向け機能 |
| **Codex CLI** | OpenAI製、シンプル |
| **Cursor** | IDE統合型、UIが使いやすい |
| **GitHub Copilot** | GitHub連携が強力 |

**→ あなたのお好みは？**

---

# 日誌、見てみましょう

## さっき設定した日誌、書かれているかな？

```
notes/ フォルダを開いてみてください
```

- AIが作業するたびに、勝手に日誌ファイルを作って追記してくれているはず
- **GEMINI.md に設定を書いておくだけで、AIが自律的に動いてくれる**
- これが GEMINI.md の力！

---

<!-- _class: lead -->

![bg right:25% 90%](./images/ebi-icon-circle.png)

# まとめ

---

# 今日やったこと

1. ✅ VS Code + Node.js + Gemini CLI をインストール
2. ✅ Gemini CLI Companion で VS Code と連携
3. ✅ AIエージェントにTodoアプリを作らせた
   - 1発プロンプト / ドキュメントベース / 計画してから
4. ✅ YOLOモードで自動実行
5. ✅ アプリ操作・API連携もできることを体験
6. ✅ GEMINI.md でAIをカスタマイズ（日誌も自動で！）

---

# 次のステップ

- 自分の作りたいものをAIに作らせてみる
- 自分のやりたいことをどうやったらできるか、AIに聞いてみる
- requirements.md を書いて再現性を高める
- GEMINI.md を育てて、自分好みのAIに

---

# ターミナルが「考える相棒」になる

## 今日体験したこと以外にも…

- 🗓️ **旅行計画**: 「ソウル3泊4日、雨の日プランも」
- 📝 **文章の推敲**: メール、ブログ、ドキュメント
- 🤔 **設計の壁打ち**: 「この構成どう思う？」
- 📰 **情報収集**: ニュース要約、リサーチ
- 📋 **1日の振り返り**: 日報作成、タスク整理

**思いついたら、まずAIに聞いてみよう**

<span class="url">参考: https://dev.classmethod.jp/articles/claude-code-daily-workflow/</span>

---

<!-- _class: xx-small -->

# 参考リンク

## 公式ドキュメント
- Gemini CLI GitHub: https://github.com/google-gemini/gemini-cli
- Gemini CLI Docs: https://geminicli.com/
- GEMINI.md: https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html
- Gemini API Rate Limits: https://ai.google.dev/gemini-api/docs/rate-limits

## 拡張機能・高度な機能
- Extensions: https://geminicli.com/extensions/
- Hooks: https://developers.googleblog.com/tailor-gemini-cli-to-your-workflow-with-hooks/
- AGENTS.md（共通標準）: https://agents.md/

---

<!-- _class: xx-small -->

# 参考リンク（続き）

## 比較・解説記事
- Gemini CLI vs Claude Code: https://composio.dev/blog/gemini-cli-vs-claude-code-the-better-coding-agent
- Claude Code Plugins vs Gemini CLI Extensions: https://harishgarg.com/claude-code-plugins-vs-gemini-cli-extensions-a-comparison

## インストール
- VS Code: https://code.visualstudio.com/
- Node.js: https://nodejs.org/

---

# 実は…このスライドも

## 全部 Claude Code に書いてもらいました

- スライドの構成・文章・コード例
- 修正や順番の入れ替えも全部AIに指示
- 人間がやったのは「こういうスライドにして」と伝えることだけ

**AIエージェント、本当になんでもできる時代です**

---

<!-- _class: lead -->

![bg right:25% 90%](./images/ebi-icon-circle.png)

# ありがとうございました！

## 質問・感想はお気軽に

YouTube: https://www.youtube.com/@ebibibi
チャンネル登録お願いします！

