---
marp: true
theme: default
paginate: true
header: "HCCJP 第76回勉強会 | 2026年8月14日"
footer: "ハイブリッドクラウド研究会"
style: |
  section.small { font-size: 25px; }
  section.small pre, section.small code { font-size: 0.82em; }
  section.x-small { font-size: 21px; }
  section.x-small pre, section.x-small code { font-size: 0.8em; }
---

# HCCJP 第76回勉強会

## AIに"オンプレの鍵"を渡してみた
### Azure Arcで繋いだWindows/Linuxを、AIエージェントに運用させる

**2026年8月14日（金）14:00〜15:30**

ハイブリッドクラウド研究会

---

# 自己紹介

## 胡田 昌彦（えびすだ まさひこ）

- 日本ビジネスシステムズ株式会社
- Microsoft MVP for Cloud and Datacenter Management / Microsoft Azure
- HCCJP 主幹事
- 最近は **AIエージェント（Claude Code）に開発・運用のほぼすべてを任せる** 生活
- YouTube: 「えびすだまさひこ」で検索 📺

---

# 本日のアジェンダ

| 時刻 | セッション | スピーカー |
|------|-----------|-----------|
| 14:00 | オープニング | 胡田 |
| 14:05 | **Microsoft "Adaptive Cloud" Updates** | 高添 氏 |
| 14:25 | Q&A | 高添 氏 |
| 14:35 | **AIに"オンプレの鍵"を渡してみた（デモ中心）** | 胡田 |
| 15:15 | 全体Q&A | 全員 |
| 15:25 | クロージング | 胡田 |

---

# 前回（第74回）のつづきです

- 第74回：**オンプレのマシンにNested Hyper-Vの検証環境をコードで建てる**
- 今回：**建てた環境を Azure Arc で繋いだら、どこまでできるのか**

> オンプレは無くならない。無くせるのは「**そこまで行く手間**」のほう

<!-- TODO: 第74回で建てたラボの構成図（dc01 / dc02 / mem01 / linux01）を貼る -->

---

# 今日の問い

## 「Arcで繋いだサーバーは、AIに任せて本当に全部できるのか？」

- スライドではなく、**動く画面**で答えます
- Windows も Linux も、区別なく
- ポート開放なし・VPNなし・踏み台なし

---

# Part 1｜なぜ今 Azure Arc なのか

<!-- TODO
- オンプレが残る理由（レイテンシ / 規制 / 既存資産 / コスト）
- でも「運用のためにそこへ行く」は残さなくていい
- 現場のあるある：VPN繋いで踏み台踏んでRDP…を1日に何度も
-->

---

# Part 2｜繋ぐ仕組みのおさらい

<!-- TODO
- Connected Machine agent（azcmagent）
- 通信はアウトバウンド 443 のみ／インバウンド開放不要
- Arc Gateway（エンドポイント集約）
- オンボーディング：スクリプト / Group Policy / Ansible など
- 実際に流すコマンド例
-->

---

<!-- _class: small -->

# Part 3｜Arc越しに"できること"の棚卸し

| やりたいこと | Arcでの手段 |
|---|---|
| 任意コマンドを流す | **Run Command** |
| 構成を宣言して強制する | **Machine Configuration** |
| エージェント/ツールを配る | **拡張機能（Extensions）** |
| 対話的に入る | **SSH over Arc** |
| パッチを当てる | **Azure Update Manager** |
| ログ・メトリクスを見る | **Azure Monitor / AMA** |
| 守る | **Defender for Cloud** |
| 誰に何を許すか | **Azure RBAC / Activity Log** |

<!-- TODO: 各行に実コマンド例と「ハマりどころ」を1枚ずつ足す -->

---

# Part 4｜ここにAIを繋ぐ

<!-- TODO
- 入口が az に統一されている ＝ AIエージェントがそのまま運用の手を持てる
- MCPではなく「CLI + スキル」で安定させる方針（うちの流儀）
- スキル化して、AIに"正しい叩き方"を教える
- 失敗パターン：AIが古いコマンドを使う / 対象を取り違える → どう防ぐか
-->

---

# Part 5｜デモ 🎬

## ① Linux：「ディスクが逼迫している。原因を特定して空けて」

## ② Windows：「DCの状態を確認して、複製が正常か報告して」

## ③ 横断：「全台のパッチ適用状況を出して、必要なものを当てて」

<!-- TODO: 各デモの前後で「AIが実際に叩いたコマンド」を見せる -->

---

# Part 6｜権限と、怖さの話

<!-- TODO
- AIに何を許し、何を許さないか（Run Command の破壊力）
- RBACの切り方：スコープ / カスタムロール / 読み取りだけの世界
- 監査：Activity Log に全部残る＝人間より追跡しやすい面もある
- 壊さないための仕掛け：承認ゲート / 検証環境で先に流す / dry-run
-->

---

# まとめ

<!-- TODO
- 「運用する場所」が変わる＝オンプレの物理的制約から運用が外れる
- そこにAIが入ると、"手を動かす人"の役割が変わる
- インフラエンジニアは何をする人になるのか
-->

---

# ご参加ありがとうございました！

- HCCJP は **Azure × ハイブリッドクラウド × 生成AI** のコミュニティです
- 企業・個人問わずオープンに参加できます
- **登壇者・事例共有 募集中！** 「うちのこの話、してみたい」をぜひ 🙌
- Connpass: https://hybridcloud.connpass.com/

## 次回：第77回（2026年9月11日（金）14:00〜）
