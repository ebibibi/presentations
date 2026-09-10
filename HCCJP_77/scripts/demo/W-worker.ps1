# 使い方: W-worker.ps1 [リソース名]
. C:\hccjp77\demo\_demo.ps1

$target = $args | Where-Object { $_ -notlike '-*' } | Select-Object -First 1

if ($target) { Write-Title ("W  ワーカーのログ ─ " + $target) }
else         { Write-Title "W  ワーカーのログ ─ 直近の実行" }
Write-Host "  C:\ProgramData\GuestConfig\arc_policy_logs\gc_worker.log" -ForegroundColor DarkGray
Write-Host "  使い方: W-worker.ps1 [リソース名]　（例: W-worker.ps1 SecureWebResource）" -ForegroundColor DarkGray
Write-Host ""

$rows = Invoke-OnArc {
  param($target)
  $log = "C:\ProgramData\GuestConfig\arc_policy_logs\gc_worker.log"
  $lines = Get-Content $log -Tail 3000
  $job = $null; $lastTime = '--:--:--'
  $out = New-Object System.Collections.ArrayList
  foreach ($line in $lines) {
    # LCM messages are continuation lines with no timestamp of their own, so
    # carry the last one seen forward.
    if ($line -match '^\[\d{4}-\d{2}-\d{2} (?<hms>\d{2}:\d{2}:\d{2})') { $lastTime = $Matches.hms }
    if ($line -match 'Job (?<j>[0-9a-f]{8}-[0-9a-f-]{27})') { $job = $Matches.j.Substring(0,8) }
    if ($line -match 'LCM:\s+\[\s*(?<phase>\w+)\s+(?<op>\w+)\s*\]\s*\[\[(?<res>[^\]]+)\]') {
      $sec = if ($line -match 'in\s+(?<s>[\d\.]+)\s+seconds') { [math]::Round([double]$Matches.s, 1) } else { $null }
      [void]$out.Add([PSCustomObject]@{ hms=$lastTime; job=$job; res=$Matches.res; phase=$Matches.phase; op=$Matches.op; sec=$sec })
    }
  }
  if ($target) { $out = $out | Where-Object { $_.res -like "*$target*" } }
  $out | Select-Object -Last 40
} -ArgumentList $target

if (-not $rows) {
  Write-Host "  該当するログがありません（割り当て名のつづりを確認してください）" -ForegroundColor Yellow
} else {
  Write-Host "【1】整形したもの（Test だけか、Set まで走ったか）" -ForegroundColor Cyan
  Write-Host ""
  Write-Host ("  {0,-9} {1,-9} {2,-28} {3,-6} {4,-5} {5}" -f '時刻','Job','リソース','操作','段階','所要') -ForegroundColor DarkGray
  Write-Host ("  " + ("-" * 76)) -ForegroundColor DarkGray
  foreach ($r in $rows) {
    $color = switch ($r.op) { 'Set' { 'Green' } 'Test' { 'Yellow' } default { 'Gray' } }
    $sec = if ($null -ne $r.sec) { "{0} 秒" -f $r.sec } else { "" }
    Write-Host ("  {0,-9} {1,-9} {2,-28} {3,-6} {4,-5} {5}" -f $r.hms, $r.job, $r.res, $r.op, $r.phase, $sec) -ForegroundColor $color
  }
  Write-Host ""
  $ops = ($rows | Select-Object -ExpandProperty op -Unique) -join ", "
  Write-Host ("  出てきた操作: " + $ops) -ForegroundColor Cyan
  if ($rows | Where-Object { $_.op -eq 'Set' }) {
    Write-Host "  → Set が実行されています。実機の値が書き換えられました。" -ForegroundColor Green
  } else {
    Write-Host "  → Set がありません。値の確認（Test / Get）だけで、まだ直していません。" -ForegroundColor Yellow
  }
}

Write-Host ""
Write-Host "【2】生のログ（そのまま・直近40行）" -ForegroundColor Cyan
Write-Host "  上の整形は、この中の LCM: 行を拾っているだけです。" -ForegroundColor DarkGray
Write-Host ("  " + ("-" * 76)) -ForegroundColor DarkGray
Invoke-OnArc { Get-Content "C:\ProgramData\GuestConfig\arc_policy_logs\gc_worker.log" -Tail 40 } |
  ForEach-Object { Write-Host $_ -ForegroundColor DarkGray }
Write-Host ("  " + ("-" * 76)) -ForegroundColor DarkGray
Write-Host ""
