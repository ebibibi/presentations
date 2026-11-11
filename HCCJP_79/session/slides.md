---
marp: true
theme: default
paginate: true
header: "HCCJP 第79回 | さよなら同期待ち"
footer: "ハイブリッドクラウド研究会"
style: |
  section, section h1, section h2, section h3, section p, section li, section td, section th, section blockquote {
    font-family: YuGothic, "Yu Gothic", "Hiragino Sans", "Noto Sans CJK JP", sans-serif;
  }
  section code, section pre { font-family: Consolas, "Courier New", monospace; }
  section { font-size: 28px; }
  section.small { font-size: 24px; }
  section.lead { justify-content: center; text-align: center; }
  section.demo h1 { color: #c62828; }
  section img { display: block; margin: 0 auto; }
---

<!-- _class: lead -->

# さよなら同期待ち

## Entra Kerberos で変わるハイブリッド参加

HCCJP 第79回勉強会　2026年11月13日

胡田 昌彦

---

# 今日のお話を一言で

**ハイブリッド参加が、同期を待たずに終わるようになります**

- オンプレの AD が発行する **Kerberos チケット**を身分証にして、Entra にその場で登録する
- 現在は**プレビュー**
- 今日は仕組みを説明したあと、**同じ PC で「失敗 → 構成 → 成功」をやって見せます**

---

# 今日の流れ

1. ハイブリッド参加のしくみ（どこで、何が、どの順番で動くか）
2. プレビューで何が変わるのか
3. 必要なもの、構成するもの
4. **デモ**: 失敗する PC を、その場で参加させる
5. まとめと注意点

---

<!-- _class: lead -->

# 1. ハイブリッド参加のしくみ

---

# ハイブリッド参加とは

**AD にドメイン参加している Windows を、Entra ID にもデバイスとして登録すること**

- オンプレの AD とグループ ポリシーはそのまま使い続けられる
- Entra 側から「会社の PC」として認識できるようになる
- その結果、たとえば次のことができる
  - 条件付きアクセスで「ハイブリッド参加済みのデバイス」を条件にする
  - Microsoft 365 などへのシングル サインオン
  - Intune との共同管理

---

<!-- _class: small -->

# 登場人物

| 場所 | 名前 | 役割 |
|---|---|---|
| クライアント | **タスク スケジューラ** | 決まったきっかけで登録処理を起動する |
| クライアント | **dsregcmd.exe** | 登録処理の本体 |
| クライアント | **TPM / 証明書ストア** | 鍵を守る / デバイス証明書を保存する |
| オンプレ | **SCP** | AD に置く案内板。登録先のテナントが書いてある |
| オンプレ | **Entra Connect Sync** | AD を Entra へ同期する。**デバイスも同期する** |
| クラウド | **DRS** | Device Registration Service。デバイス登録を受け付ける |
| クラウド | **Entra ID** | デバイスオブジェクトを持つ |

---

<!-- _class: small -->

# クライアント側の主役: タスク スケジューラ

`\Microsoft\Windows\Workplace Join\` に3つのタスクがある（デモ環境の Windows 11 で確認）

| タスク | 実行ユーザー | 動作 |
|---|---|---|
| **Automatic-Device-Join** | SYSTEM | `dsregcmd.exe` を実行する。**ハイブリッド参加の本体** |
| Device-Sync | SYSTEM | 登録後の同期 |
| Recovery-Check | ログオンユーザー | 回復の確認（既定は無効） |

**Automatic-Device-Join** が動くきっかけ

- ユーザーのサインインの **1分後**
- 登録イベント（`User Device Registration/Admin` の **4096**）が出たとき、以後 **1時間ごと**
- 1回の実行は最長 **5分**

---

<!-- _class: small -->

# 身分証は2段階

| | 仮の身分証 | 正式な身分証 |
|---|---|---|
| もの | **自己署名証明書** | **デバイス証明書** |
| 発行者 | PC 自身（だれでも作れる） | **DRS**（`MS-Organization-Access`） |
| 秘密鍵 | TPM | TPM（別の鍵） |
| 置き場所 | **AD の `userCertificate` だけ** | 証明書ストア `LocalMachine\My` |
| 役目 | 「AD の pc01 本人です」と示す | Entra とのやり取りに使う |

自称の身分証は Entra に信用されない。だから**本人確認に使って、正式な身分証と取り替える**
（鍵と置き場所はデモ環境の Windows 11 で確認）

---


# 従来の流れを、1コマずつ追う

次のページから、処理の順番に沿って図を進めます

- 青い矢印: いま起きている処理
- 灰色の矢印: すでに終わった処理
- 赤: 失敗

---

<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: false -->

![bg contain](frames/hj_old_00.png)

---

<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: false -->

![bg contain](frames/hj_old_01.png)

---

<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: false -->

![bg contain](frames/hj_old_02.png)

---

<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: false -->

![bg contain](frames/hj_old_03.png)

---

<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: false -->

![bg contain](frames/hj_old_04.png)

---

<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: false -->

![bg contain](frames/hj_old_05.png)

---

<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: false -->

![bg contain](frames/hj_old_06.png)

---

<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: false -->

![bg contain](frames/hj_old_07.png)

---

<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: false -->

![bg contain](frames/hj_old_08.png)

---

<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: false -->

![bg contain](frames/hj_old_09.png)

---

<!-- _class: small -->

# 同期待ちが生んでいた問題

- **Autopilot**: 同期が終わるまで、ユーザーを待たせる
- **条件付きアクセス**: ハイブリッド参加を求めるポリシーに弾かれる
- **非永続 VDI**: 同期が終わる前にマシンが消える
- **デバイス同期を構成していない環境**: 同期ベースの登録は完了しない

待っているのは **デバイス情報の到着と、その後の再試行**です

---

<!-- _class: small -->

# Cloud Syncの「同期」と今回の違い

**現在のCloud Syncにも、デバイス同期の公式手順があります**

| 経路 | 登録の前に必要なこと |
|---|---|
| 同期ベース | デバイス情報が同期でEntraに届くこと |
| 今回のKerberos方式 | AD発行の紹介チケットを起点に本人確認すること |

**今回外すのは「デバイスの同期待ち」。ユーザー同期とは別の話です**

デモのラボではデバイス同期を構成せず、Kerberosの登録経路を見せます

出典: [Cloud Sync Device Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/device-sync)

---

<!-- _class: lead -->

# 2. プレビューで何が変わるのか

---

# Entra Kerberos によるハイブリッド参加

**同期を待たずに、ハイブリッド参加を完了できる**

Microsoft が挙げている用途

- 非永続 VDI のハイブリッド参加
- Cloud Sync を使う（使いたい）環境
- Azure Virtual Desktop / Windows 365 のプロビジョニング改善
- Entra Connect Sync を使えない分断フォレスト

---

<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: false -->

![bg contain](frames/hj_new_00.png)

---

<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: false -->

![bg contain](frames/hj_new_01.png)

---

<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: false -->

![bg contain](frames/hj_new_02.png)

---

<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: false -->

![bg contain](frames/hj_new_03.png)

---

<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: false -->

![bg contain](frames/hj_new_04.png)

---

<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: false -->

![bg contain](frames/hj_new_05.png)

---

<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: false -->

![bg contain](frames/hj_new_06.png)

---

# TDO（Trusted Domain Object）とは

AD の中にある**信頼関係の記録**です

- 別のドメインと信頼関係を結ぶと、AD に同じ種類のオブジェクトができる
- 今回の相手は別の AD ではなく、**Entra の Kerberos 領域** `KERBEROS.MICROSOFTONLINE.COM`
- 内容は「**Entra は、この AD が発行した身分証を受け入れる**」
- これがあるので、DC は PC に **Entra への紹介状**を発行できる

---

# 信頼の向きに注意

| | |
|---|---|
| 信頼する側 | **Entra**（AD の身分証を受け入れる） |
| 信頼される側 | **AD** |
| アクセスの向き | **AD の PC → Entra のサービス** |
| AD から見た方向 | `Inbound`（受信） |

AD から見ると「相手から信頼されている」ので **Inbound** になります

---

<!-- _class: small -->

# 「Entra Kerberos」は2つの話で使われる

`Set-AzureADKerberosServer` は、役割の違うものを AD に作ります

| | ユーザー認証の仕組み | 今日の仕組み |
|---|---|---|
| 作られるもの | `krbtgt_AzureAD`、`AzureADKerberos` | **TDO**（`-SetupCloudTrust` を付けたとき） |
| アクセスの向き | クラウドの身分証 → オンプレの資源 | **オンプレの PC → クラウドのサービス** |
| 代表例 | WHfB Cloud Kerberos Trust、FIDO2 | SQL MI の受信フロー、**デバイス登録** |

名前が同じでも、向きと用途が違います

---

<!-- _class: lead -->

# 3. 必要なものと構成

---

<!-- _class: small -->

# 前提条件

| 項目 | 内容 |
|---|---|
| DC | Windows Server 2025 **ビルド 26100.6905 以降**を、**ドメインごとに1台以上** |
| クライアント | Windows 11 **ビルド 26100.6584 以降** |
| ネットワーク | 参加のときに、クライアントから WS2025 の DC へ到達できること |
| AD の権限 | Domain Admins と Enterprise Admins |
| Entra の権限 | ハイブリッド ID 管理者、アプリケーション管理者 |
| ライセンス | このプレビュー機能自体に追加要件なし |

---

<!-- _class: small -->

# 構成するのは4つ

| # | やること |
|---|---|
| 1 | **同期を有効にする**（Connect Sync または Cloud Sync） |
| 2 | **TDO を作る**: `Set-AzureADKerberosServer -SetupCloudTrust` |
| 3 | **DRSのサービスプリンシパルにSPNとタグを設定する** |
| 4 | **SCPを置く** |

このラボでは、対応OS・AD参加・通信の前提を満たしたPCに専用の追加設定はしていません

既存のKDCプロキシGPOがある環境は、公式手順に従い調整します

**同期はTDO作成の前に有効化**します（ラボで未有効時の失敗を確認）

---

<!-- _class: small -->

# 消えるもの・残るもの

| | |
|---|---|
| ❌ この登録経路で待たない | デバイス情報の同期。登録のための AD FS も不要 |
| ✅ 残る | ドメイン参加そのもの、SCP、**ユーザーの同期** |
| ✅ 新しく要る | WS2025 の DC |
| 🤔 検証で分かった | `userCertificate` は今も AD に書かれる |

**Autopilot のハイブリッド参加がクラウドネイティブになるわけではありません。** 速くなるのは登録の部分で、ドメイン参加は従来どおりです

---

<!-- _class: lead -->

# 4. デモ

失敗する PC を、その場で参加させる

---

![bg contain](lab.png)

<!--
環境は hyperv-nestlab（OSS）で自動構築した。紹介動画 https://youtu.be/nKnSazofKxs
-->

---

<!-- _class: small -->

# デモでやること

| # | やること | 見るところ |
|---|---|---|
| 1 | `pc01` の状態を確認する | まだハイブリッド参加していない |
| 2 | 構成前に参加させる | **失敗する**。新方式を試したあと、従来方式でも失敗する |
| 3 | TDO を作り、DRS を設定する | AD に TDO ができる |
| 4 | もう一度参加させる | **参加完了の状態を確認する** |
| 5 | チケットを確認する | Entra が発行したチケットがある |

ポイント: **Connect Sync は未導入。Cloud Sync のデバイス同期も使いません**

---

<!-- _class: demo small -->

# デモ1: pc01 の状態を確認する

`pc01` で実行

```powershell
dsregcmd /status | Select-String "AzureAdJoined", "DomainJoined"
```

期待する結果

```text
AzureAdJoined : NO
DomainJoined : YES
```

Entra 管理センターのデバイス一覧にも、`pc01` はまだありません

---

<!-- _class: demo small -->

# デモ2: 構成前に参加させる

`pc01` の管理者PowerShellで、実行開始時刻を記録してタスクを起動する

```powershell
$since = Get-Date
schtasks /run /tn "\Microsoft\Windows\Workplace Join\Automatic-Device-Join"
```

タスク完了後に、**今回の実行時刻以降**のログを確認する

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = "Microsoft-Windows-User Device Registration/Admin"
    StartTime = $since
} | Sort-Object TimeCreated | Select-Object TimeCreated, Id, Message
```

---

<!-- _class: demo small -->

# デモ2（続き）: 失敗の理由を見る

TDOなしでの事前検証結果（**新方式 → 従来方式の2つが失敗**）

| 順 | 方式 | 結果 |
|---|---|---|
| 1 | 新方式 `DEVICE_AUTO_KERB` | Kerberos チケットが取れない（イベント 420） |
| 2 | 従来方式 `DEVICE_AUTO` | `The device object ... is not found.`（イベント 304） |

このラボはデバイス同期未構成のため、**待つだけでは従来経路は進みません**

TDOが残ると最初も304になることがあります。番号だけでなく、時刻と本文を確認します

---

<!-- _class: demo small -->

# デモ3: TDO を作る

`dc01` の管理者PowerShellで実行。Entraには `labadmin` で対話サインインする

```powershell
$domainCred = Get-Credential CORP\Administrator
Set-AzureADKerberosServer -Domain corp.contoso.local `
    -UserPrincipalName labadmin@hccjplab.onmicrosoft.com `
    -DomainCredential $domainCred -SetupCloudTrust

Get-ADTrust -Filter * | Select-Object Name, Direction
```

期待する結果

```text
Name                         Direction
----                         ---------
KERBEROS.MICROSOFTONLINE.COM   Inbound
```

---

<!-- _class: demo small -->

# デモ3（続き）: DRS の設定を準備する

`dc01` の管理者PowerShell。対象テナントへサインインし、既存値を保持します

```powershell
Connect-Entra -TenantId hccjplab.onmicrosoft.com `
    -Scopes "Application.ReadWrite.All"
$appId = "01cb2876-7ebd-4aa4-9cc9-d28bd4d359a9"
$drs = Get-EntraServicePrincipal -Filter "AppId eq '$appId'"
if (-not $drs) { throw "DRS service principal not found" }
$spns = @($drs.ServicePrincipalNames | Where-Object { $null -ne $_ })
$tags = @($drs.Tags | Where-Object { $null -ne $_ })
$kerbSpn = "adrs/enterpriseregistration.windows.net"
$kerbTag = "KerberosPolicy:ExchangeForJwt"
```

`01cb2876-...` はDRSのアプリID。次のページも **同じPowerShell** で続けます

---

<!-- _class: demo small -->

# デモ3（続き）: 未設定の値だけ追加する

既存のSPN・タグを残し、**同じ値を二重追加しません**

```powershell
if ($spns -notcontains $kerbSpn) { $spns += $kerbSpn }
if ($tags -notcontains $kerbTag) { $tags += $kerbTag }
Set-EntraServicePrincipal -ObjectId $drs.Id `
    -ServicePrincipalNames $spns -Tags $tags
$drs = Get-EntraServicePrincipal -ObjectId $drs.Id
$drs.ServicePrincipalNames -contains $kerbSpn
$drs.Tags -contains $kerbTag
```

最後の2行が **両方 `True`** なら、SPNとタグが登録されています

---

<!-- _class: demo small -->

# デモ4: もう一度参加させる

`pc01` の管理者PowerShellで、デモ2と同じタスクを起動する

```powershell
schtasks /run /tn "\Microsoft\Windows\Workplace Join\Automatic-Device-Join"
```

**起動成功は参加完了ではありません。** タスク完了後に確認し、処理中なら再確認します

```powershell
$fields = "AzureAdJoined", "DomainJoined", "TpmProtected",
          "DeviceAuthStatus", "DeviceId"
dsregcmd /status | Select-String $fields
```

期待する結果

```text
AzureAdJoined : YES
DomainJoined : YES
TpmProtected : YES
DeviceAuthStatus : SUCCESS
```

Entra側と `DeviceId` を照合します。参加成功はユーザーSSOの確認とは別です

<!-- DeviceAuthStatusはデバイスの存在・有効性。約7秒／16〜18秒はラボ値で性能保証ではない。 -->

---

<!-- _class: demo small -->

# デモ5: チケットを確認する

`pc01` の管理者PowerShellで、SYSTEM（`0x3e7`）のチケットを見る

```powershell
klist -li 0x3e7
```

期待する結果（抜粋）

| # | チケットの宛先 | 発行元 |
|---|---|---|
| 1 | `krbtgt/CORP.CONTOSO.LOCAL` | `dc01`（AD の身分証） |
| 2 | `krbtgt/KERBEROS.MICROSOFTONLINE.COM` | `dc01`（**Entra への紹介状**） |
| 3 | `adrs/enterpriseregistration.windows.net` | **`KdcProxy:login.microsoftonline.com`** |

3枚目は **Entra が発行**しています。AD と Entra が Kerberos でつながった証拠です

---

<!-- _class: lead -->

# 5. まとめ

---

# まとめ

- 従来の同期ベースの登録は、**デバイス情報が Entra に届くのを待っていた**
- プレビューでは、**AD の Kerberos チケットを身分証にして、その場で登録できる**
- 必要なのは **対応するWS2025 DC・Windows 11と通信などの前提**。構成は4つ
- **Connect Syncやデバイス同期待ちを使わずに**ハイブリッド参加できる

---

<!-- _class: small -->

# 使う前に知っておくこと

- **プレビュー**です。本番環境で使う前に、最新のドキュメントを確認してください
- 同期はなくなりません。**ユーザーの同期**は引き続き必要です
- 参加するとき、クライアントから **WS2025 の DC に到達できる**必要があります
- ドメインに WS2025 の DC が複数あるなら、**すべて対象ビルド以降**にします
- 今日のデモは、**デバイスの登録まで**です。ユーザーのサインインや PRT は扱っていません

---

<!-- _class: small -->

# 参考資料

- [Microsoft Entra hybrid join using Microsoft Entra Kerberos (preview)](https://learn.microsoft.com/en-us/entra/identity/devices/how-to-hybrid-join-using-microsoft-entra-kerberos)
- [Cloud Syncのデバイス同期](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/device-sync)
- [How Microsoft Entra device registration works](https://learn.microsoft.com/en-us/entra/identity/devices/device-registration-how-it-works)
- [Windows Authentication for Microsoft Entra ID with the incoming trust-based flow](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/winauth-azuread-setup-incoming-trust-based-flow)
- デモ環境の自動構築: [hyperv-nestlab](https://github.com/ebibibi/hyperv-nestlab)

---

<!-- _class: lead -->

# Q&A

ご質問はコメント欄・FlowAsk からどうぞ
