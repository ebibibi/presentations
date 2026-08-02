# HCCJP 第76回勉強会

## 開催情報

- **日時**: 2026年8月14日（金）14:00-15:30
- **形式**: オンライン（YouTube Live）
- **テーマ**: AIに"オンプレの鍵"を渡してみた — Azure Arcで繋いだWindows/Linuxを、AIエージェントに運用させる

## 概要

毎月第2金曜日14時からはHCCJPの勉強会！8月は**Azure Arc × AIエージェント**でお届けします。

第74回で「オンプレのマシンにNested Hyper-Vの検証環境をコードで建てる」話をしました。今回はその**続き**です——**建てた環境をAzure Arcで繋いだら、そこから先はどこまでできるのか**。

Azure Arc でオンプレのサーバーを Azure に接続すると、そのサーバーは Azure リソースとして扱えるようになります。**インバウンドのポート開放なし、VPNなし、踏み台なし**（通信はアウトバウンド443のみ）。コマンド実行も、構成の強制も、パッチ適用も、SSH接続すら、Azure の Control Plane 経由で通ります。つまり**「サーバー室に行く」「VPNを繋ぐ」という前提そのものが消える**。

そしてここが本題です。Azure 側の入口が `az` コマンドに統一されているということは——**AIエージェントがそのまま運用の手を持てる**ということです。「あのサーバーのディスクが逼迫してる、原因を調べて直しておいて」と日本語で投げるだけで、AIがArc経由で対象を特定し、コマンドを流し、結果を読んで、次の手を打つ。オンプレのWindowsもLinuxも、区別なく。

本セッションでは、これを**その場で実演**します。「本当に全部できるのか？」を、スライドではなく動く画面でお見せします。あわせて、**AIにどこまでの権限を渡すべきか**——Arc の RBAC・監査ログ・実行できる操作の境界という、実運用で必ずぶつかる話も正面から扱います。

「オンプレは残る。でも運用する場所は変えられる」——AI時代のハイブリッドクラウド運用の姿を、一緒に見に行きましょう！

## セッション内容

### 1. Microsoft "Adaptive Cloud" 最新動向

高添 修 氏（日本マイクロソフト株式会社）

Microsoft高添さんからは毎月恒例のMicrosoft "Adaptive Cloud" の最新動向をお伝えいただきます！
Azure Local、Azure Arc、Windows Server関連の最新情報をお見逃しなく！

### 2. AIに"オンプレの鍵"を渡してみた — Azure Arcで繋いだWindows/Linuxを、AIエージェントに運用させる

**胡田 昌彦**（日本ビジネスシステムズ株式会社 / Microsoft MVP）

お話しする予定の内容：

- **なぜ今 Azure Arc なのか** — オンプレは無くならない。無くせるのは「そこまで行く手間」のほう
- **繋ぐ仕組みのおさらい** — Connected Machine agent / アウトバウンド443のみ / Arc Gateway / オンボーディングの実際
- **Arc越しに"できること"の棚卸し** — Run Command、Machine Configuration、拡張機能、SSH over Arc、Update Manager、Azure Monitor、Defender for Cloud
- **ここにAIを繋ぐ** — 入口が `az` に統一されている＝AIエージェントがそのまま運用の手を持てる。スキル化して安定させる
- **デモ**（本編）— 自宅のNested Hyper-Vラボ（第74回で建てたやつ）のWindows Server / Linux を、AIに日本語で指示して調査・修正・パッチ適用まで
- **権限と怖さの話** — AIに何を許し、何を許さないか。RBACの切り方、監査ログ、壊さないための仕掛け
- **まとめ** — 「運用する場所」が変わると、インフラエンジニアの仕事はどう変わるか

### デモでお見せする予定（抜粋）

- 「このサーバーのディスクが逼迫している。原因を特定して空けておいて」（Linux）
- 「ドメインコントローラーの状態を確認して、複製が正常か報告して」（Windows）
- 「Arcに繋がっている全台のパッチ適用状況を出して、必要なものを当てて」（横断）

※ デモは実環境を使用します。当日の状況により内容を調整する場合があります。

## スピーカー

- **高添 修 氏** - 日本マイクロソフト株式会社
- **胡田 昌彦** - 日本ビジネスシステムズ株式会社、Microsoft MVP for Cloud and Datacenter Management, Microsoft Azure

## タイムテーブル

| 時刻 | 時間 | セッション | スピーカー |
|------|------|------------|------------|
| 14:00 | 5分 | オープニング | 胡田 昌彦 |
| 14:05 | 20分 | Microsoft "Adaptive Cloud" Updates | 高添 修 氏 |
| 14:25 | 10分 | Q&A | 高添 修 氏 |
| 14:35 | 40分 | AIに"オンプレの鍵"を渡してみた（デモ中心） | 胡田 昌彦 |
| 15:15 | 10分 | 全体Q&A | 全員 |
| 15:25 | 5分 | クロージング | 胡田 昌彦 |

## 参考リンク

- [Azure Arc-enabled servers ドキュメント](https://learn.microsoft.com/azure/azure-arc/servers/)
- [Run Command（Arc対応サーバー）](https://learn.microsoft.com/azure/azure-arc/servers/run-command)
- [SSH access to Azure Arc-enabled servers](https://learn.microsoft.com/azure/azure-arc/servers/ssh-arc-overview)
- [Machine Configuration](https://learn.microsoft.com/azure/governance/machine-configuration/overview)
- [Azure Update Manager](https://learn.microsoft.com/azure/update-manager/overview)
- [第74回：コードで建てる検証環境](https://hybridcloud.connpass.com/event/396455/)

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
