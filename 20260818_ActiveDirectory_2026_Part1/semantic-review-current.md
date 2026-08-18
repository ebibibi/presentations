OpenAI Codex v0.147.0
--------
workdir: /home/ebi/wt-1539252221055864932
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a01553-a1b0-7501-ab5d-2d87e0d8a1e4
--------
user
独立したYouTube解説スライドのセマンティックレビューをしてください。生成意図・ノート・原稿なしで、公式ソース抽出事実と画面本文だけを読みます。ツールは使わないでください。
5項目をpass/failと具体的根拠で判定：source_faithfulness（公式事実と作者助言・比喩の区別）、japanese_clarity（ラベルから内容を予測）、taxonomy_challenge（分類根拠と概念の重なり）、first_time_teachback（初見で主要概念と関係を言い直せる）、presenter_usability（予習なしで画面から安全に話せる）。入門資料なので、個々のコマンドや暗号方式の実装手順まで説明していないこと自体はfail理由にしないでください。
次の形式のYAMLだけ。コードフェンス禁止。overallは全項目pass時だけpass。
source_faithfulness:
  status: pass|fail
  rationale: "..."
japanese_clarity:
  status: pass|fail
  rationale: "..."
taxonomy_challenge:
  status: pass|fail
  rationale: "..."
first_time_teachback:
  status: pass|fail
  rationale: "..."
presenter_usability:
  status: pass|fail
  rationale: "..."
reviewed_sha256: "ee4dc9989b67789597bb094b0bf37c45502f0cf2117527267ceec8aaa534f1d6"
overall: pass|fail
==== 公式ソース抽出事実 ====
# Source facts — Active Directory入門 2026年版 Part 1

取得日: 2026-08-18

## 元動画

- タイトル: 【Active Directory入門 Part1】ActiveDirectory 入門 まずは把握すべき要素/概念/単語をざっと理解！
- URL: https://www.youtube.com/watch?v=lZ8Ps6U_kvY
- 公開日: 2022-10-15
- 長さ: 49分39秒
- 2026-08-18取得時点: 37,817再生、828高評価、49コメント
- 元動画で扱う主な項目: フォレスト、ドメイン、コンテナ、OU、サイト、DNS、SRV、LDAP、NTLM、Kerberos、CredSSP、グループポリシー、ドメイン参加、ユーザープロファイル、ADデータベース、複製、Tombstone、スキーマ、FSMO、SYSVOL、FRS/DFSR、信頼関係、災害対策、診断コマンド。
- 視聴者コメントでは内容を「分かりやすい」と評価する声が複数ある一方、BGMが集中を妨げるという指摘が2件確認できる。制作者本人は最近の動画ではBGMなしにしていると返信している。
- 2026年版では内容の網羅性を維持しつつ、BGMなし、高コントラスト、体系順の再構成を採用する。

## Microsoft公式: AD DSの定義

Source: https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview

- ディレクトリはネットワーク上のオブジェクト情報を保存する階層構造。
- AD DSはディレクトリデータを保存し、ネットワークの利用者と管理者が利用できるようにする。
- 代表的なオブジェクトはユーザー、コンピューター、サーバー、ボリューム、プリンターなど。
- AD DSは認証、アクセス制御、ポリシーベース管理を統合する。
- スキーマはオブジェクトクラスと属性を定義する。
- グローバルカタログはディレクトリ内の全オブジェクトに関する情報を持ち、ドメインを越えた検索を助ける。
- 各DCは自ドメインのディレクトリ情報の完全なコピーを持ち、変更は同じドメインのDCへ複製される。

## Microsoft公式: 論理モデル

Source: https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/understanding-the-active-directory-logical-model

- 論理構造はフォレスト、ドメイン、OUなどから成る。
- フォレストは1つ以上のドメインを含み、共通のスキーマ、構成、グローバルカタログを共有する。
- ドメインはディレクトリパーティションであり、同じドメインのDC間で複製される。
- OUはドメイン内のオブジェクトを整理し、管理委任やグループポリシー適用に使う。
- 管理構造を組織図へ機械的に一致させる必要はない。運用と委任の要件で設計する。

## Microsoft公式: AD DSとMicrosoft Entra ID

Source: https://learn.microsoft.com/en-us/entra/fundamentals/compare

- AD DSはWindows Serverで提供され、オンプレミスのインフラ、Windows統合認証、LDAP、Kerberos、NTLM、ドメイン参加、グループポリシーと強く結び付く。
- Microsoft Entra IDはクラウドのIDaaSで、SaaS、OAuth2/SAML、条件付きアクセス、MFA、パスワードレス、Microsoft Entra joinなどを提供する。
- どちらかが単純に上位互換という関係ではない。同期やハイブリッド参加を通じて併用できる。

## Microsoft公式: DNS、DC Locator、SRV

Sources:

- https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/verify-srv-dns-records-have-been-created
- https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/join-computer-to-domain
- https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025

- クライアントはDNSとDC Locatorを使ってドメインコントローラーを発見する。
- SRVレコードはLDAPやKerberosなどのサービスを提供するホストとポートを示す。
- ドメイン参加では正しいDNS設定、到達性、権限、時刻同期が重要。
- Windows Server 2025はDC Locatorを改善し、短いNetBIOS形式名からDNS形式名へのマッピングを改善した。

## Microsoft公式: サイトと複製

Sources:

- https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/designing-the-site-topology
- https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts

- サイトは高速で信頼できるネットワーク接続を持つサブネットの集合を表す。
- サイト設計はクライアントが近いDCを見つけることと、サイト間複製を制御することに使われる。
- サイトリンクはサイト間の接続、コスト、スケジュールなどを表す。
- AD DSは多くのディレクトリ変更をマルチマスター方式で複製する。
- サイト内とサイト間では複製の最適化方針が異なる。

## Microsoft公式: グループポリシーとドメイン参加

Sources:

- https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-processing
- https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/join-computer-to-domain

- グループポリシーはローカル、サイト、ドメイン、OUの順序を基礎として処理される（継承・強制・ブロック・セキュリティフィルター等で結果は変わる）。
- OUはGPOリンクと管理委任に使える。一般的なコンテナはGPOリンク先ではない。
- ドメイン参加はコンピューターアカウントを作り、端末とドメインの間に安全な関係を作る。
- Kerberos認証では時刻差が問題になるため、ドメインの時刻同期が重要。

## Microsoft公式: Kerberos、NTLM、CredSSP

Sources:

- https://learn.microsoft.com/en-us/windows-server/security/kerberos/detect-remediate-rc4-kerberos
- https://learn.microsoft.com/en-us/windows/win32/secauthn/credential-security-support-provider
- https://learn.microsoft.com/en-us/entra/fundamentals/compare

- AD DS環境のWindows統合認証ではKerberosとNTLMが使われる。Kerberosが利用できない条件ではNTLMが残る場合がある。
- Kerberosはチケットを使う認証方式。RC4は互換性のため残ってきたが安全性が低く、AES系への移行が必要。
- Microsoftは、AD DCがRC4を「サポートすると仮定する既定値」を2026年第2四半期末までに無効化する計画を公式文書で案内している。適用状態は各環境の更新と設定で確認する。
- 監査にはDCのSecurityログにあるイベント4768/4769などを使える。
- CredSSPはクライアントからサーバーへ資格情報を安全に委任するSecurity Support Providerで、TLSとSPNEGOを利用する。Kerberos/NTLMと同じ分類の代替認証方式として並べない。

## Microsoft公式: LDAP

Sources:

- https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025
- https://learn.microsoft.com/en-us/entra/fundamentals/compare

- LDAPはオンプレミスのAD DSや従来型アプリがディレクトリへアクセスするときに使う主要プロトコル。
- LDAPクライアントはディレクトリ情報を検索し、許可された範囲で属性の追加・変更などの更新を行える。
- Windows Server 2025ではLDAP channel binding監査イベント3074/3075を利用できる。Windows Server 2022以降にも更新で提供される。
- Windows Server 2025では機密属性に関わるLDAP操作は暗号化された接続に制限される。
- LDAP署名、channel binding、TLS利用は互換性を監査して段階的に強化する。

## Microsoft公式: NTDS.dit、SYSVOL、DFSR

Sources:

- https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview
- https://learn.microsoft.com/en-us/windows-server/storage/dfs-replication/migrate-sysvol-to-dfsr
- https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels

- ディレクトリデータベース（NTDS.dit）にはオブジェクトと属性が保存される。
- SYSVOLにはグループポリシーテンプレートやサインインスクリプトなど、ドメインで共有するファイルが置かれる。
- ディレクトリデータとSYSVOLは別の複製系統。現行環境のSYSVOLはDFS Replication（DFSR）を使う。
- FRSは非推奨・旧方式。Windows Server 2016がFRSをサポートする最後のWindows Serverリリースであり、新しいDC昇格にはDFSR移行が必要。

## Microsoft公式: 削除、Recycle Bin、スキーマ、FSMO

Sources:

- https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/active-directory-recycle-bin
- https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-fsmo-roles
- https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview

- 削除状態もDC間で複製する必要がある。Tombstoneは削除を複製・ガベージコレクションする仕組みに関係する。
- Active Directory Recycle Binを有効化すると、削除オブジェクトを多くの属性とともに復元できる。Recycle Binはバックアップの代替ではない。
- Recycle Bin有効時、削除されたオブジェクトは復元可能なdeleted-object状態を経てrecycled-objectとなり、保持期間後にディレクトリから除去される。
- スキーマはフォレスト全体で共有され、オブジェクトクラスと属性を定義する。
- User、Computer、Groupはオブジェクトクラスの例で、displayName、mail、memberは属性の例。
- AD DSの多くはマルチマスターだが、競合や整合性問題を避けるため5つの操作を単一担当（FSMO）へ割り当てる。
- フォレスト単位: Schema Master、Domain Naming Master。
- ドメイン単位: RID Master、PDC Emulator、Infrastructure Master。
- Schema Masterはスキーマ変更を管理し、Domain Naming Masterはフォレスト内のドメインパーティションの追加・削除を管理する。
- RID MasterはDCへRIDプールを割り当てる。PDC Emulatorはパスワード変更を優先的に受け取り、フォレストルートドメインのPDC Emulatorはフォレストの権威ある時刻源となる。Infrastructure Masterは他ドメインのオブジェクト参照を管理する。

## Microsoft公式: グローバルカタログと信頼

Sources:

- https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview
- https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups

- グローバルカタログは自ドメインの全オブジェクトと全属性、他ドメインの全オブジェクトと検索に使う一部属性を保持し、フォレスト横断検索を助ける。
- 同じフォレスト内のドメイン間には信頼の経路が作られる。別フォレストとの信頼は要件に応じて明示的に設計する。
- 信頼は認証経路を作るが、それだけで対象リソースへのアクセス権を自動付与するわけではない。

## Microsoft公式: バックアップ、復旧、診断

Sources:

- https://learn.microsoft.com/en-us/azure/backup/active-directory-backup-restore
- https://learn.microsoft.com/en-us/windows/win32/ad/backing-up-and-restoring-an-active-directory-server
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/dcdiag
- https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/best-practices-for-securing-active-directory

- 複数DCは障害時の可用性を高めるが、誤削除・侵害・論理破損も複製するためバックアップの代替ではない。
- AD DS復旧ではSystem Stateを含むAD対応バックアップと、定期的に試験した復旧手順が必要。
- `dcdiag` はDCの状態を分析し、DNS、複製、接続性などのテストを行う。
- 複製確認には `repadmin /replsummary` や `repadmin /showrepl`、DC探索には `nltest /dsgetdc:<domain>`、DNSには `dcdiag /test:dns` が代表的。
- Microsoftのセキュリティ推奨では、最小権限、特権管理の分離、パッチ、監視、バックアップと復旧計画が重要。

## Microsoft公式: Windows Server 2025

Sources:

- https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels
- https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025

- Windows Server 2025のフォレスト／ドメイン機能レベルが追加された。
- Windows Server 2025機能レベルで動作できるDCはWindows Server 2025のみ。
- Windows Server 2016機能レベルではWindows Server 2016/2019/2022/2025のDCを混在できる。
- Windows Server 2025機能レベルでは32kデータベースページのオプション機能を利用できる。移行はフォレスト全体の条件を満たして計画する。
- 機能レベルはメンバーサーバーやクライアントOSを制限するものではなく、DCのOSとAD DS機能を規定する。

## Microsoft公式: DN、Kerberos基礎、時刻、PowerShell

Sources:

- https://learn.microsoft.com/en-us/windows/win32/ad/object-names-and-identities
- https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview
- https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings
- https://learn.microsoft.com/en-us/powershell/module/activedirectory/

- 識別名（Distinguished Name / DN）は、相対識別名とルートまでの祖先を連結した文字列で、オブジェクトの現在位置を含む。例は `CN=Users,DC=Fabrikam,DC=com`。移動・改名でDNは変わる。
- Kerberos Key Distribution Center（KDC）はDC上のWindows Serverセキュリティサービスへ統合され、AD DSデータベースをセキュリティアカウントデータベースとして使う。
- Kerberosは初回のドメインサインイン後、サービスごとの再利用可能なセッションチケットを使ってアクセスを成立させる。チケットにより、サービスは通常の各アクセスでDCへパススルー認証する必要がない。
- Kerberosでは、KDCが初回認証後にTicket Granting Ticket（TGT）を発行し、クライアントはTGTを提示して対象サービス用のチケットを取得する。
- `w32tm` はWindows Time Serviceの設定、監視、トラブルシューティングに使う推奨コマンドラインツール。`w32tm /monitor` はドメインまたは指定コンピューターのW32Timeを監視する。
- ActiveDirectory PowerShellモジュールには、フォレスト取得の `Get-ADForest`、ドメイン取得の `Get-ADDomain`、DC取得の `Get-ADDomainController` が含まれる。
- Active Directory Users and Computers、Active Directory Sites and Services、DNS Managerは、対応する役割またはRSATを導入したWindows Server／クライアントで使う代表的な管理コンソール。
==== 画面本文 ====
--- Slide 1 ---
Active Directory 入門
2026年版 Part 1｜まず把握すべき概念と用語
用語を、地図に置く
Source: https://www.youtube.com/watch?v=lZ8Ps6U_kvY / 2026年8月18日 ｜ 胡田昌彦 ｜ ebisuda.net
--- Slide 2 ---
02
REMAKE POLICY
内容の強みは残す。見づらさは残さない
音
BGMなし / 声と説明に集中
文字
大きく、短く / 1枚1メッセージ
色
純黒×赤文字を避ける / 色だけで区別しない
濃紺の背景＋白文字＋明るい補助色で統一
--- Slide 3 ---
03
TODAY'S GOAL
丸暗記ではなく
用語を、地図に置く
初めて聞く言葉も『論理・物理・機能』の視点で眺めれば迷いにくい
--- Slide 4 ---
04
FIRST DISTINCTION
Active Directory と Microsoft Entra ID は別物
Active Directory Domain Services
Windows Serverで運用 /  / ドメイン参加／GPO / Kerberos・NTLM／LDAP / 社内サーバー・PC管理
Microsoft Entra ID
クラウドのIDサービス /  / SaaS／条件付きアクセス / MFA・パスワードレス / Microsoft Entra join
併用 / できる
この動画の『AD』は Active Directory Domain Services（AD DS）
--- Slide 5 ---
05
LEARNING METAPHOR
AD DSを3つの役割で覚える
共有名簿
誰がいる？ / どのPC？ / どのグループ？
本人確認
誰として / サインインした？
ルール配布
どの設定を / 誰のPCへ？
学習用の比喩：保存・認証・アクセス制御・ポリシー管理を3役に整理
--- Slide 6 ---
06
THREE LENSES
用語を3つの視点で見る
① 論理構造
フォレスト / ドメイン / OU／コンテナ
② 物理構造
DC / サイト／サブネット / サイトリンク
③ 提供機能
DNS／LDAP／認証 / GPO／複製 / 信頼／復旧
重なり例｜DC＝AD DSを動かすサーバー＋認証応答　複製＝DC間構成＋同期機能
--- Slide 7 ---
07
DIRECTORY DATA
管理対象を『オブジェクト』として保存する
ユーザー
名前／所属／ / 認証に必要な情報
コンピューター
端末名／OS／所属
グループ
メンバー／権限付与
サービスアカウント
サービス用ID／ / サービス名の登録
オブジェクト = 管理対象 ／ 属性 = その対象が持つ情報項目
--- Slide 8 ---
08
DISTINGUISHED NAME
ディレクトリ内の住所は DN で表す
CN=佐藤, OU=営業部, DC=corp, DC=example, DC=com
CN
オブジェクト名
OU
組織単位
DC
DNS名の各要素
画面のフォルダー表示ではなく、階層を持つディレクトリデータ
--- Slide 9 ---
09
LOGICAL MODEL
フォレストが最上位、ドメインがデータ区画
FOREST
corp.example.com
フォレストルートドメイン / 自分のディレクトリ区画を持つ
child.corp.example.com
必要なら子ドメインを追加 / 同じフォレストの一員
→
同じフォレストはスキーマ・構成・グローバルカタログを共有
--- Slide 10 ---
10
DESIGN PRINCIPLE
フォレストやドメインは
要件が先、構造は後
設計の目安｜『分けられる』と『分けるべき』は別。まず単純な構成から
--- Slide 11 ---
11
DOMAIN ≠ DNS
ADドメインはDNS名を使う。でもDNSそのものではない
AD DSのドメイン
ユーザーやPCを持つ / ディレクトリのデータ区画 /  / 例：corp.example.com
DNSのドメイン／ゾーン
名前からIPやサービスを探す / 名前解決の範囲 /  / 例：corp.example.com
同じ名前 / 別の役割
AD DSはDNSを使ってドメインコントローラーとサービスを見つける
--- Slide 12 ---
12
DNS DEPENDENCY
DNSが壊れると、ADは『場所が分からない』
クライアント
corpのDCは / どこ？
→
DC Locator
DNSでSRVレコードを検索 / サイト等の条件でDCを選択
→
DC
LDAP／Kerberosへ / 接続
切り分けの目安｜DNS参照先でADドメインのSRVレコードを解決できるか
--- Slide 13 ---
13
SRV RECORD
SRVレコード = サービスの場所を知らせるDNSレコード
_ldap._tcp.dc._msdcs.corp.example.com
_ldap._tcp
LDAPをTCPで提供
dc._msdcs
対象ドメインのDCを検索
結果
ホスト・ポート / 優先度・重み
Aレコードだけ見て『DNSは正常』と判断しない
--- Slide 14 ---
14
DOMAIN CONTROLLER
DC = AD DSを提供するサーバー
保持
自ドメインの / ディレクトリ情報
提供
認証／LDAP / 時刻同期
同期
他のDCと / 変更を複製
DNS Server役割はDCへの併設が多いが必須ではない
--- Slide 15 ---
15
PHYSICAL MODEL
サイト = ネットワークの『近さ』を表す
東京サイト
10.10.0.0/16 / DC-TYO-01／02 /  / 高速・安定したLAN
大阪サイト
10.20.0.0/16 / DC-OSA-01 /  / 別拠点のLAN
WAN／VPN
サイトは組織図ではない。IPサブネットをサイトへ対応付ける
--- Slide 16 ---
16
SITE LINK
サイトリンク = サイト間の接続条件
経路
どのサイト同士を / 接続するか
コスト
複製経路の選択に / 影響する値
スケジュール
いつ複製を / 許可するか
近いDCの選択と、遠隔地への複製制御を物理構造で設計
--- Slide 17 ---
17
OU OR CONTAINER
OUは『管理するため』の入れ物
Organizational Unit（OU）
オブジェクトを整理 / 管理権限を委任 / GPOをリンクできる
Container
Users／Computersなど / 汎用的な入れ物 / GPOのリンク先ではない
OU設計は会社の部署図コピーではなく『委任と設定』から決める
--- Slide 18 ---
18
OU ≠ GROUP
OUは管理場所、グループは権限のまとまり
OU
原則として1オブジェクトは / 同時に1つのOU階層へ所属 /  / GPO／委任の対象
セキュリティグループ
複数グループへ所属できる /  / 共有フォルダー等の / アクセス権を付与
『営業部OUだから営業フォルダーへ入れる』ではなく、権限はグループで
--- Slide 19 ---
19
GROUP POLICY
Group Policy Object（GPO）= 設定を一括配布
Local
端末ローカル
→
Site
ネットワーク上のサイト
→
Domain
ドメイン全体
→
OU
対象OU
後で処理するGPOが原則優先。強制／継承ブロック／セキュリティフィルターで変わる
--- Slide 20 ---
20
DOMAIN JOIN
ドメイン参加 = PCにもアカウントを持たせる
PC
ドメインへ / 参加する端末
→
ドメイン参加
必要な権限で / PCアカウントを作成
→
安全な関係
端末とドメインを / 結び付ける
前提：DNS・ネットワーク到達性・権限・時刻同期
--- Slide 21 ---
21
AUTHENTICATION LAYERS
Kerberos／NTLM と
CredSSPは同じ列ではない
Kerberos・NTLMは認証方式。CredSSPは資格情報をリモート先へ委任する仕組み
--- Slide 22 ---
22
KERBEROS
Kerberos = パスワードを毎回渡さず、チケットで進む
① サインイン
ユーザーが / 本人確認
→
② KDC
TGTを発行 / ＝次の券をもらう券
→
③ サービス券
TGTを提示し / 対象用の券を取得
→
④ 利用
ファイル等へ / アクセス
時刻同期が重要。Kerberosを利用できない条件ではNTLMが残る場合がある
--- Slide 23 ---
23
LDAP
LDAP = ディレクトリへアクセスするプロトコル
検索
ユーザーは？ / グループ所属は？
更新
属性の追加・変更 / 権限の範囲内で実行
保護
署名／TLS／ / Channel Binding
互換性を監査し、署名・Channel Binding・TLS利用を段階的に強化
--- Slide 24 ---
24
DIRECTORY + FILES
AD DSで複製する主要データは2系統
NTDS.dit
ユーザー／PC／グループ / などのオブジェクトと属性 /  / AD DSの複製で同期
SYSVOL
GPOテンプレート / サインインスクリプト /  / DFS Replication（DFSR）で同期
ディレクトリデータとSYSVOLは、別の複製系統として確認する
--- Slide 25 ---
25
REPLICATION
多くの変更は、どの書き込み可能DCでも受け付ける
DC-A
ユーザー属性を / 変更
⇄
DC-B
グループを / 変更
⇄
DC-C
変更を受け取り / 複製
マルチマスターが基本。ただし全処理が完全に対等ではない → FSMOへ
--- Slide 26 ---
26
DELETION LIFECYCLE
削除状態も、保持するDC間で複製する
① 削除
オブジェクトを / 削除
→
② 削除状態
保持するDC間で / 複製
→
③ 復元可能期間
Recycle Bin有効時 / 多くの属性を保って復元
→
④ 消去
保持後に / 最終消去
Tombstoneは削除の複製・消去に関係。Recycle Binは復元機能で、バックアップではない
--- Slide 27 ---
27
SCHEMA
スキーマ = ディレクトリの『型定義』
Class
User / Computer / Group
Attribute
displayName / mail / member
Forest-wide
フォレスト全体で / 1つを共有
クラスと属性の定義を、フォレスト内のドメインで共有する
--- Slide 28 ---
28
FSMO
5つの操作役割は『担当DCを一つ』に決める
フォレストに各1つ
Schema Master / スキーマ変更を1台で受け付ける /  / Domain Naming Master / ドメイン追加・削除を調整
各ドメインに各1つ
RID Master｜重複しないID部品をDCへ配る / PDC Emulator｜パスワード変更を優先 / Infrastructure Master｜他ドメイン参照を更新
FSMO = Flexible Single Master Operations。『すべてを処理する主DC』ではない
--- Slide 29 ---
29
TRUST
信頼関係 = 別ドメインの認証結果を受け入れる経路
Domain A
ユーザーを認証 / 『この人です』
→
Domain B
認証結果を信頼 / 権限を別途確認
信頼があってもアクセス権が自動で付くわけではない
--- Slide 30 ---
30
GLOBAL CATALOG
Global Catalog（GC）= フォレスト横断の索引
Domain A の情報
オブジェクトと / 属性
GC機能を持つDC
自ドメイン：全属性 / 他ドメイン：検索用属性
Domain B の情報
オブジェクトと / 属性
→
←
GCは独立サーバーではなくDCへ追加する役割。フォレスト横断検索を助ける
--- Slide 31 ---
31
RECOVERY
DCを増やしても
複製はバックアップではない
誤削除・侵害・論理破損も複製される。可用性と復旧は別に設計する
--- Slide 32 ---
32
HEALTH CHECK
ADの健全性を確認する代表的な5観点
DNS
dcdiag /test:dns
複製
repadmin /replsummary
DC探索
nltest /dsgetdc:<domain>
時刻
w32tm /monitor
復旧
System Stateを含む / AD対応バックアップ / ＋復元テスト
運用の目安｜成功表示だけでなく『期待するDC・経路・時刻・復旧性か』を見る
--- Slide 33 ---
33
WHAT CHANGED BY 2026
2026年版で追加して覚える4点
Server 2025
機能レベルを追加 / その段階のDCは / Server 2025のみ
SYSVOL複製
FRS（旧方式） / → DFS Replication / （DFSR）
Kerberos暗号
旧式RC4の利用元を監査 / AES対応へ移行
LDAP保護
署名／TLS／ / Channel Binding / ＝TLS接続との結び付け
機能レベルはクライアントOSではなく、DCのOSとAD DS機能を規定
--- Slide 34 ---
34
SECURITY TRANSITION
監査と互換性確認から、段階的に強化
① 監査
古い暗号RC4の利用元 / 保護の弱いLDAP接続元 /  / ログで発見
② 互換性を解消
端末・サービスを更新 / KerberosはAES対応 / LDAPは署名・TLS対応
③ 段階的な強化
更新・設定の / 適用状態を確認 / 保護を段階的に強化
順番：ログで利用元を特定 → 対応 → 強化。既定値だけに頼らず確認
--- Slide 35 ---
35
CONCEPT MAP
全体はこの線でつながる
ドメイン
論理データ区画
→
DNS＋DC Locator
SRVでDCを発見
→
DC
AD DSを提供
→
認証／LDAP
本人確認・検索・更新
OU
管理と設定の単位
→
GPO
設定をリンク
→
ユーザー／PC
設定を受け取る
Site
近さ
→
近いDC
選択
DC間の複製：サイトトポロジーとネットワーク接続を考慮して変更を複製
--- Slide 36 ---
36
NEXT STEP
次は『実物』を見て、地図と結び付ける
GUI
ADユーザーとコンピューター / ADサイトとサービス / DNSマネージャー
PowerShell
Get-ADForest / Get-ADDomain / Get-ADDomainController
確認
SRVレコード / GPO適用結果 / 複製状態
Part 2：構造をGUIとPowerShellで確認する
--- Slide 37 ---
37
OFFICIAL SOURCES
今回の正本（基礎）
元動画
youtube.com/watch?v=lZ8Ps6U_kvY
AD DS overview
learn.microsoft.com/windows-server/identity/ad-ds/.../active-directory-domain-services-overview
AD logical model
learn.microsoft.com/windows-server/identity/ad-ds/plan/understanding-the-active-directory-logical-model
AD DS vs Entra ID
learn.microsoft.com/entra/fundamentals/compare
Site topology
learn.microsoft.com/windows-server/identity/ad-ds/plan/designing-the-site-topology
Replication concepts
learn.microsoft.com/windows-server/identity/ad-ds/.../active-directory-replication-concepts
Group Policy processing
learn.microsoft.com/windows-server/identity/ad-ds/manage/group-policy/group-policy-processing
完全なURLと抽出事実は同梱の source_facts.md に保存
--- Slide 38 ---
38
OFFICIAL SOURCES
今回の正本（2026差分・運用）
Functional levels
learn.microsoft.com/windows-server/identity/ad-ds/active-directory-functional-levels
What's new Server 2025
learn.microsoft.com/windows-server/get-started/whats-new-windows-server-2025
Kerberos RC4
learn.microsoft.com/windows-server/security/kerberos/detect-remediate-rc4-kerberos
CredSSP
learn.microsoft.com/windows/win32/secauthn/credential-security-support-provider
SYSVOL to DFSR
learn.microsoft.com/windows-server/storage/dfs-replication/migrate-sysvol-to-dfsr
FSMO roles
learn.microsoft.com/windows-server/identity/ad-ds/manage/understand-fsmo-roles
DCDiag
learn.microsoft.com/windows-server/administration/windows-commands/dcdiag
仕様や既定値は更新される。実装時は必ず最新の公式情報を確認

warning: Codex could not find bubblewrap on PATH. Install bubblewrap with your OS package manager. See the sandbox prerequisites: https://developers.openai.com/codex/concepts/sandboxing#prerequisites. Codex will use the bundled bubblewrap in the meantime.
codex
source_faithfulness:
  status: pass
  rationale: "AD DSとEntra ID、DNS／SRV、OUとコンテナ、GPO処理、認証方式とCredSSP、複製、FSMO、GC、信頼、復旧、2025機能レベルなどは公式抽出事実と整合する。『共有名簿』『次の券をもらう券』『場所が分からない』は学習用の比喩として明示され、設計・運用上の助言も『目安』『原則』『段階的に』などの表現で公式事実と区別されている。"
japanese_clarity:
  status: pass
  rationale: "「OUは管理場所、グループは権限のまとまり」「サイト＝ネットワークの近さ」「信頼関係＝認証を受け入れる経路」など、見出しとラベルから後続内容を予測できる。英語見出しにも日本語の定義が直結しており、表示上の余分な区切り記号はあるものの意味理解を妨げない。"
taxonomy_challenge:
  status: pass
  rationale: "論理構造・物理構造・提供機能という分類軸が先に示され、フォレスト／ドメイン／OU、DC／サイト／サイトリンク、認証／LDAP／GPOなどが根拠に沿って配置されている。DCと複製が複数の観点にまたがることも重なり例として明示し、OUとグループ、ADドメインとDNS、Kerberos／NTLMとCredSSPの混同も個別に解いている。"
first_time_teachback:
  status: pass
  rationale: "初見でも、AD DSはオブジェクトを階層的に保持し、DNSでDCを発見し、DCが認証・LDAP・複製を担い、OUへリンクしたGPOがユーザーやPCへ設定を届ける仕組みだと言い直せる。フォレスト、ドメイン、サイト、信頼、GC、バックアップの位置関係も終盤の概念マップまでに接続されている。"
presenter_usability:
  status: pass
  rationale: "各スライドに定義、対比、関係、注意点が画面内にあり、予習なしでも順番に説明できる。GPOの例外、NTLMが残る条件、Recycle Binはバックアップではないこと、信頼は権限を自動付与しないこと、セキュリティ強化前の監査と互換性確認など、安全に話すための重要な留保も表示されている。"
reviewed_sha256: "ee4dc9989b67789597bb094b0bf37c45502f0cf2117527267ceec8aaa534f1d6"
overall: pass
tokens used
22,650
source_faithfulness:
  status: pass
  rationale: "AD DSとEntra ID、DNS／SRV、OUとコンテナ、GPO処理、認証方式とCredSSP、複製、FSMO、GC、信頼、復旧、2025機能レベルなどは公式抽出事実と整合する。『共有名簿』『次の券をもらう券』『場所が分からない』は学習用の比喩として明示され、設計・運用上の助言も『目安』『原則』『段階的に』などの表現で公式事実と区別されている。"
japanese_clarity:
  status: pass
  rationale: "「OUは管理場所、グループは権限のまとまり」「サイト＝ネットワークの近さ」「信頼関係＝認証を受け入れる経路」など、見出しとラベルから後続内容を予測できる。英語見出しにも日本語の定義が直結しており、表示上の余分な区切り記号はあるものの意味理解を妨げない。"
taxonomy_challenge:
  status: pass
  rationale: "論理構造・物理構造・提供機能という分類軸が先に示され、フォレスト／ドメイン／OU、DC／サイト／サイトリンク、認証／LDAP／GPOなどが根拠に沿って配置されている。DCと複製が複数の観点にまたがることも重なり例として明示し、OUとグループ、ADドメインとDNS、Kerberos／NTLMとCredSSPの混同も個別に解いている。"
first_time_teachback:
  status: pass
  rationale: "初見でも、AD DSはオブジェクトを階層的に保持し、DNSでDCを発見し、DCが認証・LDAP・複製を担い、OUへリンクしたGPOがユーザーやPCへ設定を届ける仕組みだと言い直せる。フォレスト、ドメイン、サイト、信頼、GC、バックアップの位置関係も終盤の概念マップまでに接続されている。"
presenter_usability:
  status: pass
  rationale: "各スライドに定義、対比、関係、注意点が画面内にあり、予習なしでも順番に説明できる。GPOの例外、NTLMが残る条件、Recycle Binはバックアップではないこと、信頼は権限を自動付与しないこと、セキュリティ強化前の監査と互換性確認など、安全に話すための重要な留保も表示されている。"
reviewed_sha256: "ee4dc9989b67789597bb094b0bf37c45502f0cf2117527267ceec8aaa534f1d6"
overall: pass
