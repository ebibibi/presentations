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
    font-size: 1.6em;
  }
  h2 {
    color: #0078d4;
    font-size: 1.4em;
  }
  h3 {
    font-size: 1.2em;
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
  /* コンテンツが多いスライド用のクラス */
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
  /* さらに小さいスライド用のクラス */
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
  /* leadクラス用の大きめのフォント */
  section.lead h1 {
    font-size: 2.0em;
  }
  section.lead h2 {
    font-size: 1.6em;
  }
  section.lead .speaker {
    font-size: 1.0em;
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

---

# 🤖 このスライドについて（続き）

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

- 📹 配信は録画されています→アーカイブでもいつでも見られます！
- 💬 チャットでの質問大歓迎！
- 📝 Q&Aセッションで匿名質問も可能！

---

<!-- _class: small -->

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

## Claude Code × Azure,</br> Gemini CLI × Azure

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

<!-- _class: small-->

# 🤔 なぜCLIツールを選ぶのか？

## GUI vs CLI AIコーディングアシスタント

| ツール | タイプ | 料金 |
|--------|--------|------|
| **Cline** | VS Code拡張 | 無料（API料金別） |
| **GitHub Copilot** | VS Code統合 | 無料～ |
| **Cursor** | 専用エディタ | 無料～ |
| **Claude Code** | CLI | 月額$20～ |
| **Gemini CLI** | CLI | 無料～ |

### 🚀 CLIツールの利点
- **自動化しやすい** - スクリプトやCIに組み込み可能
- **軽量・高速** - GUIのオーバーヘッドなし / 「VSCodeのやり方」で失敗すること無し
- **柔軟性が高い** - 任意のエディタと併用可能


---

<!-- _class: small-->

# 🆚 Claude Code vs Gemini CLI

## 主な違い

| 項目 | Claude Code | Gemini CLI |
|------|-------------|------------|
| **料金** | 有料（月額$20） | **無料**でも利用可能 |
| **環境** | WSL必須（Windows） | **Windowsで直接動作** |
| **セットアップ** | 複雑（DNS設定等） | シンプル |
| **モデル** | Claude Opus 4/Sonnet 4 | Gemini 2.5 Pro/Flash |
| **コード生成** | 非常に高品質 | 高品質 |
| **MCP対応** | ✅ | ✅ |

### 💡 選び方のポイント
- **無料で試したい** → Gemini CLI
- **WSL設定が面倒** → Gemini CLI
- **現時点で最強のものが使いたい** → Claude Code

---

<!-- _class: small -->

# 📥 Step 1: インストール

## Claude Codeのインストール（Windows WSL版）

```bash
# WSL2のセットアップ（未インストールの場合）
wsl --install

# WSL内でNode.jsをインストール
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Claude Codeをインストール
npm install -g @anthropic-ai/claude-code #おそらく権限のエラーが出ます
```

📚 **公式ドキュメント**: https://docs.anthropic.com/en/docs/claude-code

---

<!-- _class: x-small -->

## Claude Codeのインストール（Windows WSL版ではこちらを個人的に推奨）

```bash
# First, save a list of your existing global packages for later migration
npm list -g --depth=0 > ~/npm-global-packages.txt

# Create a directory for your global packages
mkdir -p ~/.npm-global

# Configure npm to use the new directory path
npm config set prefix ~/.npm-global

# Note: Replace ~/.bashrc with ~/.zshrc, ~/.profile, or other appropriate file for your shell
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc

# Apply the new PATH setting
source ~/.bashrc

# Now reinstall Claude Code in the new location
npm install -g @anthropic-ai/claude-code

# Optional: Reinstall your previous global packages in the new location
# Look at ~/npm-global-packages.txt and install packages you want to keep
```

📚 **公式ドキュメント**: https://docs.anthropic.com/en/docs/claude-code

---

<!-- _class: x-small -->

# ⚠️ 重要！WSL環境でClaude Codeがオフラインになる問題

## 🚨 WSLでClaude Codeがすぐにofflineになる場合の解決方法

### 1. WSL設定ファイルの編集
```bash
# /etc/wsl.conf に以下を追加
[network]
generateResolvConf = false
```

### 2. WSLを再起動
```bash
wsl --shutdown
# その後、WSLを再度起動
```

### 3. DNS設定を手動で追加
```bash
# /etc/resolv.conf に適切なDNSサーバーを設定
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
```

**💡 詳細はこちら → https://note.com/ebibibi/n/n211c76198608**

---

# 💻 WSLとWindowsの連携

## VSCodeとWSLの連携

### 📁 Windows側のプロジェクトフォルダへのアクセス
```bash
# Windows側のCドライブにアクセスする場合
cd /mnt/c
```

### ⚡ パフォーマンスのために
- プロジェクトファイルはWSL側（`~/projects/`など）に配置推奨
- Windows側のファイルアクセスは信じられないくらい遅い

---

## Gemini CLIのインストール

```bash
# あらかじめNode.js (+npm) をインストール(インストーラーで「次へ」と進めるだけでよい)

# npmでインストール
npm install -g @google/generative-ai-cli

```

- Claude Codeと比べると超簡単！✨🚀

---
<!-- _class: small -->
## 動画も参考にどうぞ！

### 📹 Claude CodeをWindowsにインストールする方法！
[![Claude Code](https://img.youtube.com/vi/3NbsOeZMhgE/mqdefault.jpg)](https://www.youtube.com/watch?v=3NbsOeZMhgE)

### 📹 Gemini CLI：Google最強AIが今だけ無料で使える！
[![Gemini CLI](https://img.youtube.com/vi/Wp5DSo_3bTU/mqdefault.jpg)](https://www.youtube.com/watch?v=Wp5DSo_3bTU)

---

<!-- _class: small -->

# ⚙️ Step 2: 基本設定

## 📝 CLAUDE.mdの作成

- 起動時に自動的に読み込む設定ファイル
- 既存レポジトリなら /init を実行すれば素敵なものが自動作成される

```markdown
# 必ず守るべき重要な指示
- 日本語で応答すること
- 必ずMicrosoft Learn MCPを参照してから実装すること
- 初回には必ず design.md, progress.md を読み現在の状況を把握すること
- 進捗は progress.md に記載すること
```

## 📝 gemini.mdの作成

- 役割はCLAUDE.mdと一緒です。
- /init コマンド的なものは現時点ではなさそうです。
---

## 他にも山ほどTipsはあります
多すぎる & みんな試行錯誤中なので、今日は記事紹介のみとしておきます。

- [速習 Claude Code](https://zenn.dev/mizchi/articles/claude-code-cheatsheet)
- [実務で使っているClaude Codeの開発環境の紹介](https://zenn.dev/gatechnologies/articles/5780de81709e97)
- [Claude Codeにコマンド一発でMCPサーバを簡単設定](https://zenn.dev/karaage0703/articles/3bd2957807f311)
- [テストから始めるAgentic Coding 〜Claude Codeと共に行うTDD〜 / Agentic Coding starts with testing \- Speaker Deck](https://speakerdeck.com/rkaga/agentic-coding-starts-with-testing)
---

<!-- _class: x-small -->

# 🔗 Step 3: Microsoft Learn MCP連携

- 必須ではないですけど超お勧めです！
- MCP連携の設定場所は複数あります。下記はプロジェクトレベルの例。

## Claude Code

```bash
claude mcp add microsoft_learn_mcp -s project -t http https://learn.microsoft.com/
```

## Gemini CLI
- .gemini/settings.jsonに下記を記載
```
{
  "mcpServers": {
    "microsoft_learn_mcp": {
      "type": "http",
      "url": "https://learn.microsoft.com/"
    }
  }
}
```
- ただし、Gemini CLIはきちんとMCP経由ではLearnの記事を読みにいってくれない。(自力で検索する)

---
<!-- _class: small -->
# 📋 Step 4: Azureへの操作はやっぱり既存ツール群

- 今さらですが…。結局devcontainerを作ってしまうのも楽だと思います。

```
# Install Azure CLI
curl -sL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg && \
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $(lsb_release -cs) main" > /etc/apt/sources.list.d/azure-cli.list && \
    apt-get update && \
    apt-get install -y azure-cli && \
    rm -rf /var/lib/apt/lists/*

# Install PowerShell 7
wget -q "https://packages.microsoft.com/config/debian/$(lsb_release -rs)/packages-microsoft-prod.deb" -O packages-microsoft-prod.deb && \
    dpkg -i packages-microsoft-prod.deb && \
    apt-get update && \
    apt-get install -y powershell && \
    rm packages-microsoft-prod.deb && \
    rm -rf /var/lib/apt/lists/*

# Install Azure PowerShell Module
pwsh -Command "Set-PSRepository -Name 'PSGallery' -InstallationPolicy Trusted; Install-Module -Name Az -Scope AllUsers -Force"

# Install Bicep CLI
curl -Lo bicep https://github.com/Azure/bicep/releases/latest/download/bicep-linux-x64 && \
    chmod +x ./bicep && \
    mv ./bicep /usr/local/bin/bicep

```
---

# 📝 Step 5: AIと協力して作業する！
個人的に推奨のやり方
- まずAIと何をどのような技術要素で実装するのかを相談する。
- 決定事項を design.md にまとめてもらう。
- 実装計画をAIに立ててもらい progress.md に記載してもらう。
- AIに実装を依頼し、progress.md に進捗を記載してもらう。

---

<!-- _class: lead -->

# 🚀 実際にやってみましょう！

---

<!-- _class: lead -->

# セッション②

## Microsoft "Adaptive Cloud" Updates

**スピーカー：高添 修 氏**
<span class="speaker">日本マイクロソフト株式会社</span>

⏱️ 14:25 - 14:45（20分）

---

<!-- _class: lead -->

# セッション③

## Azure Arc対応Kubernetes拡張機能
## "Edge RAG"

**スピーカー：胡田 昌彦**
<span class="speaker">日本ビジネスシステムズ株式会社<br>Microsoft MVP for Azure Hybrid, Windows Server</span>

⏱️ 14:45 - 15:05（20分）

---

<!-- _class: small -->

# ⚠️ 何度も失敗するので全てスクリプト化しておくこと！

## 😓 展開の現実的な課題

### 失敗の頻度
- 展開には様々な場所で失敗し、何度もOS再インストールからやり直した
- **おそらく10回以上**やり直し

### 💡 強い推奨事項
- **極力自動化することを強く推奨**
- PowerShellスクリプト化

---

<!-- _class: lead -->

# どんなものか見てみましょう！

---

<!-- _class: lead -->

# 個人的にハマったポイント

---


<!-- _class: small -->

# Active Directory事前準備で入力する認証情報

## わかりにくいコマンド
```powershell
New-HciAdObjectsPreCreation -AzureStackLCMUserCredential (Get-Credential) -AsHciOUName "OU=azurelocal,DC=dev1,DC=ebisuda,DC=net"
```

## 🤔 注意
- このADの準備段階で入力するクレデンシャルはazurelocalのnodeのローカルの管理者となるイメージ
- 既存のドメインユーザーを入力するのではないので注意。

---

<!-- _class: x-small -->

# 🚨 AKSクラスタ作成時の注意点

## コントロールプレーンIP指定の問題

### 問題の症状
- Edge RAGの前提条件となるAKSクラスタがコントロールプレーンIPを指定しないと展開できない状況が発生
- 本来はコントロールプレーンIPを指定しなくても展開できるはず

### 解決方法
```bash
az aksarc create \
  --control-plane-count 1 \
  --control-plane-ip 10.1.1.205 \
  # その他のパラメータ
```

### 📝 備考
- サポートに問い合わせをしたが再現しないため未解決
- しかし、私の環境では何度でも再現した
- 上記オプションを追加することで解決

---

<!-- _class: small -->

# Edge RAGの要求スペックが高すぎる問題

## 💻 必要なVM構成

### GPUが使用可能な場合
- **Standard_NC8_A2** × 3ノード + **Standard_D8s_v3** × 3ノード

### CPUのみの場合
- **Standard_D8s_v3** × 6ノード

| VM サイズ | GPU | GPU メモリ (GiB) | vCPU | メモリ (GiB) |
|-----------|-----|------------------|------|--------------|
| Standard_NC8_A2 | 1 | 16 | 8 | 16 |

| VM サイズ | vCPU | メモリ (GB) |
|-----------|-----|-------------|
| Standard_D8s_v3 | 8 | 32 |

---

<!-- _class: small -->

# 合計リソース要求量

## 💰 GPU使用時の合計スペック
- **vCPU**: 48コア（NC8_A2: 24 + D8s_v3: 24）
- **メモリ**: 120GB（NC8_A2: 24GB + D8s_v3: 96GB）
- **vGPU**: 3（各16GB GPU メモリ）

## 🖥️ CPU専用時の合計スペック
- **vCPU**: 48コア（D8s_v3: 8 × 6ノード）
- **メモリ**: 192GB（D8s_v3: 32GB × 6ノード）

## 😅 現実的な課題
可用性、冗長性の観点ではよいが、個人で検証するのはきつすぎる。
外部にLLMを配置するなら、1ノードだけでも動作した。

---
# Azure Local（旧Azure Stack HCI）でのリソース管理の落とし穴

## 🚨 ノードプール追加時の謎現象

### 問題の症状
- Hyper-V管理画面では**CPU、メモリ、ストレージに余裕がある**
- しかし、ノードプール追加時に**リソース不足エラー**が頻発
- 空きリソースがあっても実際には使用できない状態

### 現象の詳細
- **VHDマウント失敗**エラーが表示されることもある
- 裏側の処理で何らかの問題が発生している模様
- 一見、リソースに問題がないように見えるため混乱

### 💡 解決方法
**Azure Localホスト（Hyper-Vノード）の再起動**
- 単純だが効果的な解決策
- 再起動後、リソースが正常に利用可能になる

---

# Edge RAGの現状評価

## 📊 プレビュー版の特徴と課題

### 🔍 現状の印象
- **プレビューのためまだまだ荒削り**
- 不安定な動作や予期しないエラーが発生
- ドキュメントも断片的で試行錯誤が必要

### 🏗️ 本番を見据えた設計
- **冗長構成が標準**で組み込まれている
- 高可用性を前提とした構成になっている
- 障害発生時の対応も考慮された設計

### 💻 リソース要求の現実
- **ホストに要求されるリソースはかなり大きい**
- 個人検証には厳しいスペック要求
- **しかし開発ゼロで使える**ように構成されているのは良い

---

<!-- _class: lead -->

# ありがとうございました！

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
