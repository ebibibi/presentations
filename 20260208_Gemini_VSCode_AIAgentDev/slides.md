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
| 後半（約1時間） | Todoアプリを作ってみる<br>アプリケーション操作<br>API連携<br>などなど！ |

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

**JavaScriptの実行エンジン。Gemini CLI の動作に必要。**

1. https://nodejs.org/ にアクセス
2. Windows用のインストーラー（.msi）をダウンロード
3. インストーラーを実行（デフォルト設定でOK）

**確認（PowerShellで）:**
```powershell
node -v
npm -v
```

---

# ⚠️ npm でエラーが出たら

## 「スクリプトの実行が無効になっています」

PowerShellを **管理者として実行** して:

```powershell
Set-ExecutionPolicy RemoteSigned
```

「Y」で許可 → もう一度 `npm -v` を確認

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

1. 認証方法で「Login with Google」を選択
2. ブラウザが開くのでGoogleアカウントでログイン
3. rを押してリスタート

---

# Step 5: VS Code 拡張機能のインストール

## VS Code のターミナルで gemini を起動するだけ！

```powershell
gemini
```

「Do you want to connect VS Code to Gemini CLI?」と聞かれるので **Yes** を選択

→ 自動で **Gemini CLI Companion** がインストールされる！

---

# Step 6: 動作確認

起動したら:
```
/ide status
```

「Connected to VS Code」と表示されればOK！

---

<!-- _class: lead -->

# 🎉 環境セットアップ完了！

## おめでとうございます！

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

# 日本語で使おう 🇯🇵

## 英語で返ってきましたね… 毎回言うのは面倒！

AIに GEMINI.md を作らせよう:

```
GEMINI.md を作成して。
日本語で考えて、日本語で回答するように指示を書いて。
```

→ **設定ファイルの作成もAIに任せる！**

💡 GEMINI.md = プロジェクトのルールブック（後で詳しく紹介）

---

# 💡 今日一番大事なこと

## あなたがやらなくていい。AIにやらせる。

AIが「手動で開いてください」と言ってきても…

```
開いてください。
```

→ **AIがコマンドを実行して開いてくれる！**

せっかくAIエージェントを使うのだから、**人間は指示するだけ**

---

<!-- _class: small -->

# 💡 今日一番大事なこと（続き）

## AIエージェント時代の考え方

- PCの操作は**ほとんどコマンドで自動化できる**
- GUIで手作業していたことも、AIがコマンドで実行してくれる
- 何が自動化できるか知らなくてもいい

## じゃあどうするか？

- **AIが全部できると信じて、まず「やって」とお願いする**
- 仕事で「こうしてください」と言われたら、そのままAIに頼む
- これだけで生産性が劇的に変わる

## 今日はこれだけ覚えて帰ってもOKです！

---

# YOLOモード 🚀

## 確認なしで自動実行させる

**YOLOモード有効化:**
- 起動時: `gemini --yolo`
- 実行中: `Ctrl + Y` で切り替え

⚠️ 超便利だけど、最悪環境自体も壊す危険性あり！

**YOLO** = "You Only Live Once"（人生一度きり、やっちゃえ！）
日本語的には「よろ〜（よろしく〜）」と覚えると覚えやすいかも？（笑）

---

# お片付けもAIに任せる 🧹

## 次のデモの前に、さっき作ったファイルを削除

```
GEMINI.md 以外の全ファイルを削除してください。
```

**→ 自分で消しに行かない。AIにやらせる！**

※ もちろん自分で消してもOKです

---

# デモ②: ドキュメントに書いてから作らせる

## まず requirements.md をAIに書かせる

```
Todoアプリの要件定義書を requirements.md として作成して。
タスクの追加、完了、削除ができて、
ローカルストレージに保存する仕様で。
```

**→ 要件書すらAIに書かせる！**

※ もちろん自分でゼロから書いてもOKです

---

# デモ②: ドキュメントに書いてから作らせる（続き）

## できた requirements.md を使って作らせる

1. 中身を確認・修正
2. `@requirements.md` で参照させる

```
@requirements.md に従ってアプリケーションを作成してください。
```

**@ コマンド**: ファイルを参照させる
**→ より正確に意図が伝わる！**

---

# デモ②: 要件を更新して再反映する

## requirements.md に指示を追加

```
requirements.md にダークモードで実装する指示を追加して。
```

追加したら、もう一度:

```
@requirements.md に従ってアプリケーションを更新してください。
```

**→ ドキュメントを育てながら開発できる！**

---

# お片付け（2回目）🧹

```
GEMINI.md 以外の全ファイルを削除してください。
```

---

# 2つのパターンの使い分け

| パターン | 向いているケース |
|----------|------------------|
| ①1発プロンプト | 簡単なもの、試作 |
| ②ドキュメントベース | 要件が明確、再現性が必要 |

**複雑なものは②を使おう！**
**「計画モード」の実装が進んできているので実装されたらそれも使おう！**

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
PowerShellで実現可能だよ。
```

- PowerShellスクリプトを生成して実行してくれる
- キー送信でアプリを操作できる
- **知らない人が多いけど、スクリプトで普通にできること**

⚠️ 今の Gemini CLI ではうまくできませんでした。Claude Code ならできました。
**→ AIエージェントにも性能差あり。そのうちできるようになる。**

---

<!-- _class: small -->

# デモ⑤: Todoist と API 連携する

## 外部サービスのAPIも呼べる

```
Todoist に「test」っていうタスクを追加して。
```

**準備:**
1. https://todoist.com/ でアカウント作成
2. 設定 → 連携 → APIトークンを取得
3. トークンをAIに伝える

**→ タスクの追加・一覧表示・削除もAIに任せられる！**

⚠️ Gemini CLI 無料版ではこのレベルの指示ではうまくいきませんでした。
Claude Code でデモします。Gemini でもできないか、一緒に試行錯誤してみましょう！

---

<!-- _class: lead -->

# ここまでわかれば
# 何にでも使えます！ 🎉

## あとは1つだけ知っておくといいこと

---

# コンテキストの量を意識せよ 📊

## 唯一ちょっと意識しておきたいこと

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

<!-- _class: x-small -->

# 対策: 定期的にリセットする

## クリアする
```powershell
# 会話履歴を削除する
/clear
```

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

# GEMINI.md の階層

```
~/.gemini/GEMINI.md        ← グローバル（全プロジェクト共通）
プロジェクト/GEMINI.md     ← プロジェクト固有
プロジェクト/src/GEMINI.md ← サブディレクトリ固有
```

すべて読み込まれて結合される

---

<!-- _class: xx-small -->

# GEMINI.md の階層 ― 具体例

## ~/.gemini/GEMINI.md（グローバル：全プロジェクト共通）
```markdown
- 日本語で考えて、日本語で回答してください
- コードにはコメントを日本語で書いてください
```
→ **どのプロジェクトでも毎回言わなくて済む！**

## プロジェクト/GEMINI.md（プロジェクト固有）
```markdown
# Todoアプリ
- HTML / CSS / JavaScript で実装
- ローカルストレージで永続化
- ダークモードで統一
```
→ **このプロジェクトのルールをAIが常に把握**

## プロジェクト/tests/GEMINI.md（サブディレクトリ固有）
```markdown
- テストコードを書くときは Jest を使用してください
```
→ **tests/ の中で作業するときだけ追加で読み込まれる**

---

# デモ: GEMINI.md に作業ログ機能を追加しよう

## AIが自動で作業ログをつけてくれる！

GEMINI.md に以下を追記:

```markdown
# ルール
- 1回の会話ごとに、必ず notes/YYYY-MM-DD.md に
  作業ログを追記してください
- 形式: ## HH:MM - やったこと
- ファイルがなければ作成、あれば追記
```

---

# デモ: 作業ログがつくか試してみよう

## 何回か会話してみる

AIに何か作業させて、notes/ を確認してみましょう

**→ 会話のたびに作業ログが追記されている！**
**→ GEMINI.md にルールを書くだけで、AIの行動が変わる**

これが GEMINI.md の力！

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

**もっと活用するなら使っていきたい機能:**
- Extensions（拡張機能）
- MCP（外部ツール連携）
- Hooks（自動化）
- Skills（再利用可能な技）
- Custom Commands（カスタムコマンド）
- Sub-Agents（サブエージェント）

---

<!-- _class: x-small -->

# ⚠️ この辺りはすぐに変わります

## 機能の詳細を暗記しても意味がない

- AIエージェントの進化は**とても速い**
- 今日紹介した機能も、数ヶ月後には別物になっているかも

## でも本質は変わらない

- **コンテキスト**: AIに何を見せるか
- **実行タイミング**: いつ、何をさせるか

この2つだけ意識していれば大丈夫

## 難しそう？ → 習うより慣れろ！

先に勉強して覚えようとしなくていい。尻込みも不要。
**使いながら覚える。それが一番早い。**

---
<!-- _class: small -->

# Extensions（拡張機能）

## AIの能力を拡張するパッケージ

- プロンプト、MCPサーバー、スキル、コマンドをまとめたパッケージ
- チームで共有して環境を統一できる
- 公式・コミュニティ製が **351個以上** 公開中

**インストールは1行:**
```powershell
gemini extensions install <GitHubリポジトリURL>
```

GitHub、Terraform、Redis、Figma、Stripe など多数
https://geminicli.com/extensions/ で一覧を見れる

⚠️ 多くの拡張は APIキーやトークンなどの認証設定が必要

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

<!-- _class: x-small -->

# Hooks（フック）

## AIの動作の「前後」にスクリプトを自動実行

```json
// .gemini/settings.json
{
  "hooks": {
    "BeforeTool": [{
      "matcher": "write_file|replace",
      "hooks": [{
        "name": "secret-scanner",
        "type": "command",
        "command": ".gemini/hooks/block-secrets.sh",
        "description": "シークレットの混入を防止"
      }]
    }]
  }
}
```

→ **ファイル書き込みの前に、秘密情報が含まれてないかチェック！**

- スクリプトは自分で書く or 拡張機能としてまとめて入手もできる

---

<!-- _class: x-small -->

# Skills（スキル）

## 再利用可能な「技」を Markdown で定義

```
.gemini/skills/code-reviewer/SKILL.md   ← プロジェクト用
~/.gemini/skills/code-reviewer/SKILL.md ← 全プロジェクト共通
```

```markdown
---
name: code-reviewer
description: コードレビューを実施するスキル
---
# Code Reviewer
コードを徹底的にレビューして、バグやセキュリティの問題を指摘してください。
```

- `/code-reviewer` と打つだけで実行
- `scripts/` にスクリプトを配置して実行させることも可能
- チームで共有・再利用できる
- Claude Code の Skills と互換性あり！スキルの使い回しができる

---

# Custom Commands（カスタムコマンド）

## よく使うプロンプトをコマンド化

```
.gemini/commands/test.toml → /test で実行
~/.gemini/commands/       → 全プロジェクト共通
```

`.toml` ファイルにプロンプトを書くだけ！

- ネームスペースも可: `git/commit.toml` → `/git:commit`
- チームで共有・バージョン管理できる

---

# Sub-Agents（サブエージェント）

## AIが別のAIに仕事を振る

- 専門的なタスク（コードレビュー、ドキュメント作成など）を別のエージェントに委任
- 並列実行・独立したコンテキストで動作
- `/subagents` コマンドで管理

⚠️ まだ実験的機能（YOLO モードが必要）

**→ 1人のAIが全部やるのではなく、チームのように分業できる時代へ**

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

**現状はClaude Codeが総合力でトップ。モデル単体で見るとCodexが少し強い印象というのが胡田の印象。**

---

<!-- _class: lead -->

![bg right:25% 90%](./images/ebi-icon-circle.png)

# まとめ

---

# 今日やったこと

1. ✅ VS Code + Node.js + Gemini CLI をインストール
2. ✅ Gemini CLI Companion で VS Code と連携
3. ✅ AIエージェントにTodoアプリを作らせた
   - 1発プロンプト / ドキュメントベース
4. ✅ 「AIにやらせる」マインドセットを体験
5. ✅ YOLOモードで自動実行
6. ✅ GEMINI.md でAIをカスタマイズ（作業ログも自動で！）
7. ✅ 高度な機能の紹介（Extensions, MCP, Hooks, Skills, Commands, Sub-Agents）

---

# 次のステップ

- 自分の作りたいものをAIに作らせてみる
- 自分のやりたいことをどうやったらできるか、AIに聞いてみる
- requirements.md を書いて再現性を高める
- GEMINI.md を育てて、自分好みのAIに

---


<!-- _class: lead -->

# AIエージェントに
# 頼むだけで
# 全部できる時代へ

**胡田はもう仕事の8割はAIエージェントに話しかけるだけです。Skill増殖中。あなたも今日から始めましょう！**

---


<!-- _class: xx-small -->

# 参考リンク

## インストール
- VS Code: https://code.visualstudio.com/
- Node.js: https://nodejs.org/

## 公式ドキュメント
- Gemini CLI GitHub: https://github.com/google-gemini/gemini-cli
- Gemini CLI Docs: https://geminicli.com/
- GEMINI.md: https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html

---

<!-- _class: xx-small -->

# 参考リンク（続き）

## 高度な機能
- Extensions 一覧: https://geminicli.com/extensions/
- MCP: https://geminicli.com/docs/tools/mcp-server/
- Hooks: https://developers.googleblog.com/tailor-gemini-cli-to-your-workflow-with-hooks/
- Skills: https://geminicli.com/docs/cli/skills/
- Custom Commands: https://geminicli.com/docs/cli/custom-commands/
- Sub-Agents: https://geminicli.com/docs/core/subagents/

## 共通標準・比較
- AGENTS.md（共通標準）: https://agents.md/
- Claude Code の日常活用: https://dev.classmethod.jp/articles/claude-code-daily-workflow/

---

# 実は…このスライドも

## 全部 Claude Code に書いてもらいました

- スライドの構成・文章・コード例
- 修正や順番の入れ替えも全部AIに指示
- 人間がやったのは「こういうスライドにして」と伝えることだけ

**AIエージェント、本当になんでもできる時代です**

その過程をnote記事にしました → https://note.com/ebibibi/n/n17504280d80d

---

<!-- _class: lead -->

![bg right:25% 90%](./images/ebi-icon-circle.png)

# ありがとうございました！

## 質問・感想はお気軽に

YouTube: https://www.youtube.com/@ebibibi
チャンネル登録お願いします！

