# HCCJP 第72回勉強会

## 開催情報

- **日時**: 2026年4月10日（金）14:00-15:30
- **形式**: オンライン（YouTube Live）
- **テーマ**: AIエージェントに Azure を教える — Microsoft公式 Agent Skills を読み解く

## 概要

毎月第2金曜日14時からはHCCJPの勉強会！4月は「Microsoft公式 Agent Skills」をテーマにお届けします！

Claude Code、GitHub Copilot、OpenAI Codex… AIコーディングエージェントは「コードを書く」だけではなく、**インフラの設計・構築・運用まで担う時代**になりました。でも、エージェントは本当にAzureの正しい使い方を知っているでしょうか？

古いAPIを使ってしまう。ベストプラクティスに反した構成を作る。セキュリティの考慮が足りない構成をデプロイしてしまう——そんな経験をした方も多いのではないでしょうか。

この課題に対して、Microsoftは公式に「AIエージェントにAzureの知識を教える」ためのスキル集を**3つのGitHubリポジトリ**で公開しています。合計300以上のスキルと200以上のツール。AIエージェントがAzureインフラを正しく扱うための基盤が、いま急速に整いつつあります。

本セッションでは、これら3つのリポジトリの中身を深掘りし、何が提供されているのか、どう使えるのか、そして**ハイブリッドクラウドの文脈でどんな意味を持つのか**を解説します。Azure Local や Azure Arc のスキルはどこまでカバーされているのか？——HCCJPメンバーなら気になるこのポイントも、しっかり読み解きます！

## セッション内容

### 1. AIエージェントに Azure を教える — Microsoft公式 Agent Skills を読み解く

**胡田 昌彦**

Microsoft公式の3つのAgent Skillsリポジトリを読み解き、AIエージェント × Azure の全体像を解説します。

- **Part 1**: AIコーディングエージェントの現在地 — コード補完からインフラ運用へ
- **Part 2**: 3つのリポジトリの構造 — microsoft/skills（SDK開発支援、132 skills）、microsoft/azure-skills（運用支援、24 skills + 2 MCP）、MicrosoftDocs/Agent-Skills（サービス知識の百科事典、192 skills）
- **Part 3**: 注目スキルの深掘り — prepare→validate→deployの3ステップ、entra-agent-id、cloud-solution-architect
- **Part 4**: ハイブリッドクラウド視点での分析 — Azure Local / Azure Arc スキルのカバー状況と現状の課題
- **Part 5**: デモ — azure-skills プラグインで実際にAzureリソースを操作
- **Part 6**: 考察 — AIエージェントがインフラを操作する時代にエンジニアは何をすべきか

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
| 15:15 | 10分 | Q&A | 高添 修 氏 |
| 15:25 | 5分 | クロージング | 胡田 昌彦 |

## 参考リンク

- [microsoft/skills](https://github.com/microsoft/skills) — SDK開発支援（132 skills）
- [microsoft/azure-skills](https://github.com/microsoft/azure-skills) — 運用支援（24 skills + 2 MCP）
- [MicrosoftDocs/Agent-Skills](https://github.com/MicrosoftDocs/Agent-Skills) — サービス知識の百科事典（192 skills）
- [Skill Explorer](https://microsoft.github.io/skills/) — 全スキル一覧（1-click install）
- [Announcing the Azure Skills Plugin](https://devblogs.microsoft.com/all-things-azure/announcing-the-azure-skills-plugin/) — 公式ブログ
- [Context-Driven Development](https://devblogs.microsoft.com/all-things-azure/context-driven-development-agent-skills-for-microsoft-foundry-and-azure/) — 公式ブログ

## 視聴方法

- **YouTube Live**: TBD
- チャンネル登録してお待ちください！

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
