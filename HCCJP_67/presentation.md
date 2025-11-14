---
marp: true
theme: gaia
paginate: true
backgroundColor: #fff
style: |
  section {
    font-family: 'Meiryo', 'Segoe UI', sans-serif;
    font-size: 32px;
  }
  h1 {
    color: #0078d4;
    font-size: 1.5em;
  }
  h2 {
    color: #0078d4;
    font-size: 1.3em;
  }
  h3 {
    font-size: 1.1em;
  }
  .speaker {
    font-size: 0.8em;
    color: #666;
  }
  table {
    font-size: 0.7em;
  }
  th {
    background-color: #0078d4;
    color: white;
  }
  code {
    font-size: 0.85em;
    background-color: #f5f5f5;
  }
  li {
    font-size: 0.9em;
    margin-bottom: 0.3em;
  }
  /* コンテンツが多いスライド用 */
  section.small {
    font-size: 26px;
  }
  section.small h1 {
    font-size: 1.3em;
  }
  section.small h2 {
    font-size: 1.1em;
  }
  section.small li {
    font-size: 0.9em;
  }
  /* さらに小さいスライド用 */
  section.x-small {
    font-size: 22px;
  }
  section.x-small h1 {
    font-size: 1.2em;
  }
  section.x-small h2 {
    font-size: 1.0em;
  }
  section.x-small li {
    font-size: 0.88em;
  }
  /* leadクラス用 */
  section.lead {
    text-align: center;
  }
  section.lead h1 {
    font-size: 1.8em;
  }
  section.lead h2 {
    font-size: 1.4em;
  }
---

<!-- _class: lead -->

![bg right:30% 80%](../Images/ebi/アセット9.png)

# ADに依存しないクラスタの世界へ(前半)

## On-PremからAzure Localまで

**胡田 昌彦**（日本ビジネスシステムズ株式会社 / Microsoft MVP）

HCCJP 第67回勉強会
2025年11月14日

---

# 前半のアジェンダ

Windows フェールオーバークラスタのAD非依存構成の進化

1. **フェールオーバークラスタの基本**
2. **従来のAD依存構成**
3. **Windows Server 2012 R2**: AD-detached
4. **Windows Server 2016**: ワークグループクラスター
5. **Windows Server 2025**: Hyper-V完全サポート
6. **ADの役割と代替手段**
7. **まとめと展望**

⏱️ 約20分

---

<!-- _class: small -->

# フェールオーバークラスタの基本

## 高可用性を実現する仕組み

- **複数のノード**を連携させてサービスを提供
- 障害時に**自動フェールオーバー**でサービス継続
- **ハートビート監視**で問題を検知
- サーバー障害時もサービス停止を最小限に

### 代表的な用途
- Hyper-V仮想マシンの高可用性
- SQL Server (FCI / Always On AG)
- ファイルサーバー

---

<!-- _class: small -->

# 従来のAD依存構成

## Active Directoryが前提だった時代

### ADが担っていた重要な役割

- **クラスター名アカウント (CNO)** をAD上で管理
- **ノード間認証**: Kerberos認証で安全な通信
- **DNS連携**: 動的DNS更新で名前解決
- **権限管理**: ドメイングループでアクセス制御
- **管理の容易性**: GPOによる統一設定

**問題点**: 小規模環境やエッジではAD構築が負担に

---

<!-- _class: small -->

# Windows Server 2012 R2: AD-detached

## 初めてのAD非依存への試み

### 主な特徴
- クラスター名の**ADオブジェクトを作成しない**構成が可能
- New-Cluster -AdministrativeAccessPoint Dns で構成
- DNS名だけで管理するクラスター

### 制約
- ✅ ノードは依然として**ADドメイン参加が必要**
- ✅ 主に**SQL Server Always On AG**向けにサポート
- ❌ Hyper-Vやファイルサーバーは非推奨

**位置づけ**: 限定的だが重要な第一歩

---

<!-- _class: small -->

# Windows Server 2016: ワークグループクラスター登場

## 真のAD非依存クラスターへ

### 画期的な進化
- **ドメイン非参加ノード**だけでクラスター構成が可能に
- ワークグループ環境でも高可用性を実現

### 主な要件
- **ノード間認証**: 同一のローカル管理者アカウント + NTLM
- **DNS**: 手動でクラスター名を登録
- **クォーラム**: Cloud Witness または Disk Witness
  - ファイル共有Witnessは非サポート

---

<!-- _class: x-small -->

# Windows Server 2016の制約

## サポート範囲が限定的

### ✅ サポートされるワークロード
- **SQL Server Always On 可用性グループ (AG)**
  - SQL Server 2016以降で対応

### ❌ 制約のあるワークロード
- **Hyper-V**: 構成は可能だが...
  - ライブマイグレーション不可（クイックマイグレーションのみ）
  - ダウンタイムが発生するため実用性に欠ける
- **ファイルサーバー**: 認証の問題で非推奨
- **CAU (クラスター対応更新)**: 使用不可

**結論**: 主にSQL AG向けの機能として位置づけ

---

<!-- _class: small -->

# Windows Server 2025: 大きな進化

## Hyper-V完全サポートが実現！

### 🚀 ついに実現した機能
- ワークグループクラスターで**Hyper-Vが正式サポート**
- **ライブマイグレーション**が可能に
- ダウンタイムなしでVMを移行

### なぜ可能になったのか？
- **証明書ベース認証**の導入
- NTLMからの脱却（Microsoftは2024年にNTLM非推奨化）
- より安全な相互認証の実現

---
# 認証技術の進化

## Kerberos → NTLM → 証明書認証

| 世代 | 認証方式 | 特徴 |
|------|----------|------|
| **従来（AD環境）** | Kerberos | 安全・スケーラブル・AD必須 |
| **2016～2022** | NTLM | ドメイン不要・セキュリティ上の懸念 |
| **2025～** | 証明書ベース | 安全・AD不要・相互認証 |

### 証明書ベース認証の仕組み
- 各ノードに**X.509証明書**をインストール
- 相互に証明書を信頼させる設定
- TLS相互認証でノード間通信を保護
- 自己署名証明書またはCA発行証明書を使用

---

<!-- _class: small -->

# Windows Server 2025のサポート範囲

## 何ができて、何ができない？

### ✅ 正式サポート
- **Hyper-V仮想マシン**（ライブマイグレーション含む）
- **SQL Server Always On AG**

### ❌ 引き続き非サポート
- **ファイルサーバー**
  - Kerberos認証が必要なため
  - NTLM廃止の流れもあり
- **SQL Server FCI (フェールオーバークラスタインスタンス)**

---

<!-- _class: small -->

# Azure LocalのADレス構成

## クラウド統合でさらに進化

### ローカルアイデンティティクラスター
- Azure Local (23H2以降) でADレス構成をサポート
- **Azure Key Vault**と統合
  - ノードのパスワードや暗号化キーを安全に保管
  - BitLocker鍵もクラウドバックアップ

### メリット
- AD構築が不要で導入のハードル低下
- クラウドによる安全な秘密情報管理
- エコシステム（Veeam、Dell、Lenovoなど）との協調

---

<!-- _class: small -->

# 管理機能の強化

## WS2025とAzure Localの新機能

### 運用を簡素化する機能
- **内部DNSサービス**
  - クラスター内で名前解決を自己完結
  - 外部DNSサーバーへの依存を削減

- **管理ツールキット**
  - ガイド付きウィザードで設定を自動化
  - 証明書配置や管理PC設定を簡略化

### Azure Arc連携
- ドメインレスでも集中管理が可能
- ポリシー適用・監視・タグ付けをクラウドから

---

# ADが担っていた役割（まとめ）

## Active Directoryは何をしていたのか？

| 役割 | 内容 | 重要度 |
|------|------|--------|
| **① ID管理** | CNO/VCOでクラスター名・役割名を管理 | ⭐⭐⭐ |
| **② 認証** | Kerberosでノード間・クライアント認証 | ⭐⭐⭐ |
| **③ DNS連携** | 動的DNS更新で名前解決を自動化 | ⭐⭐ |
| **④ 権限管理** | ドメイングループでアクセス制御 | ⭐⭐ |
| **⑤ 管理性** | GPO・一元管理による運用の簡素化 | ⭐⭐ |

**結論**: ADはクラスターの「身元保証人」かつ「セキュリティ管理者」

---

# ADなし環境での代替手段

## それぞれの役割をどう置き換えるか？

| AD時代の役割 | ADレス環境での代替手段 |
|-------------|----------------------|
| **CNO/VCO管理** | DNS名で管理 / 内部DNSサービス |
| **Kerberos認証** | 証明書ベース認証 (2025～) / NTLM (～2024) |
| **動的DNS更新** | 手動登録 / クラスター内部DNS / Azure DNS |
| **権限管理** | ローカルセキュリティ設定 / 証明書権限管理 |
| **Witness** | Cloud Witness / Disk Witness |
| **GPO統制** | スクリプト / Azure Arc / Azure Policy |

**ポイント**: DNS・証明書・クラウドサービスの組み合わせで補完

---

<!-- _class: small -->

# メリット・デメリット

## ADレス構成の評価

### ✅ メリット
- ドメインコントローラーの構築・維持コスト削減
- 小規模・エッジ環境での迅速な展開
- インフラのシンプル化

### ⚠️ デメリット
- 手動設定が増加（DNS、証明書など）
- 証明書管理の知識が必要
- ファイルサーバーなど一部ワークロードは依然AD必須
- 運用者にとって馴染みが薄い

---

<!-- _class: x-small -->

# 参考資料

### 公式ドキュメント
- **Microsoft Learn: フェールオーバー クラスター概要**
  https://learn.microsoft.com/windows-server/failover-clustering/
- **Microsoft Learn: ワークグループ クラスターの作成**
  https://learn.microsoft.com/windows-server/failover-clustering/deploy-workgroup-cluster
- **Microsoft Learn: ワークグループ クラスターを使用してライブ マイグレーションを行う**
  https://learn.microsoft.com/ja-jp/windows-server/virtualization/hyper-v/manage/live-migration-workgroup-cluster?tabs=powershell

### 技術ブログ
- **山市良氏: Windows Server 2025 新機能**
  https://www.say-tech.co.jp/
- **NTTデータ先端技術: Hyper-V クラスター検証**
  https://www.intellilink.co.jp/column/
- **AzureFeeds: 証明書ベース認証構築**
  https://www.azurefeeds.com/


---

<!-- _class: lead -->

![bg left:30% 80%](../Images/ebi/アセット9.png)

# ご清聴ありがとうございました！

## 質問・コメントをお待ちしています

**#HCCJP でシェアお願いします！**

