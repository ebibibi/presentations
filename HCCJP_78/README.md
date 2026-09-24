# HCCJP 第78回勉強会

## 開催情報

- **日時**: 2026年10月9日（金）14:00-15:30
- **形式**: オンライン（YouTube Live）
- **テーマ**: Azureへの通信経路をプライベートに！？プライベートパス構成で読み解くAzure Localのネットワーク
- **Connpass**: https://hybridcloud.connpass.com/event/407828/
- **YouTube Live**: https://www.youtube.com/watch?v=OzM0kAtUcDA

## 概要

毎月第2金曜日14時からはHCCJPの勉強会！10月は幹事企業・三井情報（MKI）の松本さんに、Azure Local のネットワークをじっくり語っていただきます。

Azure LocalでAzureへの通信を外部に出したくない、と考えたときに思い浮かぶのはDisconnected Operationsかもしれません。
しかし今回取り上げるプライベートパス構成は、あくまでConnectedモードのままAzureへの通信経路をExpressRouteやサイト間VPN経由のプライベートな経路に置き換えるアーキテクチャです。
一見すると通信経路を複雑にするだけにも見えるこの構成のメリット、構成時のポイントについて、触ってみてわかった内容をお話しします。

また、この構成はAzure Arc Gatewayやプロキシ設定等、Azure Localの南北方向の通信制御の仕組みを理解するにも良い題材です。
Azure Localの何が、何のために、どこと、どういう経路で通信しているのか、プライベートパス構成を通して理解を深めていきましょう。

後半は毎月恒例、日本マイクロソフト 高添さんによる Microsoft "Adaptive Cloud" 最新動向です。

## セッション内容

### 1. Azureへの通信経路をプライベートに！？プライベートパス構成で読み解くAzure Localのネットワーク

**松本 秀太 氏**（三井情報株式会社 デジタルインフラ第二技術本部 インフラ第二技術部 第一技術室）

Azure LocalでAzureへの通信を外部に出したくない、と考えたときに思い浮かぶのはDisconnected Operationsかもしれません。
しかし今回取り上げるプライベートパス構成は、あくまでConnectedモードのままAzureへの通信経路をExpressRouteやサイト間VPN経由のプライベートな経路に置き換えるアーキテクチャです。
一見すると通信経路を複雑にするだけにも見えるこの構成のメリット、構成時のポイントについて、触ってみてわかった内容をお話しします。

また、この構成はAzure Arc Gatewayやプロキシ設定等、Azure Localの南北方向の通信制御の仕組みを理解するにも良い題材です。
Azure Localの何が、何のために、どこと、どういう経路で通信しているのか、プライベートパス構成を通して理解を深めていきましょう。

### 2. Microsoft "Adaptive Cloud" 最新動向

**高添 修 氏**（日本マイクロソフト株式会社）

Microsoft高添さんからは毎月恒例のMicrosoft "Adaptive Cloud" の最新動向をお伝えいただきます！
Azure Local、Azure Arc、Windows Server関連の最新情報をお見逃しなく！

## スピーカー

- **松本 秀太 氏** - 三井情報株式会社 デジタルインフラ第二技術本部 インフラ第二技術部 第一技術室
- **高添 修 氏** - 日本マイクロソフト株式会社
- **胡田 昌彦**（司会） - 日本ビジネスシステムズ株式会社、Microsoft MVP for Cloud and Datacenter Management, Microsoft Azure

## タイムテーブル

| 時刻 | 時間 | セッション | スピーカー |
|------|------|------------|------------|
| 14:00 | 5分 | オープニング | 胡田 昌彦 |
| 14:05 | 45分 | Azureへの通信経路をプライベートに！？プライベートパス構成で読み解くAzure Localのネットワーク | 松本 秀太 氏 |
| 14:50 | 10分 | Q&A | 松本 秀太 氏 |
| 15:00 | 20分 | Microsoft "Adaptive Cloud" 最新動向 | 高添 修 氏 |
| 15:20 | 5分 | Q&A | 高添 修 氏 |
| 15:25 | 5分 | クロージング・次回告知 | 胡田 昌彦 |

## 視聴方法

- **YouTube Live**: https://www.youtube.com/watch?v=OzM0kAtUcDA
- チャンネル登録をお願いします！ https://www.youtube.com/@hccjp

## 素材

| ファイル | 用途 |
|---|---|
| `connpass_event.md` | Connpass 掲載内容（フォーム項目＋説明欄）と準備チェックリスト |
| `thumbnail.png` / `cover.png` | サムネイル（1280x720） |
| `thumbnail_prompt.txt` | 背景生成プロンプト（画像内の文字は全面禁止） |
| `make_thumbnail.py` | 見出し・開催日・ロゴの合成スクリプト |

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
