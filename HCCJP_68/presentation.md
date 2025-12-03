---
marp: true
theme: gaia
paginate: true
backgroundColor: #fff
style: |
  section {
    font-family: 'Meiryo', 'Segoe UI', sans-serif;
    font-size: 32px;
  }
  h1 {
    color: #0078d4;
    font-size: 1.5em;
  }
  h2 {
    color: #0078d4;
    font-size: 1.3em;
  }
  h3 {
    font-size: 1.1em;
  }
  .speaker {
    font-size: 0.8em;
    color: #666;
  }
  table {
    font-size: 0.7em;
  }
  th {
    background-color: #0078d4;
    color: white;
  }
  code {
    font-size: 0.85em;
    background-color: #f5f5f5;
  }
  li {
    font-size: 0.9em;
    margin-bottom: 0.3em;
  }
  /* コンテンツが多いスライド用 */
  section.small {
    font-size: 26px;
  }
  section.small h1 {
    font-size: 1.3em;
  }
  section.small h2 {
    font-size: 1.1em;
  }
  section.small li {
    font-size: 0.9em;
  }
  /* さらに小さいスライド用 */
  section.x-small {
    font-size: 22px;
  }
  section.x-small h1 {
    font-size: 1.2em;
  }
  section.x-small h2 {
    font-size: 1.0em;
  }
  section.x-small li {
    font-size: 0.88em;
  }
  /* leadクラス用 */
  section.lead {
    text-align: center;
  }
  section.lead h1 {
    font-size: 1.8em;
  }
  section.lead h2 {
    font-size: 1.4em;
  }
---

<!-- _class: lead -->

![bg right:30% 80%](../Images/ebi/アセット9.png)

# Ignite 注目ポイント

## 全体サマリー & AIエージェント編

**胡田 昌彦**（日本ビジネスシステムズ株式会社 / Microsoft MVP）

HCCJP 第68回勉強会
2025年12月12日

---

# アジェンダ

Microsoft Ignite 2025 の注目ポイント

1. **Ignite 2025 全体の傾向**
2. **AIエージェントの最新動向**
3. **まとめ**

⏱️ 約30分

---

<!-- _class: lead -->

# AIエージェント時代の到来

## 人間と同じようにAIエージェントを管理する

---

<!-- _class: small -->

# なぜAIエージェントにIDが必要なのか？

## これまでのMicrosoftのID管理の考え方

### 一貫した方針：すべてのアクセス主体にIDを
- **人間（ユーザー）**: Entra IDでID管理
- **アプリケーション**: サービスプリンシパル / マネージドID
- **デバイス**: デバイスID / Intune管理
- **そしてAIエージェント**: **Microsoft Entra Agent ID** 🆕

### Zero Trustの原則
> 「誰が」「何を」「どこから」アクセスしているか常に検証

**AIエージェントも例外ではない**

---

<!-- _class: small -->

# Microsoft Entra Agent ID

## AIエージェントを「一級市民」として管理

### 主要な機能
- **エージェントの発見と登録**
  - シャドーエージェントを含むすべてのAIエージェントを発見
  - 一意のIDを割り当て、完全なインベントリを維持

- **Agent Registry（エージェントレジストリ）**
  - 組織内のすべてのAIエージェントの「唯一の情報源」
  - 作成者、実行場所、機能、ガバナンスポリシーを管理

- **ライフサイクル管理**
  - 作成・更新・無効化を自動化
  - アクセスパッケージで意図的・監査可能・期限付きのアクセスを実現

> **ポイント**: Copilot Studioだけでなく、**非Microsoftエコシステム**のエージェントも管理対象

---

# Agent 365

## AIエージェントのコントロールプレーン

| 機能 | 説明 |
|------|------|
| **Registry** | エージェントの一元管理・単一の情報源 |
| **Access Control** | リソースへのアクセス制限 |
| **Visualization** | 統合ダッシュボード・分析 |
| **Interoperability** | 人間とエージェントのワークフロー連携 |
| **Security** | 脅威からエージェントを保護 |

### ハイブリッド/マルチクラウド対応
- **Copilot Studio / Microsoft Foundry**だけでなく
- **パートナーエコシステム**のエージェントも統合管理
- AWS、GCP、オンプレミスで動作するエージェントも対象

---

<!-- _class: small -->

# セキュリティとガバナンス

## Zero Trustをエージェントにも適用

### Conditional Access の拡張
- AIエージェントにも条件付きアクセスポリシーを適用
- リスクの高いエージェントをブロック
- ネットワーク制御で悪意あるリソースへのアクセスを防止

### データ保護 (Microsoft Purview)
- **Purview DLP for Copilot**: 機密データを含むプロンプトをブロック
- クレジットカード番号や個人情報の漏洩を防止

### Security Copilotとの連携
- Microsoft 365 E5にSecurity Copilotを含む
- Defender、Entra、Intune、Purviewに12の新エージェントを組み込み

---

<!-- _class: lead -->

# 3つの「IQ」

## AIエージェントを支えるインテリジェンス層

---

<!-- _class: small -->

# Work IQ

## Microsoft 365 Copilotの頭脳

### あなたの仕事を理解する
- **データ**: メール、ファイル、会議、チャットなど組織・個人データに接続
- **メモリ**: 好み、習慣、ワークフローを学習・記憶
- **推論**: 洞察を提供し、ニーズを予測、タスクを先回りして実行

### 新機能
- **会話メモリ**: セッション間でコンテキストを保持
- **SharePointメタデータ推論**: 構造化メタデータで正確な回答（GA）

> 3つの新エージェント: Workforce Insights、People、Learning Agent

---

<!-- _class: small -->

# Fabric IQ

## ビジネスデータのインテリジェンス層

### Microsoft Fabricと統合（プレビュー）
- Power BIの統一セマンティックレイヤーをビジネス運用に拡張
- **2,000万以上のモデル**に対応

### 何ができる？
- 分析データ、時系列データ、位置データを統合
- 運用システムとビジネス意味を紐づけ
- **リアルタイム**で人間とAIが行動可能な「ライブビュー」を提供

> データ分析・ガバナンス・インサイトのためのインテリジェンス

---

<!-- _class: small -->

# Foundry IQ

## 従来のRAGから次世代RAGへ

| | 従来のRAG | Foundry IQ（次世代RAG） |
|------|----------|----------------------|
| **検索** | キーワード/ベクトル検索 | コンテキストエンジニアリング |
| **グラウンディング** | 単純な文書参照 | 意味理解に基づく根拠付け |
| **精度** | ハルシネーションが課題 | 大幅に削減 |
| **基盤** | 個別実装 | Azure AI Search統合 |

### Foundry IQの位置づけ
- **RAGの進化形**として、より正確で信頼性の高い応答を実現
- カスタムAIエージェント構築のための開発者向けインテリジェンス

> 現在プレビュー提供中

---

# 3つのIQの関係

## Microsoft Agent Factory

| IQ | 対象 | 役割 |
|------|------|------|
| **Work IQ** | エンドユーザー | 仕事・組織・個人を理解 |
| **Fabric IQ** | ビジネスデータ | データ統合・分析・ガバナンス |
| **Foundry IQ** | 開発者 | エージェント構築・RAG強化 |

### Agent Factory
- 3つのIQを統合したエージェント構築プログラム
- **単一の従量課金プラン**でMicrosoft Foundry / Copilot Studioを利用
- 初期ライセンス・プロビジョニング不要でエージェント展開

---

<!-- _class: lead -->

# AI開発プラットフォームの選択肢

## どこでエージェントを構築・実行するか？

---

<!-- _class: x-small -->

# AI開発プラットフォームの比較

| 観点 | Microsoft 365 Copilot | Copilot Studio | Azure AI Foundry | Azure（モデルのみ） | 非Microsoft |
|------|---------------------|----------------|-----------------|------------------|-------------|
| **対象者** | エンドユーザー | ビジネスユーザー | 開発者/DS | 開発者 | 開発者 |
| **開発手法** | 利用のみ | ローコード | コードファースト | フルコード | フルコード |
| **M365統合** | ネイティブ | シームレス | API経由 | なし | なし |
| **ガバナンス** | 組み込み | Power Platform | Azure RBAC | Azure RBAC | 自前構築 |
| **モデル選択** | 固定 | 限定的 | 11,000+ | 11,000+ | 任意 |
| **カスタマイズ** | 低 | 中 | 高 | 最高 | 最高 |
| **立ち上げ速度** | 即時 | 数日 | 数週間 | 数週間〜 | 数ヶ月〜 |

---

<!-- _class: small -->

# 各プラットフォームの位置づけ

## SaaS → PaaS → IaaS/自前構築

### Microsoft 365 Copilot（SaaS）
- すぐ使える完成品、カスタマイズは限定的

### Copilot Studio（ローコードPaaS）
- ビジネスユーザー向け、M365との統合が強み
- ガバナンス（DLP、監査ログ、コンプライアンス）が組み込み

### Azure AI Foundry / Microsoft Foundry（コードファーストPaaS）
- 開発者向け、11,000+モデルへのアクセス
- OpenAI + Anthropic両方を提供する唯一のクラウド

### Azureモデルのみ利用（IaaS的）
- フル制御、Microsoftエコシステムは使わない

### 完全非Microsoft（オンプレ/他クラウド）
- すべて自前構築、最大の自由度と責任

---

<!-- _class: small -->

# 推奨アーキテクチャ

## フロントエンド/バックエンドパターン

```
┌─────────────────────────────────────────────────────┐
│  ユーザー（Teams / Web / Mobile）                    │
└─────────────────────┬───────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────┐
│  Copilot Studio（フロントエンド）                    │
│  - 会話UI、ユーザー対応、簡易ロジック                │
└─────────────────────┬───────────────────────────────┘
                      ↓ 複雑なタスクをルーティング
┌─────────────────────────────────────────────────────┐
│  Azure AI Foundry（バックエンド）                    │
│  - 高度な推論、カスタムモデル、マルチエージェント    │
└─────────────────────────────────────────────────────┘
```

> **ベストプラクティス**: 多くの組織は両方を併用
> Copilot Studioでプロトタイプ → Azure AI Foundryで本番構築

---

<!-- _class: x-small -->

# 参考文献

### Microsoft公式ドキュメント
- **Microsoft Entra Ignite 2025: Key Announcements and Updates**
  [https://learn.microsoft.com/en-us/entra/fundamentals/whats-new-ignite-2025](https://learn.microsoft.com/en-us/entra/fundamentals/whats-new-ignite-2025)

- **Riding the AI Wave: How Microsoft Entra is Evolving for the Agentic Era**
  [https://techcommunity.microsoft.com/blog/microsoft-entra-blog/riding-the-ai-wave-how-microsoft-entra-is-evolving-for-the-agentic-era/4460536](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/riding-the-ai-wave-how-microsoft-entra-is-evolving-for-the-agentic-era/4460536)

- **Microsoft Ignite 2025: Copilot and agents built to power the Frontier Firm**
  [https://www.microsoft.com/en-us/microsoft-365/blog/2025/11/18/microsoft-ignite-2025-copilot-and-agents-built-to-power-the-frontier-firm/](https://www.microsoft.com/en-us/microsoft-365/blog/2025/11/18/microsoft-ignite-2025-copilot-and-agents-built-to-power-the-frontier-firm/)

- **Ambient and autonomous security for the agentic era**
  [https://www.microsoft.com/en-us/security/blog/2025/11/18/ambient-and-autonomous-security-for-the-agentic-era/](https://www.microsoft.com/en-us/security/blog/2025/11/18/ambient-and-autonomous-security-for-the-agentic-era/)

---

<!-- _class: lead -->

![bg left:30% 80%](../Images/ebi/アセット9.png)

# ご清聴ありがとうございました！

## 質問・コメントをお待ちしています

**#HCCJP でシェアお願いします！**

