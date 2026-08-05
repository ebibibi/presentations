# arcwin01 (IIS) へデモ用の 1 枚ペラを配置する。Azure Arc の Run Command から実行される。
# __HTML_B64__ は deploy.sh が windows.html の base64 に置換する
# (生の HTML を埋め込むと、クォート・改行・日本語が各層で壊れるため)。
$ErrorActionPreference = 'Stop'

$root = 'C:\inetpub\wwwroot'
New-Item -ItemType Directory -Path $root -Force | Out-Null
[IO.File]::WriteAllBytes((Join-Path $root 'index.html'), [Convert]::FromBase64String('__HTML_B64__'))

# 既定の iisstart.htm が index.html より先に出ないようにする
Remove-Item (Join-Path $root 'iisstart.htm') -Force -ErrorAction SilentlyContinue
Import-Module WebAdministration
$site = 'IIS:\Sites\Default Web Site'
$docs = (Get-WebConfiguration -Filter '/system.webServer/defaultDocument/files' -PSPath $site).Collection
if (-not ($docs | Where-Object { $_.value -eq 'index.html' })) {
    Add-WebConfiguration -Filter '/system.webServer/defaultDocument/files' -PSPath $site -AtIndex 0 -Value @{ value = 'index.html' }
}

# LAN から見えるように 80/tcp を開ける。
# 既定規則の表示名はロケールで翻訳されるため -Name で操作する (KB/0014)。
Get-NetFirewallRule -Name 'IIS-WebServerRole-HTTP-In-TCP' -ErrorAction SilentlyContinue | Enable-NetFirewallRule -ErrorAction SilentlyContinue
if (-not (Get-NetFirewallRule -Name 'HCCJP76-HTTP-In' -ErrorAction SilentlyContinue)) {
    New-NetFirewallRule -Name 'HCCJP76-HTTP-In' -DisplayName 'HCCJP76 HTTP (80)' -Direction Inbound -Protocol TCP -LocalPort 80 -Action Allow | Out-Null
}

Start-Service W3SVC -ErrorAction SilentlyContinue
& iisreset /noforce | Out-Null

$r = Invoke-WebRequest http://localhost -UseBasicParsing
$title = [regex]::Match($r.Content, '<title>(.*?)</title>').Groups[1].Value
"status=$($r.StatusCode) bytes=$($r.RawContentLength) title=$title"
