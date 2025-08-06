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
  /* さらにほんの少し小さいスライド用のクラス */
  section.xx-small {
    font-size: 22px;
  }
  section.xx-small h1 {
    font-size: 1.2em;
  }
  section.xx-small h2 {
    font-size: 1.0em;
  }
  section.xx-small code {
    font-size: 0.6em;
  }
  section.xx-small li {
    font-size: 0.88em;
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

# HCCJP 第64回勉強会

## ハイブリッドクラウド研究会

**2025年8月8日（金）14:00開始**

---

# 本日のテーマ

## 🚀 BicepでMicrosoft Entra IDリソース & オンプレミスVM管理

- Bicep による Entra ID リソース管理
- Azure Arc によるオンプレミス VM 管理
- Microsoft Adaptive Cloud 最新動向

---

<!-- _class: lead -->

![bg right:30% 80%](../Images/hcc-logo02f.png)

# オープニング

**司会：胡田 昌彦**
<span class="speaker">日本ビジネスシステムズ株式会社<br>Microsoft MVP for Azure Hybrid, Windows Server</span>

---
<!-- _class: x-small -->

# 👨‍💻 自己紹介

## 胡田 昌彦（えびすだ まさひこ）

### 📺 現在の活動
- **YouTubeに注力中！** → https://youtube.com/@ebibibi

### 🏆 資格・認定
- **Microsoft MVP for Azure Hybrid & Windows Server**（ダブル受賞）
- **Microsoft Certified Trainer**

### 📖 著書
- **「Windowsインフラ管理者入門」** 著者

### 🎵 趣味
- ベース、ドラム、セッション、将棋

---

# 🤖 このスライドについて

## 生成AIで作成しました！

### 使用技術
- **Claude** - スライド内容の生成
- **Marp** - Markdownベースのプレゼンテーション
- **VS Code** - 統合開発環境

**先月分の内容をもとに「今月分作っておいて！」って頼むだけでバッチり作ってくれてビビってます。**

---

# タイムテーブル

| 時刻 | 時間 | セッション | スピーカー |
|------|------|------------|------------|
| 14:00 | 5分 | オープニング | 胡田 昌彦 |
| 14:05 | 40分 | BicepでMicrosoft Entra IDリソース&オンプレミスVM管理 | 胡田 昌彦 |
| 14:45 | 10分 | Q&A | 全員 |
| 14:55 | 20分 | Microsoft "Adaptive Cloud" Updates | 高添 修 氏 |
| 15:15 | 10分 | Q&A | 全員 |
| 15:25 | 5分 | クロージング | 胡田 昌彦 |

---

![bg right:20% 60%](../Images/hcc-logo02f.png)

# HCCJPとは

## ハイブリッドクラウド研究会

- 毎月第2金曜日 14時から開催
- Azure + ハイブリッドクラウド関連の最新情報をお届け
- オンライン配信（YouTube HCCJPチャンネル）

📺チャンネル登録お願いします！
https://www.youtube.com/channel/UCrf4bEl7yJnkGYo3F67gA7w

---

# 本日の注意事項

- 📹 配信は録画されています→アーカイブでもいつでも見られます！
- 💬 Youtubeのチャットでのコメント大歓迎！
- 📝 Q&Aセッションで匿名質問も可能！(Slido利用)

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

# セッション①

## BicepでMicrosoft Entra IDリソース</br>& オンプレミスVM管理

**スピーカー：胡田 昌彦**
<span class="speaker">日本ビジネスシステムズ株式会社<br>Microsoft MVP for Azure Hybrid, Windows Server</span>

⏱️ 14:05 - 14:45（40分）

---

# セッション①について

## 🎯 本セッションのポイント

- **Bicep によるEntra IDリソース管理**の実演
- **Azure Arc によるオンプレミスVM管理**の実演
- 実際のコード例とデモンストレーション
- **Infrastructure as Code（IaC）** の活用法

**コードで分かりやすく解説します！**

---

<!-- _class: x-small -->

# 🎯 なぜBicepでEntra IDなのか？

## Infrastructure as Code（IaC）の重要性

### 従来の手動管理の課題
- **手作業によるヒューマンエラー**
- **設定の属人化**
- **環境間の設定差異**
- **スケーラビリティの問題**

### Bicepによる解決
- **宣言的な設定記述**
- **バージョン管理可能**
- **再現性の確保**
- **自動化・CI/CD対応**

**Entra IDもオンプレVMも「コードで管理」する時代です！**

---

<!-- _class: small -->

# 🔧 BicepでEntra ID管理：できること

## ✅ できること（今回のデモで扱う内容）

- **グループの作成・管理**
- **グループオーナーの設定**
- **グループメンバーの管理**
- **サービスプリンシパルの作成**
- **アプリケーション登録**
- **Web Appsとの認証統合**
- **既存ユーザーの参照** （読み取り専用）

## 🎯 Microsoft Graph Bicep の特徴
- **2025年7月に一般提供開始**
- **動的型（Dynamic Types）** のみサポート
- **Bicep v0.36.1** 以上が必要

---

<!-- _class: small -->

# 🚨 現在の制限事項（2025年8月時点）

## ❌ まだできないこと

- **ユーザーアカウントの作成** （読み取り専用のみサポート）
- **条件付きアクセスポリシー** （機能リクエスト中）
- **アプリケーションパスワードの作成** （証明書のみサポート）
- **ロール割り当て可能グループ** （デプロイ時にエラーが発生）

## 🔧 回避策
- **DeploymentScript リソース**でMicrosoft Graph APIを直接呼び出し
- **Azure PowerShell/CLI** による補完的な処理

## 📚 情報源
- **Microsoft Learn**: [Microsoft Graph Bicep Limitations](https://learn.microsoft.com/en-us/graph/templates/bicep/limitations)
- **GitHub**: [Azure/bicep Issues #13734](https://github.com/Azure/bicep/issues/13734)

---

<!-- _class: small -->

# 📁 今日のデモ構成

## Demo 1-5: Entra ID リソース管理
- **demo1**: グループ作成の基本
- **demo2**: マネージドIDをグループオーナーに設定
- **demo3**: ユーザーをグループメンバーに追加
- **demo4**: サービスプリンシパルによる自動化
- **demo5**: Web Apps + Entra ID認証統合

## Demo 6: Azure Arc VM管理
- **demo6**: オンプレミスVMの構成管理

**実際のコードを見ながら解説していきます！**

📁 **ソースコード**: https://github.com/ebibibi/presentations/tree/main/HCCJP_64_Bicep_EntraID_Arc

---

<!-- _class: lead -->

# 🚀 Demo 1: グループ作成の基本

---

<!-- _class: lead -->

# 🚀 Demo 2: マネージドIDをオーナーに設定

---

<!-- _class: lead -->

# 🚀 Demo 3: ユーザーをメンバーに追加

---

<!-- _class: lead -->

# 🚀 Demo 4: サービスプリンシパルで自動化

---

<!-- _class: lead -->

# 🚀 Demo 5: Web Apps + Entra ID認証

---

<!-- _class: lead -->

# 🚀 Demo 6: Azure Arc VM管理

---

<!-- _class: x-small -->

# 🗂️ プロジェクト構成

## ファイル構成の説明

```
HCCJP_64_Bicep_EntraID_Arc/
├── slides.md                   # 本日のプレゼンスライド
└── Demos/
    ├── demo1_グループ作成/
    │   ├── main.bicep          # グループ作成のメインコード
    │   ├── deploy.ps1          # デプロイスクリプト
    │   └── bicepconfig.json    # Bicep設定ファイル
    ├── demo2_グループ所有者にマネージドIDを設定/
    ├── demo3_グループメンバーにユーザーを設定/
    ├── demo4_サービスプリンシパルを使って自動化/
    ├── demo5_WebAppsとEntraID認証/
    └── demo6_ArcVM構成/
```

**各デモは独立して実行可能です！**

---

<!-- _class: x-small -->

# 🚀 デプロイの基本手順

## PowerShellスクリプトによる自動デプロイ

### 各デモ共通の手順
```powershell
# リソースグループの作成とデプロイ
./deploy.ps1
```

### スクリプトの内容例
```powershell
# リソースグループ名とロケーションの設定
$resourceGroupName = "hccjp-demo1"
$location = "japaneast"

# リソースグループの作成
az group create --name $resourceGroupName --location $location

# Bicep テンプレートのデプロイ
az deployment group create `
    --resource-group $resourceGroupName `
    --template-file ".\main.bicep"
```

**ワンクリックでInfrastructure as Codeが実現！**

---

<!-- _class: lead -->

# 💡 デモ作成中に気が付いた注意点！

---

<!-- _class: small -->

# ⚠️ 実装時のハマりポイント

## 🔧 bicepconfig.jsonの配置場所

- **VS Codeで開いているフォルダのルート**に配置する必要あり
- サブディレクトリに置いても認識されない
- 各デモディレクトリに個別配置が必要(だと思う)
- VS CodeのBicep拡張は挙動が不安定で結果が一意でないように思う。

## 🔄 グループのowner設定は2回実行が必要

- **ManagedIDをグループオーナーに設定する場合**
- **1回目のデプロイでは失敗**することが多い
- **2回目で成功**するパターン
- `dependsOn` を設定しても同様
- **Microsoft公式ドキュメントにも記載されている既知の問題**

---

<!-- _class: small -->

# ⚠️ 削除とトラブルシューティング

## 🗑️ リソース削除の注意点

- **リソースグループ削除だけでは不十分**
- **Entra IDリソース**（グループ、アプリ等）は別途削除が必要

## 🐛 Azure CLI のバグ対応

### よく遭遇するエラー
```
The content for this response was already consumed
```

### 解決方法
- **Azure CLI のバグ**が原因
- **Azure PowerShell** を使用することで回避可能
- Bicepの展開時エラー時にこのメッセージが表示される模様

---

<!-- _class: lead -->

# 🌟 まとめ

---

<!-- _class: small -->

# 📈 今日学んだこと

## 🎯 セッションのまとめ

### Bicep × Entra ID
- **Infrastructure as Code**でIDリソース管理
- **グループ・アプリケーション**の自動化
- **Web Apps認証**との統合

### Bicep × Azure Arc
- **オンプレミスVM**のクラウド管理
- **拡張機能**の自動デプロイ
- **リモート実行**による構成管理

---

<!-- _class: xx-small -->

# 🚀 次のステップ

## より深く学習するために

### 📚 Microsoft 公式学習リソース

#### **Bicep 関連**
- **Bicep 基礎学習パス**: https://learn.microsoft.com/ja-jp/training/paths/fundamentals-bicep/
- **Bicep 上級学習パス**: https://learn.microsoft.com/ja-jp/training/paths/advanced-bicep/
- **Bicep 公式ドキュメント**: https://learn.microsoft.com/ja-jp/azure/azure-resource-manager/bicep/
- **Microsoft Graph Bicep**: https://learn.microsoft.com/ja-jp/graph/templates/bicep/

#### **Azure Arc 関連**
- **Azure Arc 概要**: https://learn.microsoft.com/ja-jp/azure/azure-arc/overview
- **Azure Arc 入門モジュール**: https://learn.microsoft.com/ja-jp/training/modules/intro-to-azure-arc/
- **Azure Arc サーバー管理**: https://learn.microsoft.com/ja-jp/training/paths/deploy-manage-azure-arc-enabled-servers/
- **Azure Arc サーバー公式ドキュメント**: https://learn.microsoft.com/ja-jp/azure/azure-arc/servers/overview


---

<!-- _class: lead -->

# ありがとうございました！

## 質問をお待ちしています！

---

<!-- _class: lead -->

# Q&Aセッション

## 💬 ご質問をお待ちしています！

- チャットでの質問歓迎
- **匿名での質問も可能**
- どんな質問でもOK！

⏱️ 14:45 - 14:55（10分）

---

<!-- _class: lead -->

# セッション②

## Microsoft "Adaptive Cloud" Updates

**スピーカー：高添 修 氏**
<span class="speaker">日本マイクロソフト株式会社</span>

⏱️ 14:55 - 15:15（20分）

---

<!-- _class: lead -->

# Q&Aセッション

## 💬 ご質問をお待ちしています！

- チャットでの質問歓迎
- **匿名での質問も可能**
- どんな質問でもOK！

⏱️ 15:15 - 15:25（10分）

---

<!-- _class: lead -->

# 次回予告

## 📅 次回は9月12日（金）14:00〜

毎月第2金曜日に開催！

**YouTubeチャンネル登録**をお忘れなく！
https://www.youtube.com/channel/UCrf4bEl7yJnkGYo3F67gA7w

---

<!-- _class: lead -->

![bg left:28% 82%](../Images/hcc-logo02f.png)

# ご参加ありがとうございました！

## また来月お会いしましょう！

🎯 本日の資料は後日公開予定
📧 お問い合わせは ebibibi@gmail.com まで

**#HCCJP** でツイートお願いします！