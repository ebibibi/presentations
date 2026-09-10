# The lab password is NOT stored in this file. Set it once per session:
#   $env:LABPWD = Read-Host "lab password" -AsSecureString | ConvertFrom-SecureString -AsPlainText
# or simply:  $env:LABPWD = "..."
if (-not $env:LABPWD) { throw "環境変数 LABPWD にラボの管理者パスワードを設定してください" }
# Shared helper: credential + a wrapper that runs a scriptblock inside the
# nested Hyper-V host (nested-lab-01) that actually owns arcwin01.

$LabPwd = ConvertTo-SecureString $env:LABPWD -AsPlainText -Force
$LabCred = New-Object System.Management.Automation.PSCredential("Administrator", $LabPwd)
function Invoke-OnLabHost { param([scriptblock]$Script, [object[]]$ArgList)
  Invoke-Command -VMName "nested-lab-01" -Credential $LabCred -ScriptBlock $Script -ArgumentList $ArgList
}
# Two hops: L0 -> L1 (nested-lab-01) -> L2 (arcwin01). The inner session has its
# own environment, so the password is passed in as an argument rather than read
# from $env:LABPWD there.
function Invoke-OnArcwin { param([scriptblock]$Script)
  Invoke-Command -VMName "nested-lab-01" -Credential $LabCred -ScriptBlock {
    param($inner, $pwd)
    $c2 = New-Object System.Management.Automation.PSCredential("Administrator", (ConvertTo-SecureString $pwd -AsPlainText -Force))
    Invoke-Command -VMName "arcwin01" -Credential $c2 -ScriptBlock ([scriptblock]::Create($inner))
  } -ArgumentList $Script.ToString(), $env:LABPWD
}

