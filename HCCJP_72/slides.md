---
marp: true
theme: default
paginate: true
header: "HCCJP 第72回勉強会 | 2026年4月10日"
footer: "ハイブリッドクラウド研究会"
---

# AIエージェントに Azure を教える

## Microsoft公式 Agent Skills を読み解く

**HCCJP 第72回勉強会**
2026年4月10日（金）

胡田 昌彦
日本ビジネスシステムズ株式会社
Microsoft MVP for Cloud and Datacenter Management, Microsoft Azure

---

# 本日のアジェンダ

| 時刻 | セッション | スピーカー |
|------|-----------|-----------|
| 14:00 | オープニング | 胡田 |
| 14:05 | **AIエージェントに Azure を教える** | 胡田 |
| 14:45 | Q&A | 全員 |
| 14:55 | **Microsoft "Adaptive Cloud" Updates** | 高添 氏 |
| 15:15 | Q&A → クロージング | 全員 |

---

# HCCJPとは

- **Hybrid Cloud Community Japan**
- 2018年から続く勉強会コミュニティ
- ハイブリッドクラウドに関する知見を共有
- 毎月第2金曜日 14:00〜 オンライン開催

**主幹事:** 日本ビジネスシステムズ株式会社
**幹事:** NTTコミュニケーションズ、日商エレクトロニクス、日本HP、日本マイクロソフト、VistaNet、ネットワールド、三井情報、レノボ

---

<!-- _class: lead -->

# セッション①
## AIエージェントに Azure を教える
## — Microsoft公式 Agent Skills を読み解く

---

# AIコーディングエージェントの現在地

- **Claude Code** / **GitHub Copilot** / **OpenAI Codex** ...
- コードを書くだけでなく、**インフラの設計・構築・運用**まで
- でも「Azure の正しい使い方」を知らないと...
  - 古いAPIを使う、ベストプラクティスに反する、セキュリティリスク

**→ AIエージェントに「正しいAzureの知識」を教える必要がある**

---

# Agent Skills とは？（30秒で）

- **AIエージェントに専門知識を与えるmarkdownファイル群**
- LLMは事前学習で知識を持っているが、適切なコンテキストがないと活性化できない
- スキル = そのトリガー（activation context）

```
.github/skills/
├── azure-ai-projects-py/
│   └── SKILL.md          ← これがスキル本体
├── azure-cosmos-py/
│   └── SKILL.md
└── ...
```

---

# Microsoft公式: 3つのリポジトリ

| リポジトリ | 役割 | スキル数 |
|-----------|------|---------|
| **microsoft/skills** | SDK×言語別の実装スキル | 132 |
| **MicrosoftDocs/Agent-Skills** | Azureサービスの百科事典 | 192 |
| **microsoft/azure-skills** | 統合プラグイン | 20+MCP |

**3つは「レイヤーが違う」**
- skills = コードの書き方を教える
- Agent-Skills = サービスの知識を教える
- azure-skills = 知識＋実行能力をセットで提供

---

# ① microsoft/skills（⭐1,900+）

**「このSDKのコードをどう書くか」を教えるスキル**

| 言語 | 数 | 例 |
|------|-----|-----|
| Core（共通） | 9 | cloud-solution-architect, mcp-builder, entra-agent-id |
| Python | 41 | azure-ai-projects-py, azure-cosmos-py |
| .NET | 28 | azure-ai-openai-dotnet, azure-search-documents-dotnet |
| TypeScript | 25 | azure-ai-projects-ts, azure-storage-blob-ts |
| Java | 25 | azure-ai-projects-java, azure-cosmos-java |
| Rust | 7 | （新規追加中） |

---

# ① microsoft/skills — カテゴリ分類

| カテゴリ | 内容 |
|---------|------|
| **foundry** | AI agents, projects, inference, search |
| **data** | Storage, Cosmos DB, Tables |
| **messaging** | Event Hubs, Service Bus, Event Grid |
| **monitoring** | OpenTelemetry, App Insights |
| **identity** | Authentication, credentials |
| **security** | Key Vault |
| **integration** | API Management, App Configuration |
| **compute** | Container Apps, Functions |
| **m365** | Microsoft Graph, Teams |

---

# ① 注目スキル: entra-agent-id

**AIエージェントにOAuth2アイデンティティを持たせる** 🆕

- Microsoft Entra Agent ID（Preview）
- AIエージェント専用のサービスプリンシパル
- Graph API 経由で作成・管理
- Blueprints / BlueprintPrincipals / WIF

**→ エージェントが「自分の権限」でAzureリソースにアクセスする時代**

---

# ① 注目スキル: cloud-solution-architect

**44のアーキテクチャ設計パターンをエージェントに教える**

- Well-Architected Framework の5本柱
- アーキテクチャスタイル選定
- ミッションクリティカル設計
- テクノロジー選択のガイドライン

**→ 「どのサービスを使うべきか？」の判断をAIが支援**

---

# ② MicrosoftDocs/Agent-Skills（⭐450+）

**「Azureの各サービスについて何を知るべきか」の百科事典**

192個のスキルが **19カテゴリ** に分類:

| カテゴリ | 例 |
|---------|-----|
| 🤖 AI + ML | Azure AI Foundry, AI Search, Document Intelligence, Speech |
| ☁️ Compute | Functions, VM, Container Apps, AKS |
| 🗄️ Databases | Cosmos DB, SQL Database, PostgreSQL |
| 🔒 Security | Key Vault, DDoS Protection, Firewall |
| 🌐 Networking | VNet, Load Balancer, Front Door |
| 🌍 Hybrid + Multicloud | **Azure Arc, Azure Local, Stack HCI** |

---

# ② 各スキルに含まれる知識

1つのスキルに含まれる情報カテゴリ:

- **Troubleshooting** — よくある問題と解決策
- **Best Practices** — 推奨パターン
- **Decision Making** — 「どんな時にこのサービスを選ぶか」
- **Architecture & Design Patterns** — 設計パターン
- **Limits & Quotas** — 制限事項（これ重要！）
- **Security** — セキュリティ考慮事項
- **Configuration** — 設定のベストプラクティス
- **Integrations & Coding Patterns** — 連携パターン
- **Deployment** — デプロイ手順

---

# ② HCCJPメンバー注目: Hybrid + Multicloud

| スキル | 説明 |
|-------|------|
| **azure-arc** | Azure Arc でマルチクラウド/オンプレを統合管理 |
| **azure-aks-edge-essentials** | エッジでのKubernetes |
| **azure-stack-edge** | Azure Stack Edge デバイス |
| **microsoft-foundry-local** | Foundry をローカルで実行 |

**→ 前回（第71回）のテーマ「AI時代のハイブリッドクラウド」の延長線上にある**

---

# ② azure-arc スキルの深さ（実例）

**9カテゴリ × 数十トピック** が1つのスキルに凝縮:

| カテゴリ | トピック数 | 例 |
|---------|----------|-----|
| Troubleshooting | 20+ | Kubernetes/Servers/SQL MI/Resource Bridge |
| Security | 59行分 | RBAC, AD/Entra auth, TDE, Private Link |
| Configuration | 100行分 | GitOps, Extensions, Key Vault, 監視 |
| Deployment | 30行分 | Data controllers, Edge RAG, SCVMM |

**AIエージェントが「Arcの専門家」になれるだけの知識量**

---

# ② 重要な発見: ハイブリッド系のカバー格差 🔴

| リポジトリ | Arc | Local | Foundry Local |
|-----------|-----|-------|---------------|
| **MicrosoftDocs/Agent-Skills** | ✅ 充実 | ✅ 充実 | ✅ あり |
| **microsoft/skills** | ❌ なし | ❌ なし | ❌ なし |
| **microsoft/azure-skills** | ❌ なし | ❌ なし | ❌ なし |

- SDK開発スキル・統合プラグインは **クラウドネイティブ寄り**
- ハイブリッド/エッジの知識は **MicrosoftDocs/Agent-Skills だけ**
- → **ハイブリッドクラウドの仕事をAIにさせるなら、このリポジトリが必須**

---

# ③ microsoft/azure-skills（⭐560+）

**「知識＋実行能力」を1パッケージで提供する統合プラグイン**

## 3層構造

| 層 | 役割 |
|----|------|
| **Skills（脳）** | 20個のキュレート済みスキル — ワークフロー、判断基準、ガードレール |
| **Azure MCP Server（手）** | 200+ツール × 40+サービス — リソース操作、価格確認、ログ照会 |
| **Foundry MCP（AI専門家）** | モデルカタログ、デプロイ、エージェントワークフロー |

---

# ③ azure-skills の主要スキル

| スキル | 役割 |
|-------|------|
| **azure-prepare** | デプロイ前の設計・準備 |
| **azure-validate** | 構成の検証・チェック |
| **azure-deploy** | 実際のデプロイ実行 |
| **azure-diagnostics** | トラブルシューティング |
| **azure-cost-optimization** | コスト最適化 |
| **azure-compliance** | コンプライアンスチェック |
| **azure-rbac** | 権限管理 |
| **microsoft-foundry** | AI Foundry統合 |
| **entra-app-registration** | アプリ登録 |

**→ prepare → validate → deploy の3ステップが設計されている**

---

# ③ ワンクリックインストール

```bash
# GitHub Copilot CLI
/plugin marketplace add microsoft/azure-skills
/plugin install azure@azure-skills

# Claude Code
/plugin marketplace add microsoft/azure-skills
/plugin install azure@azure-skills
```

**エージェントを選ばない。同じスキルが Copilot でも Claude Code でも動く。**

---

<!-- _class: lead -->

# デモ

## azure-skills プラグインで
## 実際にAzureリソースを操作してみる

---

# 3つのリポジトリの使い分け

```
あなたの開発プロジェクト
│
├── 「Cosmos DB の Python コード書いて」
│   └── → microsoft/skills の azure-cosmos-py が活躍
│
├── 「Container Apps のベストプラクティスは？」
│   └── → MicrosoftDocs/Agent-Skills の azure-container-apps が活躍
│
└── 「このアプリを Azure にデプロイして」
    └── → microsoft/azure-skills の prepare→validate→deploy が活躍
```

---

# まとめ: 何が変わるのか？

## Before（従来）
- 人間が Azure のドキュメントを読む
- 人間が設計・構築・運用する
- AIは「コード補完」だけ

## After（Agent Skills 時代）
- AIエージェントが Azure の知識を持つ
- AIエージェントが設計・構築・運用を支援する
- 人間は「判断」と「承認」に集中する

**→ インフラエンジニアの役割は「作る人」から「判断する人」へ**

---

# 参考リンク

- [microsoft/skills](https://github.com/microsoft/skills) — SDK開発スキル集
- [MicrosoftDocs/Agent-Skills](https://github.com/MicrosoftDocs/Agent-Skills) — Azureサービス百科事典
- [microsoft/azure-skills](https://github.com/microsoft/azure-skills) — 統合プラグイン
- [Skill Explorer](https://microsoft.github.io/skills/) — 全スキル一覧
- [Announcing the Azure Skills Plugin](https://devblogs.microsoft.com/all-things-azure/announcing-the-azure-skills-plugin/)
- [Context-Driven Development](https://devblogs.microsoft.com/all-things-azure/context-driven-development-agent-skills-for-microsoft-foundry-and-azure/)

---

<!-- _class: lead -->

# ありがとうございました！

### Q&A

Slido / YouTube チャットで質問をどうぞ 🙋

---

<!-- _class: lead -->

# セッション②
## Microsoft "Adaptive Cloud" 最新動向

高添 修 氏
日本マイクロソフト株式会社

---

# クロージング

## 次回: HCCJP 第73回勉強会
- **日時**: 2026年5月8日（金）14:00〜（予定）
- **テーマ**: TBD

## フォローお願いします！
- YouTube: チャンネル登録
- Connpass: HCCJP
- X: @HCCJP

**ご参加ありがとうございました！🎉**
