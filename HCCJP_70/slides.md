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
    font-size: 1.8em;
  }
  h2 {
    color: #0078d4;
    font-size: 1.5em;
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
  section.lead h1 {
    font-size: 2.2em;
  }
  section.lead h2 {
    font-size: 1.8em;
  }
  section.lead .speaker {
    font-size: 1.0em;
  }
  section.point {
    font-size: 42px;
  }
  section.point h1 {
    font-size: 1.6em;
  }
  section.point h2 {
    font-size: 1.3em;
    color: #333;
  }
  .arch-box {
    font-family: monospace;
    font-size: 0.7em;
    line-height: 1.3;
    background: #f8f8f8;
    padding: 15px;
    border-radius: 8px;
  }
---

<!-- _class: lead -->

![bg right:30% 80%](../Images/hcc-logo02f.png)

# HCCJP 第70回勉強会

## ハイブリッドクラウド研究会

**2026年2月13日（金）14:00開始**

---

<!-- _class: lead -->

# ローカルLLMで
# クラウドアプリもAI使い放題！

## NVIDIA DGX Spark × Azure ハイブリッド構成

---

<!-- _class: lead -->

![bg right:30% 80%](../Images/hcc-logo02f.png)

# オープニング

**司会：胡田 昌彦**
<span class="speaker">日本ビジネスシステムズ株式会社<br>Microsoft MVP for Cloud and Datacenter Management, Microsoft Azure</span>

---

<!-- _class: x-small -->

# タイムテーブル

| 時刻 | 時間 | セッション | スピーカー |
|------|------|------------|------------|
| 14:00 | 5分 | オープニング | 胡田 昌彦（JBS / Microsoft MVP） |
| 14:05 | 45分 | ローカルLLMでAI使い放題！NVIDIA DGX Spark × Azure | 胡田 昌彦 |
| 14:50 | 10分 | Q&A | 匿名で何でも質問できます！ |
| 15:00 | 20分 | Microsoft "Adaptive Cloud" Updates | 高添 修 氏（日本マイクロソフト） |
| 15:20 | 5分 | Q&A | 何でも質問できます！ |
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

- 📹 配信は録画されています（アーカイブ視聴可）
- 💬 質問・コメント大歓迎！
- 📝 Q&Aセッションでまとめてお答えします

---

<!-- _class: x-small -->

# 質問・コメント方法

## 💬 YouTubeチャットで質問・コメント大歓迎！

- 右側のライブチャット欄から投稿してください
- セッション中でもお気軽にどうぞ
- 固定コメントに各種リンクを掲載します

---

<!-- _class: lead -->

# セッション①

## ローカルLLMでAI使い放題！
## NVIDIA DGX Spark × Azure

**胡田 昌彦**

⏱️ 14:05 - 14:50（45分）

---

<!-- _class: point -->

# 今日のゴール

## クラウドLLMのAPI課金、気になりませんか？

→ **ローカルLLM × クラウドのハイブリッド構成**で解決！

---

<!-- _class: lead -->

# Part 1
# NVIDIA DGX Spark

---

<!-- _class: point -->

# DGX Spark とは

- デスクトップサイズの**AIスーパーコンピュータ**
- **128GB統合メモリ**（CPU/GPU共有）
- **240W**でシステム全体が動く（省電力！）
- 価格: 国内70〜80万円台

---

<!-- _class: point -->

# 128GBメモリの威力

## 大規模モデルがローカルで動く

- 通常GPU: 24GB → 70Bモデルが限界
- DGX Spark: 128GB → **120Bモデルも余裕**

---

<!-- _class: lead -->

# Part 2
# ローカルLLM環境構築

---

<!-- _class: small -->

# 構成: Ollama + LiteLLM

<!-- 🎨 画像生成プロンプト:
Create a clean, modern technical architecture diagram showing the internal structure of NVIDIA DGX Spark (128GB unified memory).
Inside a rounded rectangle labeled "DGX Spark (128GB)", show two boxes side by side:
- Left box: "Ollama" (LLM Runtime) with model names: qwen3, llama3, gemma3
- Right box: "LiteLLM" (Unified Proxy) with features: Responses API, Session Management, Routing
An arrow from the right edge labeled "API Requests" points into LiteLLM, and an arrow from LiteLLM points to Ollama.
Style: flat design, blue (#0078d4) accent color, white background, no gradients, tech presentation style.
-->

<div class="arch-box">

```
┌─────────────────────────────────────────────────┐
│              DGX Spark (128GB)                   │
│                                                  │
│  ┌──────────┐    ┌────────────────┐              │
│  │  Ollama   │◄───│   LiteLLM      │◄── API      │
│  │ (LLM実行) │    │ (統合プロキシ)  │   リクエスト │
│  │           │    │                │              │
│  │ ・qwen3   │    │ ・Responses API│              │
│  │ ・llama3  │    │ ・セッション継続│              │
│  │ ・gemma3  │    │ ・ルーティング  │              │
│  └──────────┘    └────────────────┘              │
└─────────────────────────────────────────────────┘
```
</div>

---

<!-- _class: point -->

# Responses API とは？

## Chat Completions API との違い

| | Chat Completions | Responses API |
|---|---|---|
| 入出力 | Messages配列 | Items形式 |
| 状態管理 | **クライアント側** | **サーバー側** |
| 会話継続 | 毎回全履歴送信 | `previous_response_id` |
| ビルトインツール | なし | Web検索、ファイル検索等 |

→ **Agent SDKはResponses APIを前提に設計**

---

<!-- _class: point -->

# なぜ LiteLLM？

## Ollama + LiteLLM で統合・運用をシンプルに

- Ollama v0.13.3以降: `/v1/responses` 対応済み
- ただし **stateful（session継続）は未対応**
- LiteLLM: セッション継続、ルーティング、複数バックエンド統合

→ Agent SDK/フレームワークの実装がシンプルに！

---

<!-- _class: point -->

# LiteLLM の価値

- **100以上のLLMプロバイダー統合**
- **セッション継続**（previous_response_id対応）
- **自動フェイルオーバー/ルーティング**
- コストトラッキング、レート制限

→ ローカル × クラウドの**統合ハブ**として最適

---

<!-- _class: point -->

# 今回はヘッドレス構成

- DBなし、管理UIなし
- **設定ファイル1つで完結**
- シンプルに統合APIだけ使いたい用途に最適

---

<!-- _class: lead -->

# Part 3
# Azure × オンプレ ハイブリッド

---

<!-- _class: small -->

# 全体構成

<!-- 🎨 画像生成プロンプト:
Create a professional network architecture diagram showing a hybrid cloud setup:
LEFT SIDE (labeled "Azure Cloud", blue background):
- "Azure App Service (Private Miner)" box at top
- "Azure OpenAI (Pay-per-use)" box at bottom
- A dashed arrow labeled "Fallback" from App Service to Azure OpenAI
RIGHT SIDE (labeled "On-Premises", green background):
- "DGX Spark" box containing "Ollama + LiteLLM"
- Below it: "https://spark.xxx.ts.net"
CONNECTION between sides:
- Solid arrow from Azure App Service to DGX Spark, labeled "Tailscale Funnel (HTTPS)"
Style: clean flat design, two-tone (blue for cloud, green for on-prem), white background, suitable for tech presentation. No 3D effects.
-->

<div class="arch-box">

```
┌── Azure ──────────────┐     ┌── オンプレミス ──────────┐
│                        │     │                          │
│  ┌──────────────────┐  │     │  ┌──────────────────┐    │
│  │  Azure App Service│  │     │  │   DGX Spark       │    │
│  │  (Private Miner)  │──┼─────┼─▶│   Ollama+LiteLLM  │    │
│  └──────────────────┘  │     │  └──────────────────┘    │
│           │             │     │         ▲                │
│           │ Fallback    │     │         │ Tailscale      │
│           ▼             │     │         │ Funnel         │
│  ┌──────────────────┐  │     │         │                │
│  │  Azure OpenAI     │  │     │  https://spark.xxx.ts.net│
│  │  (従量課金)       │  │     │                          │
│  └──────────────────┘  │     └──────────────────────────┘
└────────────────────────┘
```
</div>

---

<!-- _class: point -->

# Tailscale Funnel

## VPNなしでインターネット公開

```
tailscale funnel --bg 8080
```

→ `https://spark.xxx.ts.net` で公開

---

<!-- _class: point -->

# フェイルオーバー構成

<!-- 🎨 画像生成プロンプト:
Create a simple failover flow diagram:
1. "API Request" arrow enters from the left
2. First node: "DGX Spark (Primary)" with label "Free / Unlimited" - highlighted in green
3. If DGX Spark fails (red X mark), arrow goes down to:
4. Second node: "Azure OpenAI (Fallback)" with label "Pay-per-use" - highlighted in blue
5. Both nodes have an arrow pointing right to "Response"
Style: flowchart style, clean, minimal, green for primary path, blue for fallback path, white background.
-->

1. **Primary**: DGX Spark（使い放題）
2. **Fallback**: Azure OpenAI（従量課金）

→ ローカル障害時も継続稼働

---

<!-- _class: point -->

# 実際のシステム: Private Miner

- Azure App Service で稼働
- 社内ドキュメントからナレッジ抽出
- **データを外に出さずにAI活用**

---

<!-- _class: lead -->

# 苦労話

---

<!-- _class: point -->

# リモートデスクトップで5時間溶かした

- 設定アプリがハングアップ
- RDP証明書エラー
- **Wi-Fi経由だと繋がらない**（有線固定で解決）

教訓: **tcpdumpでSYN確認が最強の切り分け**

---

<!-- _class: point -->

# apt更新でGPGキー期限切れ

- NVIDIA Workbenchの署名が期限切れ
- GPGキーを手動更新で解決

---

<!-- _class: point -->

# nvidia-smi エラー

- DGX Dashboardから「Update」したら動かなくなった
- **再起動で解決**（ドライバ更新後は再起動必要）

---

<!-- _class: lead -->

# 🎬 デモ

---

<!-- _class: point -->

# デモ内容

1. **DGX Spark の状態確認**
   - nvidia-smi、ollama list、systemctl status

2. **LiteLLM API を叩く**
   - curlでリクエスト → ローカルLLMが応答

3. **Private Miner 診断UI**
   - /diagnostics で接続状態確認

---

<!-- _class: lead -->

# 🎬 デモ開始！

---

<!-- _class: lead -->

# バイブコーディングの話

---

<!-- _class: point -->

# 全部 Claude Code で作った

- Private Miner アプリ全体
- Azure インフラ（Bicep、CI/CD）
- DGX Spark 環境構築
- **このスライドも**
- connpass イベント概要
- サムネイル画像

---

<!-- _class: point -->

# でもAIだけでは作れなかったもの

- 「ローカルLLM × Azure」という**発想**
- 「LiteLLMで統合する」という**要件発見**
- 「Tailscale Funnelで公開」という**設計判断**

## AIは「How」を実装、「What」を決めるのは人間

---

<!-- _class: point -->

# まとめ

1. **DGX Spark**: 120Bモデルがローカルで動く
2. **LiteLLM**: 統合・ルーティング・セッション継続
3. **Tailscale Funnel**: 簡単にインターネット公開
4. **フェイルオーバー**: Azure OpenAIと連携

**ローカルLLM × クラウドの真のハイブリッド**

---

<!-- _class: lead -->

# Q&A

## 💬 質問にお答えします！

- どんな質問でも大歓迎です

⏱️ 14:50 - 15:00（10分）

---

<!-- _class: lead -->

# セッション②

## Microsoft "Adaptive Cloud" Updates

**高添 修 氏**
<span class="speaker">日本マイクロソフト株式会社</span>

⏱️ 15:00 - 15:20（20分）

---

<!-- _class: lead -->

# Q&A

## 💬 質問にお答えします！

- どんな質問でも大歓迎です

⏱️ 15:20 - 15:25（5分）

---

![bg right:40% 90%](../Images/hcc-logo02f.png)

# 📺 チャンネル登録を！

## 目指せ 1000人！

**YouTube HCCJPチャンネル**
https://www.youtube.com/channel/UCrf4bEl7yJnkGYo3F67gA7w

毎月第2金曜日の最新情報をお見逃しなく！

---

<!-- _class: lead -->

![bg left:28% 82%](../Images/hcc-logo02f.png)

# クロージング

## 本日のご参加ありがとうございました！

- アーカイブはYouTubeチャンネルから視聴可能
- 資料は後日公開予定
- ハッシュタグは **#HCCJP**

---

<!-- _class: lead -->

# 次回予告

## 📅 2026/3/13 14:00〜

次回の内容は調整中です！

最新情報は YouTube チャンネル・X（旧Twitter）でお知らせ！
https://www.youtube.com/channel/UCrf4bEl7yJnkGYo3F67gA7w

---

<!-- _class: lead -->

![bg left:28% 82%](../Images/hcc-logo02f.png)

# ご参加ありがとうございました！

## また次回お会いしましょう！
