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
  section.lead h1 {
    font-size: 2.2em;
  }
  section.lead h2 {
    font-size: 1.8em;
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
<span class="speaker">日本ビジネスシステムズ株式会社<br>Microsoft MVP</span>

---

# タイムテーブル

| 時刻 | セッション | スピーカー |
|------|------------|------------|
| 14:00 | オープニング | 胡田 昌彦 |
| 14:05 | ローカルLLMでAI使い放題！(40分) | 胡田 昌彦 |
| 14:45 | Q&A (10分) | |
| 14:55 | Adaptive Cloud Updates (20分) | 高添 修 氏 |
| 15:15 | Q&A (5分) | |
| 15:20 | クロージング | 胡田 昌彦 |

---

<!-- _class: lead -->

# セッション①

## ローカルLLMでAI使い放題！
## NVIDIA DGX Spark × Azure

**胡田 昌彦**

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

<!-- _class: point -->

# 構成

## Ollama + LiteLLM

<!-- ここにアーキテクチャ図を挿入 -->

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

<!-- _class: point -->

# 全体構成

<!-- ここにハイブリッド構成図を挿入 -->

Azure App Service → Tailscale Funnel → DGX Spark

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

⏱️ 14:45 - 14:55（10分）

---

<!-- _class: lead -->

# セッション②

## Microsoft "Adaptive Cloud" Updates

**高添 修 氏**
<span class="speaker">日本マイクロソフト株式会社</span>

⏱️ 14:55 - 15:15（20分）

---

<!-- _class: lead -->

# Q&A

## 💬 質問にお答えします！

⏱️ 15:15 - 15:20（5分）

---

![bg right:40% 90%](../Images/hcc-logo02f.png)

# 📺 チャンネル登録を！

## 目指せ 1000人！

https://www.youtube.com/channel/UCrf4bEl7yJnkGYo3F67gA7w

---

<!-- _class: lead -->

![bg left:28% 82%](../Images/hcc-logo02f.png)

# ありがとうございました！

**#HCCJP**

次回: 2026/3/13 14:00〜
