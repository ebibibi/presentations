# HCCJP 第72回勉強会

## 開催情報

- **日時**: 2026年4月10日（金）14:00-15:30
- **形式**: オンライン（YouTube Live）
- **テーマ**: AIエージェントに Azure を教える — Microsoft公式 Agent Skills を読み解く

## 概要

AIコーディングエージェント（Claude Code / GitHub Copilot / Codex 等）が当たり前になった今、
Microsoftは公式に「AIエージェントにAzureの知識を教える」ためのスキル集を3つのリポジトリで公開しています。

132個のSDK開発スキル、192個のAzureサービス百科事典、そして200+のツールを持つ統合プラグイン。
これらを読み解くことで、「AIエージェントがAzureインフラを設計・構築・運用する時代」の全体像が見えてきます。

今回はこれらの公式リポジトリの中身を深掘りし、何が提供されているのか、
どう使えるのか、そしてハイブリッドクラウドの文脈でどんな意味を持つのかを解説します。

## セッション内容

### 1. AIエージェントに Azure を教える — Microsoft公式 Agent Skills を読み解く

胡田 昌彦（日本ビジネスシステムズ株式会社）

- AIコーディングエージェントの現状（軽く）
- Microsoft公式 Agent Skills の3リポジトリ構造
  - **microsoft/skills** — SDK×言語別の実装スキル（132個）
  - **MicrosoftDocs/Agent-Skills** — Azureサービス全体の百科事典（192個）
  - **microsoft/azure-skills** — 統合プラグイン（スキル＋Azure MCP Server＋Foundry MCP）
- 注目スキルの深掘り
  - azure-prepare → azure-validate → azure-deploy の3ステップワークフロー
  - entra-agent-id（AIエージェントにOAuthアイデンティティを与える）
  - cloud-solution-architect（44の設計パターン）
  - microsoft-foundry（AI Foundry統合）
- デモ: azure-skills プラグインで実際にAzureリソースを操作
- 考察: AIエージェントがインフラを操作する時代に何が変わるか

### 2. Microsoft "Adaptive Cloud" 最新動向

高添 修 氏（日本マイクロソフト株式会社）

Microsoft高添さんからは毎月恒例のMicrosoft "Adaptive Cloud" の最新動向をお伝えいただきます！
Azure Local、Azure Arc、Windows Server関連の最新情報をお見逃しなく！

## スピーカー

- **胡田 昌彦** - 日本ビジネスシステムズ株式会社、Microsoft MVP for Cloud and Datacenter Management, Microsoft Azure
- **高添 修 氏** - 日本マイクロソフト株式会社

## タイムテーブル

| 時刻 | 時間 | セッション | スピーカー |
|------|------|------------|------------|
| 14:00 | 5分 | オープニング | 胡田 昌彦 |
| 14:05 | 40分 | AIエージェントに Azure を教える — Microsoft公式 Agent Skills を読み解く | 胡田 昌彦 |
| 14:45 | 10分 | Q&A | 全員 |
| 14:55 | 20分 | Microsoft "Adaptive Cloud" Updates | 高添 修 氏 |
| 15:15 | 10分 | Q&A | 全員 |
| 15:25 | 5分 | クロージング | 胡田 昌彦 |

## 視聴方法

- **YouTube Live**: TBD
- チャンネル登録をお願いします！

## 参考リンク

- [microsoft/skills](https://github.com/microsoft/skills) — SDK開発スキル集（132個）
- [MicrosoftDocs/Agent-Skills](https://github.com/MicrosoftDocs/Agent-Skills) — Azureサービス百科事典（192個）
- [microsoft/azure-skills](https://github.com/microsoft/azure-skills) — 統合プラグイン
- [Announcing the Azure Skills Plugin](https://devblogs.microsoft.com/all-things-azure/announcing-the-azure-skills-plugin/) — 公式ブログ
- [Context-Driven Development: Agent Skills for Microsoft Foundry and Azure](https://devblogs.microsoft.com/all-things-azure/context-driven-development-agent-skills-for-microsoft-foundry-and-azure/) — 公式ブログ
- [Skill Explorer](https://microsoft.github.io/skills/) — 全スキル一覧（1-click install）

## 主催

ハイブリッドクラウド研究会（HCCJP）

**主幹事**: 日本ビジネスシステムズ株式会社

**幹事**（50音順）:
- NTTコミュニケーションズ株式会社
- 日商エレクトロニクス株式会社
- 日本ヒューレット・パッカード株式会社
- 日本マイクロソフト株式会社
- VistaNet株式会社
- 株式会社ネットワールド
- 三井情報株式会社
- レノボ・エンタープライズ・ソリューションズ株式会社
