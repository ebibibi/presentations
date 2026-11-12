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

## Entra Kerberosで変わるハイブリッド参加

HCCJP 第79回勉強会｜2026年11月13日

胡田 昌彦

---

# 今日の流れ

1. 同期方式のハイブリッド参加（従来方式）
2. Kerberos方式のハイブリッド参加（新方式）
3. Kerberos方式に必要な構成
4. デモ：構成前と構成後を比べる
5. まとめと検証範囲

<!--
ハイブリッド参加はAD参加とEntra登録の両方を持つ状態。
Kerberos方式ではADのチケットを本人確認に使い、デバイスの事前同期を待たずに登録する。
Cloud Syncにもデバイス同期機能がある。今回のラボはデバイス同期未構成で、Kerberos構成前後の結果を比較する。
-->

---

# ハイブリッド参加とは？

- **AD参加済みのPCを、Entra IDにもデバイス登録**
- ADのアカウントやグループポリシーを引き続き利用
- Entra IDでもPCを識別し、条件付きアクセスなどに利用
- 確認：`DomainJoined` と `AzureAdJoined` が **両方 YES**

<!--
Microsoft Entra hybrid joinedはオンプレミスのAD参加とEntra IDへのデバイス登録を持つ状態。
条件付きアクセス等の利用には各機能の構成・ライセンスなどが別途必要。
参考: https://learn.microsoft.com/en-us/entra/identity/devices/concept-hybrid-join
-->

---

<!-- _class: lead -->

# 1. 同期方式のハイブリッド参加（従来方式）

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

<!-- _class: lead -->

# 2. Kerberos方式のハイブリッド参加（新方式）

EntraがKerberosを話せるようになったことで、<br>
ADからデバイス情報が同期されるのを待たずに、<br>
**PCを本人確認できるようになった。**

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

<!--
TDOはcomputerではなくtrustedDomainクラスのADオブジェクト。信頼先・信頼の向き・認証用の信頼情報を保持する。今回の信頼先はKERBEROS.MICROSOFTONLINE.COM。AzureADKerberosというコンピューターオブジェクトとは別物。DCからTDOへの矢印はADの信頼情報の参照であり、別サーバーへの通信ではない。
根拠: https://learn.microsoft.com/en-us/windows/win32/adschema/c-trusteddomain
https://learn.microsoft.com/en-us/entra/identity/authentication/configure-microsoft-entra-kerberos-trust
-->

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

<!--
登録に使う認証トークンの取得と、DRSへのデバイス登録を区別する。登録要求にはトークンだけでなく証明書要求・転送公開鍵等を含む。旧方式との主な違いは登録前の本人確認経路であり、全HTTP APIや要求フィールドの同一性を実測したという意味ではない。
https://learn.microsoft.com/en-us/entra/identity/devices/device-registration-how-it-works
https://learn.microsoft.com/en-us/entra/identity/devices/how-to-hybrid-join-using-microsoft-entra-kerberos
-->

---

<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: false -->

![bg contain](frames/hj_new_06.png)

---

<!-- _class: lead -->

# 3. Kerberos方式に必要な構成

---

# TDO：ADとEntraの信頼

| | 今回の構成 |
|---|---|
| 信頼する側 | **Entra** |
| 信頼される側 | **AD** |
| AD側の表示 | **Inbound** |

**外部ドメインとの信頼関係を結ぶイメージ**

相手は Entra の Kerberos領域。Entraが **AD発行の紹介チケット** を信頼する。

<!--
TDOはTrusted Domain Object。相手のKerberos領域はKERBEROS.MICROSOFTONLINE.COM。
外部ドメインとの信頼関係という説明は比喩。通常のADドメインやフォレストを追加するわけではなく、ADがEntraを信頼するという逆向きの意味でもない。
根拠: https://learn.microsoft.com/en-us/entra/identity/authentication/configure-microsoft-entra-kerberos-trust
アクセスはADのPCからEntraのサービスへ。信頼の表示方向とは区別する。
WHfB Cloud Kerberos Trustのユーザー認証とは別の構成。既存のAzureADKerberos等があってもTDOの存在は別途確認する。
-->

---

<!-- _class: small -->

# 必要なOSと通信

| 対象 | 前提条件 |
|---|---|
| DC | **WS2025 26100.6905以降**／ドメインごとに1台以上 |
| PC | **Windows 11 26100.6584以降** |
| 通信 | PCから対応DC・Entraへ到達可能 |

構成権限：AD管理者／EntraのハイブリッドID管理者・アプリケーション管理者

<!--
ADの構成権限はDomain AdminsとEnterprise Admins。TDOはハイブリッドID管理者、DRS設定はアプリケーション管理者。
このプレビュー機能自体に追加のライセンス要件なし。条件付きアクセスやIntune等の要件とは別。
参加時には対応するWS2025 DCへの通信が必要。ドメイン内のWS2025 DCの更新状況も確認する。
-->

---

# 構成するのは4つ

1. **ユーザー同期** を有効化
2. **TDO** を作成
3. **DRSのSPN・タグ** を設定
4. **SCP** で登録先を指定

<!--
同期はConnect SyncまたはCloud Sync。ラボでは同期未有効だとTDO作成に失敗した。
対応OS・AD参加・通信などの前提を満たしたPCに、今回のラボでは専用の追加設定はしていない。
既存のKDCプロキシGPOを配布する環境は、公式手順に従って調整する。
-->

---

<!-- _class: lead -->

# 4. デモ：構成前と構成後を比べる

---

![bg contain](lab.png)

<!--
環境は hyperv-nestlab（OSS）で自動構築した。紹介動画 https://youtu.be/nKnSazofKxs
-->

---

<!-- _class: demo small -->

# デモ1：開始状態

**pc01：AD参加済み・Entra未参加**

```powershell
dsregcmd /status | Select-String "AzureAdJoined", "DomainJoined"
```

```text
AzureAdJoined : NO
DomainJoined : YES
```

<!--
Entraの対象デバイス、TDO、DRSの対象SPN・タグも未設定であることを事前に確認。
Connect Sync未導入、Cloud Syncのデバイス同期も未構成。
-->

---

<!-- _class: demo small -->

# デモ2：構成前は登録に失敗

pc01で実行。**タスク完了後に今回のログを確認**

```powershell
$since = Get-Date
schtasks /run /tn "\Microsoft\Windows\Workplace Join\Automatic-Device-Join"
```

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = "Microsoft-Windows-User Device Registration/Admin"
    StartTime = $since
} | Sort-Object TimeCreated | Select-Object TimeCreated, Id, Message
```

事前検証：**Kerberos方式で420 → 同期方式で304**

<!--
Kerberos未構成でチケットを取得できず、その後の同期方式もデバイス情報がないため失敗する。
TDOが残るとKerberos経路も304になることがある。番号だけでなく実行時刻と本文を見る。
Cloud Sync自体がデバイスを同期できないという一般論ではなく、このラボがデバイス同期未構成という条件。
-->

---

<!-- _class: demo small -->

# デモ3：TDOを作る

**dc01で実行**／Entraにはlabadminでサインイン

```powershell
$domainCred = Get-Credential CORP\Administrator
Set-AzureADKerberosServer -Domain corp.contoso.local `
    -UserPrincipalName labadmin@hccjplab.onmicrosoft.com `
    -DomainCredential $domainCred -SetupCloudTrust

Get-ADTrust -Filter * | Select-Object Name, Direction
```

確認：**KERBEROS.MICROSOFTONLINE.COM／Inbound**

<!--
AD側の資格情報とEntra側のサインインは、それぞれの管理境界を構成するために使う。
TDOを作った段階ではPCの登録はまだ完了していない。
-->

---

<!-- _class: demo small -->

# デモ3：DRS設定の準備

**dc01の同じPowerShellで続ける**

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

<!--
対象テナントにサインインし、既存のSPN・タグを取得する。
$appIdはDRSアプリの識別子、$drs.Idはテナント内のサービスプリンシパルのオブジェクトID。
-->

---

<!-- _class: demo small -->

# デモ3：DRSへSPN・タグを追加

**未設定の値だけ追加**し、既存値を保持する

```powershell
if ($spns -notcontains $kerbSpn) { $spns += $kerbSpn }
if ($tags -notcontains $kerbTag) { $tags += $kerbTag }
Set-EntraServicePrincipal -ObjectId $drs.Id `
    -ServicePrincipalNames $spns -Tags $tags
$drs = Get-EntraServicePrincipal -ObjectId $drs.Id
$drs.ServicePrincipalNames -contains $kerbSpn
$drs.Tags -contains $kerbTag
```

確認：**最後の2行が両方True**

---

<!-- _class: demo small -->

# デモ4：構成後に登録を再試行

**pc01で起動 → タスク完了後に状態確認**

```powershell
schtasks /run /tn "\Microsoft\Windows\Workplace Join\Automatic-Device-Join"
```

```powershell
$fields = "AzureAdJoined", "DomainJoined", "TpmProtected",
          "DeviceAuthStatus", "DeviceId"
dsregcmd /status | Select-String $fields
```

```text
AzureAdJoined : YES       DomainJoined : YES
TpmProtected  : YES       DeviceAuthStatus : SUCCESS
```

**Entra側とDeviceIdを照合**

<!--
schtasksの成功表示はタスク起動の受付。登録完了とは別で、処理中なら再確認する。
DeviceAuthStatusはEntra側のデバイスの存在・有効性の確認。ユーザーSSOやIntune準拠の検証ではない。
約7秒／16〜18秒はラボでの観測値で、性能保証ではない。
-->

---

<!-- _class: demo small -->

# デモ5：PCのチケットを確認

pc01の管理者PowerShellで、**SYSTEMのチケット** を見る

```powershell
klist -li 0x3e7
```

| 宛先 | 発行元 |
|---|---|
| `krbtgt/CORP.CONTOSO.LOCAL` | ADのdc01 |
| `krbtgt/KERBEROS.MICROSOFTONLINE.COM` | ADのdc01（紹介チケット） |
| `adrs/enterpriseregistration.windows.net` | **EntraのKDC** |

<!--
0x3e7はSYSTEMのログオンセッション。通常のklistではログオンユーザーのチケットを見てしまう。
ほかのチケットが並んでもよい。チケットの存在だけで登録完了を判定せず、デモ4の状態と合わせて確認する。
-->

---

# 5. まとめと検証範囲

- **デバイスの事前同期は不要**
- **AD参加・ユーザー同期は継続**
- 現在 **プレビュー**。導入前に要件を確認

今回の検証は **デバイス登録まで**（ユーザーSSO・PRTは未検証）

<!--
ドメイン参加そのものやDCへの到達性が不要になるわけではない。
Autopilot全体がクラウドネイティブになる話でもない。
ADのuserCertificateへの書き込みは新方式でも観測した。属性を書かないことと同期を待たないことは別。
-->

---

<!-- _class: small -->

# 参考資料・質疑応答

- [Kerberosによるハイブリッド参加：要件と設定](https://learn.microsoft.com/en-us/entra/identity/devices/how-to-hybrid-join-using-microsoft-entra-kerberos)
- [デバイス登録の仕組み](https://learn.microsoft.com/en-us/entra/identity/devices/device-registration-how-it-works)
- [Cloud Syncのデバイス同期](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/device-sync)
- [TDOの構成手順](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/winauth-azuread-setup-incoming-trust-based-flow)
- デモ環境の構築：[hyperv-nestlab](https://github.com/ebibibi/hyperv-nestlab)

質問はコメント欄・FlowAskへ
