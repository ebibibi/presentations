# The lab password is NOT stored in this file. Set it once per session:
#   $env:LABPWD = Read-Host "lab password" -AsSecureString | ConvertFrom-SecureString -AsPlainText
# or simply:  $env:LABPWD = "..."
if (-not $env:LABPWD) { throw "環境変数 LABPWD にラボの管理者パスワードを設定してください" }
# Shared helper for the HCCJP#77 live demo. Runs ON nested-lab-01 (L1), which is
# also where Hyper-V Manager is open, so the whole demo stays on one screen.
$ArcCred = New-Object System.Management.Automation.PSCredential(
  "Administrator", (ConvertTo-SecureString $env:LABPWD -AsPlainText -Force))

function Invoke-OnArc { param([scriptblock]$Script)
  Invoke-Command -VMName "arcwin01" -Credential $ArcCred -ScriptBlock $Script
}

function Write-Title { param([string]$Text)
  Write-Host ""
  Write-Host ("  " + $Text + "  ") -ForegroundColor Black -BackgroundColor Cyan
  Write-Host ""
}

function Write-Next { param([string]$Cmd, [string]$What, [string[]]$Steps)
  Write-Host ""
  Write-Host "  ────────────────────────────────────────────" -ForegroundColor DarkGray
  Write-Host "  次にやること: " -NoNewline -ForegroundColor DarkGray
  Write-Host $What -ForegroundColor White
  if ($Steps) {
    Write-Host ""
    foreach ($line in $Steps) {
      if ($line -like '*⚠*') { Write-Host ("    " + $line) -ForegroundColor Yellow }
      else                   { Write-Host ("    " + $line) -ForegroundColor Gray }
    }
    Write-Host ""
  }
  if ($Cmd) { Write-Host "  コマンド    : " -NoNewline -ForegroundColor DarkGray; Write-Host $Cmd -ForegroundColor Yellow }
  Write-Host ""
}

# T0 is written to disk, not a variable, so it survives closing the console.
$script:T0File = "C:\hccjp77\demo\T0.txt"
function Get-Elapsed {
  if (-not (Test-Path $script:T0File)) { return $null }
  $t0 = [datetime]::Parse((Get-Content $script:T0File -Raw).Trim())
  return (Get-Date) - $t0
}

function Show-OsTruth {
  Invoke-OnArc {
    $p = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server"
    $tls = (Get-ItemProperty $p -Name Enabled -EA SilentlyContinue).Enabled
    [PSCustomObject]@{
      'タイムゾーン'       = (Get-TimeZone).Id
      'TLS 1.2 Server'     = $(if ($null -eq $tls) { "値なし（消えている）" } else { $tls })
      '最終起動'           = (Get-CimInstance Win32_OperatingSystem).LastBootUpTime.ToString("HH:mm:ss")
    }
  } | Format-List 'タイムゾーン','TLS 1.2 Server','最終起動'
}
