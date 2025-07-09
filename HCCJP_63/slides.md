---
marp: true
theme: gaia
paginate: true
backgroundColor: #fff
style: |
  section {
    font-family: 'Meiryo', 'Segoe UI', sans-serif;
  }
  h1 {
    color: #0078d4;
  }
  h2 {
    color: #0078d4;
  }
  .speaker {
    font-size: 0.9em;
    color: #666;
  }
  table {
    font-size: 0.8em;
  }
  th {
    background-color: #0078d4;
    color: white;
  }
---

<!-- _class: lead -->

![bg right:30% 80%](../Images/hcc-logo02f.png)

# HCCJP 第63回勉強会

## ハイブリッドクラウド研究会

**2025年7月11日（金）14:00開始**

---

# 本日のテーマ

## 🚀 Azure + 生成AI

- Claude Code×Azure
- Gemini CLI×Azure  
- Microsoft "Adaptive Cloud" 最新動向
- Azure Arc対応Kubernetes拡張機能 "Edge RAG"

---

# 🤖 このスライドについて

## 生成AIで作成しました！

### 使用技術
- **Claude** - スライド内容の生成
- **Marp** - Markdownベースのプレゼンテーション
- **VS Code** - 統合開発環境

### ✨ 生成AIの活用例
- 司会進行用スライドの構成
- デザインとレイアウトの最適化
- ロゴの効果的な配置

**今日のテーマにぴったり！生成AIの実践例です**

---

# タイムテーブル

| 時刻 | 時間 | セッション | スピーカー |
|------|------|------------|------------|
| 14:00 | 5分 | オープニング | 胡田 昌彦 |
| 14:05 | 20分 | 【前半】Claude Code×Azure, Gemini CLI×Azure | 胡田 昌彦 |
| 14:25 | 20分 | Microsoft "Adaptive Cloud" Updates | 高添 修 氏 |
| 14:45 | 20分 | Azure Arc対応 K8s拡張機能 "Edge RAG" | 胡田 昌彦 |
| 15:05 | 10分 | 【後半】Claude Code×Azure, Gemini CLI×Azure | 胡田 昌彦 |
| 15:15 | 10分 | Q&A | 全員 |
| 15:25 | 5分 | クロージング | 胡田 昌彦 |

---

<!-- _class: lead -->

![bg right:30% 80%](../Images/hcc-logo02f.png)

# オープニング

**司会：胡田 昌彦**
<span class="speaker">日本ビジネスシステムズ株式会社<br>Microsoft MVP for Azure Hybrid, Windows Server</span>

---

![bg right:20% 60%](../Images/hcc-logo02f.png)

# HCCJPとは

## ハイブリッドクラウド研究会

- 毎月第2金曜日 14時から開催
- Azure + 生成AI関連の最新情報をお届け
- オンライン配信（YouTube HCCJPチャンネル）

📺チャンネル登録お願いします！
https://www.youtube.com/channel/UCrf4bEl7yJnkGYo3F67gA7w

---

# 本日の注意事項

- 📹 配信は録画されています
- 💬 チャットでのご質問歓迎
- 🔇 マイクはミュートでお願いします
- 📝 Q&Aセッションで匿名質問も可能

---

# 質問方法

## 💡 Slidoで匿名質問ができます！

- **匿名で質問可能** - お気軽にどうぞ！
- **いつでも質問OK** - セッション中でも遠慮なく
- **疑問点はすぐに** - 思いついたらすぐ投稿

### 📱 Slidoの使い方
1. QRコードまたはURLからアクセス
2. 質問を入力して送信
3. 他の方の質問に「いいね」も可能

**セッション中、疑問点があればいつでも質問してください！**

---

<!-- _class: lead -->

# セッション①【前半】

## Claude Code×Azure, Gemini CLI×Azure

**スピーカー：胡田 昌彦**
<span class="speaker">日本ビジネスシステムズ株式会社<br>Microsoft MVP for Azure Hybrid, Windows Server</span>

⏱️ 14:05 - 14:25（20分）

---

# セッション①について

## 🎯 本セッションのポイント

- 話題沸騰中のClaude CodeとGemini CLI
- Azure環境構築のTipsと実演
- Microsoft Learn Docs MCPの活用
- **無料でも実現可能！**

コンソールベースの生成AIでまるで魔法のような体験を！

---

# 📥 Step 1: インストール

## Claude Codeのインストール

```bash
# VS Code拡張機能から
1. 拡張機能マーケットプレイスを開く
2. "Claude Code" を検索
3. インストールボタンをクリック
```

## Gemini CLIのインストール

```bash
# npmでインストール
npm install -g @google/generative-ai-cli

# または、直接ダウンロード
# https://github.com/google/generative-ai-cli
```

**🎬 実演：実際にインストールしてみましょう！**

---

# ⚙️ Step 2: 基本設定

## 📝 claude.mdの作成

```markdown
# Claude設定ファイル

## プロジェクトのコンテキスト
このプロジェクトはAzureを使用します。

## 重要な指示
- 必ずMicrosoft Learn MCPを参照してから実装すること
- Azure関連の質問は公式ドキュメントを確認
```

## 📝 gemini.mdの作成

```markdown
# Gemini設定ファイル

## プロジェクトのコンテキスト
Azure環境での開発を行います。

## 必須事項
- Microsoft Learn MCPで最新情報を確認してから実装
```

---

# 🔗 Step 3: Microsoft Learn MCP連携

## MCPの設定方法

1. **MCP Server for Microsoft Learn Docsのインストール**
   ```bash
   npm install -g @microsoft/mcp-server-learn
   ```

2. **VS Codeでの設定**
   - 設定 → MCP → サーバー追加
   - Microsoft Learnサーバーを有効化

3. **動作確認**
   - `@learn` コマンドでドキュメント検索
   - Azure関連の最新情報を即座に参照

**🎬 実演：MCPを使ってAzureドキュメントを検索！**

---

# 📋 Step 4: AIへの指示設定

## claude.md / gemini.mdへの追加指示

```markdown
## 開発ルール
1. Azure関連の実装前に必ず以下を実行：
   - @learn でMicrosoft公式ドキュメントを検索
   - 最新のベストプラクティスを確認
   
2. 実装の流れ：
   - ドキュメント確認 → 設計 → 実装
   
3. セキュリティ：
   - Azure Key Vaultの使用を検討
   - マネージドIDを優先
```

**💡 ポイント：AIが自動的に公式ドキュメントを参照するように！**

---

# 💭 Step 5: 何を作るか相談

## AIとのブレインストーミング

### 相談例：
「Azureを使って、今すぐ役立つものを作りたい」

### AIからの提案例：
- Azure Functionsで自動化ツール
- Static Web Appsでポートフォリオサイト
- Cosmos DBを使ったチャットアプリ
- Azure OpenAIを活用したアシスタント

**🎬 実演：実際にAIと相談してアイデアを出してもらいます！**

---

# 📝 Step 6: design.mdの作成

## 決定した内容を文書化

```markdown
# プロジェクト設計書

## プロジェクト名
Azure ベースの○○アプリケーション

## 概要
[AIと決めた内容を記載]

## 使用するAzureサービス
- Azure Functions
- Azure Storage
- Azure Key Vault

## アーキテクチャ
[簡単な構成図や説明]

## 実装ステップ
1. リソースグループの作成
2. 各サービスのデプロイ
3. 接続設定
```

---

# 🚀 Step 7: 実装開始！

## AIに実装を依頼

```markdown
design.mdに基づいて、以下を実装してください：
1. 必要なAzureリソースの作成スクリプト
2. 基本的なアプリケーションコード
3. デプロイ用の設定ファイル
```

## 実装のポイント
- AIが自動的にMCP経由でドキュメントを参照
- 最新のベストプラクティスに基づいた実装
- インフラとコードを同時に生成

**🎬 実演：実装を開始してもらいます！**

---

# ⏸️ セッション①前半まとめ

## ここまでの成果

✅ Claude Code / Gemini CLIのセットアップ完了
✅ Microsoft Learn MCPとの連携設定
✅ AIへの適切な指示の設定
✅ プロジェクトの方向性決定（design.md）
✅ 実装開始

## 🔜 後半セッションでは...
- 実装の続き
- トラブルシューティング
- デプロイまでの流れ

**では、セッション②の後でお会いしましょう！**

---

<!-- _class: lead -->

# セッション②

## Microsoft "Adaptive Cloud" Updates

**スピーカー：高添 修 氏**
<span class="speaker">日本マイクロソフト株式会社</span>

⏱️ 14:25 - 14:45（20分）

---

# セッション②について

## 📊 毎月恒例の最新動向

- Microsoft "Adaptive Cloud"の最新アップデート
- 先月休会分も含めた**2か月分の情報**
- Azureの新機能・サービス
- 今後のロードマップ

お見逃しなく！

---

<!-- _class: lead -->

# セッション③

## Azure Arc対応Kubernetes拡張機能
## "Edge RAG"

**スピーカー：胡田 昌彦**
<span class="speaker">日本ビジネスシステムズ株式会社<br>Microsoft MVP for Azure Hybrid, Windows Server</span>

⏱️ 14:45 - 15:05（20分）

---

# セッション③について

## 🔧 Edge RAGの実践

- Azure Local上での簡単な動作
- プレビュー版の展開と動作検証
- **はまりポイントの共有**
- 実践的なTips

現場で役立つ情報満載！

---

<!-- _class: lead -->

# セッション①【後半】

## Claude Code×Azure, Gemini CLI×Azure
## （続き）

**スピーカー：胡田 昌彦**
<span class="speaker">日本ビジネスシステムズ株式会社<br>Microsoft MVP for Azure Hybrid, Windows Server</span>

⏱️ 15:05 - 15:15（10分）

---

<!-- _class: lead -->

# Q&Aセッション

## 💬 ご質問をお待ちしています！

- チャットでの質問歓迎
- **匿名での質問も可能**
- どんな質問でもOK！

⏱️ 15:15 - 15:25（10分）

---

# 主催・幹事

## 主催：ハイブリッドクラウド研究会

**主幹事**
- 日本ビジネスシステムズ株式会社

**幹事**（50音順）
- NTTコミュニケーションズ株式会社
- 日商エレクトロニクス株式会社
- 日本ヒューレット・パッカード株式会社
- 日本マイクロソフト株式会社
- VistaNet株式会社
- 株式会社ネットワールド
- 三井情報株式会社
- レノボ・エンタープライズ・ソリューションズ株式会社

---

<!-- _class: lead -->

# 次回予告

## 📅 次回は8月9日（金）14:00〜

毎月第2金曜日に開催！

**YouTubeチャンネル登録**をお忘れなく！
https://www.youtube.com/channel/UCrf4bEl7yJnkGYo3F67gA7w

---

<!-- _class: lead -->

![bg left:30% 80%](../Images/hcc-logo02f.png)

# ご参加ありがとうございました！

## また来月お会いしましょう！

🎯 本日の資料は後日公開予定
📧 お問い合わせはHCCJP事務局まで

**#HCCJP** でツイートお願いします！
