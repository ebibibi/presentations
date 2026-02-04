# HCCJP 第70回勉強会

## 開催情報

- **日時**: 2026年2月13日（金）14:00-15:30
- **形式**: オンライン（YouTube Live）
- **テーマ**: ローカルLLMでクラウドアプリもAI使い放題！NVIDIA DGX Spark × Azure ハイブリッド構成

## 概要

毎月第2金曜日14時からはHCCJPの勉強会！2月は「ローカルLLM × クラウドのハイブリッド構成」をテーマにお届けします！

クラウドLLMのAPI課金が気になる…そんな悩みを解決！**NVIDIA DGX Spark**をオンプレミスに設置してローカルLLMを動かせば、**AI使い放題**の環境が手に入ります。さらにAzure上のアプリケーションからシームレスに利用できるハイブリッド構成を、実践事例を交えてご紹介します。

ポイントはLiteLLM！Ollamaはv0.13.3以降でResponses API（/v1/responses）に対応していますが、stateful（previous_response_id / conversation）には未対応です。必要に応じてLiteLLMを挟むことで、OpenAI互換APIの統合（例：セッション継続やルーティング）を行い、Agent SDK/フレームワーク側の実装をシンプルにできます。

本セッションでは、Ollama、LiteLLMといったオープンソースツールを活用した統合的なLLM基盤の構築方法を学べます！

## セッション内容

### 1. ローカルLLMでクラウドアプリもAI使い放題！NVIDIA DGX Spark × Azure ハイブリッド構成

**NVIDIA DGX Spark**は128GB統合メモリを搭載したデスクトップサイズのAIスーパーコンピューター。これをオンプレミスに設置すれば、大規模LLMを**使い放題**で運用できます。Ollama + LiteLLMで統合的なLLM基盤を構築し、VPN経由でAzure上のアプリケーションから利用する「真のハイブリッドクラウド」構成を実践事例を交えてご紹介します。

- **NVIDIA DGX Spark**とは？128GB統合メモリの威力
- Ollama / LiteLLM によるローカルLLM環境の構築
- **LiteLLMでResponses API対応** → Agent SDKが動く！
- Azure × オンプレミスLLM ハイブリッド構成の実装

### 2. Microsoft "Adaptive Cloud" 最新動向

Microsoft高添さんからは毎月恒例のMicrosoft "Adaptive Cloud" の最新動向をお伝えいただきます！Azure Local、Azure Arc、Windows Server関連の最新情報をお見逃しなく！

## スピーカー

- **胡田 昌彦** - 日本ビジネスシステムズ株式会社、Microsoft MVP for Cloud and Datacenter Management, Microsoft Azure
- **高添 修 氏** - 日本マイクロソフト株式会社

## タイムテーブル

| 時刻 | 時間 | セッション | スピーカー |
|------|------|------------|------------|
| 14:00 | 5分 | オープニング | 胡田 昌彦 |
| 14:05 | 45分 | ローカルLLMでAI使い放題！NVIDIA DGX Spark × Azure | 胡田 昌彦 |
| 14:50 | 10分 | Q&A | 全員 |
| 15:00 | 20分 | Microsoft "Adaptive Cloud" Updates | 高添 修 氏 |
| 15:20 | 5分 | Q&A | 全員 |
| 15:25 | 5分 | クロージング | 胡田 昌彦 |
## 視聴方法

- **YouTube Live**: https://www.youtube.com/channel/UCrf4bEl7yJnkGYo3F67gA7w
- チャンネル登録をお願いします！

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
