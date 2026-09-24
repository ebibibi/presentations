# HCCJP 第78回勉強会 — Connpass 掲載内容

> Connpass にはイベント作成APIが無いため、管理画面へ手作業で入力する。
> グループ: https://hybridcloud.connpass.com/ →「新しいイベントを作成」
> 下の「フォーム項目」を各欄へ、「説明欄」以下をそのまま説明欄へ貼る（Connpass は Markdown 記法に対応）。
> イベント画像は `thumbnail.png` を使う。

## フォーム項目

| 項目 | 値 |
|---|---|
| イベントタイトル | Azureへの通信経路をプライベートに！？プライベートパス構成で読み解くAzure Localのネットワーク |
| キャッチ | Disconnectedじゃない、Connectedのまま経路をプライベートに。Azure Localの南北通信をまるごと読み解く【HCCJP 第78回】 |
| 開催日時 | 2026/10/09（金）14:00 〜 15:30 |
| 開催形式 | オンライン |
| 開催場所 | オンライン（YouTube Live） |
| 参加費 | 無料 |
| 定員 | 999名 |
| ハッシュタグ | HCCJP |
| 資料の公開 | 公開 |

---

## 説明欄（ここから下をそのまま貼る）

毎月第2金曜日14時からはHCCJPの勉強会！10月は幹事企業・三井情報（MKI）の **松本 秀太 氏** による **Azure Local のプライベートパス構成** のセッションと、毎月恒例の **Microsoft "Adaptive Cloud" 最新動向**（高添 修 氏）の2本立てでお届けします。

## ⏰ タイムテーブル

| 時刻 | 時間 | セッション | スピーカー |
|------|------|------------|------------|
| 14:00 | 5分 | オープニング | 胡田 昌彦 |
| 14:05 | 45分 | Azureへの通信経路をプライベートに！？プライベートパス構成で読み解くAzure Localのネットワーク | 松本 秀太 氏 |
| 14:50 | 10分 | Q&A | 松本 秀太 氏 |
| 15:00 | 20分 | Microsoft "Adaptive Cloud" 最新動向 | 高添 修 氏 |
| 15:20 | 5分 | Q&A | 高添 修 氏 |
| 15:25 | 5分 | クロージング・次回告知 | 胡田 昌彦 |

## 📺 視聴方法

YouTube Live（HCCJPチャンネル）で配信します。参加登録なしでもご覧いただけますが、資料共有や次回のご案内のためConnpassからの参加登録をおすすめします。

配信URL: https://www.youtube.com/watch?v=OzM0kAtUcDA

---

## セッション1：Azureへの通信経路をプライベートに！？プライベートパス構成で読み解くAzure Localのネットワーク

**松本 秀太 氏**（三井情報株式会社）

Azure LocalでAzureへの通信を外部に出したくない、と考えたときに思い浮かぶのはDisconnected Operationsかもしれません。
しかし今回取り上げるプライベートパス構成は、あくまで**Connectedモードのまま**Azureへの通信経路を**ExpressRouteやサイト間VPN経由のプライベートな経路**に置き換えるアーキテクチャです。
一見すると通信経路を複雑にするだけにも見えるこの構成のメリット、構成時のポイントについて、**触ってみてわかった内容**をお話しします。

また、この構成は**Azure Arc Gatewayやプロキシ設定等、Azure Localの南北方向の通信制御の仕組み**を理解するにも良い題材です。
Azure Localの**何が、何のために、どこと、どういう経路で通信しているのか**、プライベートパス構成を通して理解を深めていきましょう。

---

## セッション2：Microsoft "Adaptive Cloud" 最新動向

**高添 修 氏**（日本マイクロソフト株式会社）

毎月恒例、Azure Local・Azure Arc・Windows Server まわりの最新情報を日本マイクロソフトの高添さんからお届けします。アップデートの本数が多い領域なので、「今月これだけは押さえておきたい」を20分に凝縮してご紹介いただきます。**この枠だけを目当てに毎月ご参加いただいている方も多い、HCCJPの定番コーナーです。**

---

## 👤 スピーカー

- **松本 秀太 氏** — 三井情報株式会社
- **高添 修 氏** — 日本マイクロソフト株式会社
- **胡田 昌彦**（司会） — 日本ビジネスシステムズ株式会社、Microsoft MVP for Cloud and Datacenter Management, Microsoft Azure

## 🙌 こんな方におすすめ

- Azure Local を導入・検討中で、「Azure との通信をインターネットに出したくない」という要件に向き合っている方
- Disconnected Operations とプライベートパス構成の違いを整理したい方
- ExpressRoute / サイト間VPN / プロキシ / Azure Arc Gateway と Azure Local の関係を理解したい方
- Azure Local の通信要件（何が・どこと・どういう経路で通信しているのか）を設計・説明する立場の方
- Azure Local / Azure Arc / Windows Server の最新動向をまとめてキャッチアップしたい方

## 📚 過去回のアーカイブ

- 公式サイト: https://www.hccjp.org/
- YouTube: https://www.youtube.com/@hccjp

## 🏢 主催

ハイブリッドクラウド研究会（HCCJP）
主幹事: 日本ビジネスシステムズ株式会社

幹事（50音順）:
NTTコミュニケーションズ株式会社 / 日商エレクトロニクス株式会社 / 日本ヒューレット・パッカード株式会社 / 日本マイクロソフト株式会社 / VistaNet株式会社 / 株式会社ネットワールド / 三井情報株式会社 / レノボ・エンタープライズ・ソリューションズ株式会社

#HCCJP

---

## 準備チェックリスト

- [x] アジェンダ確定（松本さん・高添さん）
- [x] README / Connpass 原稿 / サムネイル作成
- [ ] 松本さんへ事前確認（表記・持ち時間・資料公開可否・リハーサル）（メール下書きは Obsidian の HCCJP 第78回フォルダ）
- [ ] Connpass イベント作成（手動・上記を貼る／画像は `thumbnail.png`）
- [x] YouTube Live を予約（https://www.youtube.com/watch?v=OzM0kAtUcDA）
- [ ] Connpass の説明欄に YouTube URL を反映（手動）
- [ ] hccjp.org に第78回を掲載（hccjp リポの `content.json`・Connpass 公開後）
- [ ] 告知: Connpass メール / X / BlueSky / LinkedIn / Discord（`hccjp-promote`）
- [ ] HCCJP Teams・JBS の Teams に紹介
- [ ] 前日: 登壇者へ Teams 招待・リマインドメール
