. C:\hccjp77\demo\_demo.ps1
Write-Title "D6  評価の順番を見る ─ 1台につき1本ずつ"

Write-Host "  誰が動いていて、誰が待っているか。詰まるとここに出ます。" -ForegroundColor Gray
Write-Host ""

$ev = Invoke-OnArc {
  $log = "C:\ProgramData\GuestConfig\arc_policy_logs\gc_agent.log"
  $lines = Get-Content $log -Tail 1500
  # Only look at the agent's current session. A VM reboot (or a gcarcservice
  # restart) cuts a run in half, and the orphaned 'start' with no 'done' would
  # otherwise be reported as still running.
  $from = 0
  for ($j = $lines.Count - 1; $j -ge 0; $j--) {
    if ($lines[$j] -match 'Created Assignment_Heartbeat timer') { $from = $j; break }
  }
  $lines = $lines[$from..($lines.Count - 1)]
  $i = 0
  foreach ($line in $lines) {
    $i++
    if ($line -notmatch '^\[\d{4}-\d{2}-\d{2} (?<hms>\d{2}:\d{2}:\d{2})') { continue }
    $hms = $Matches.hms
    # Order comes from the line index, not the timestamp: when the time zone is
    # broken the log clock jumps backwards mid-file and time comparisons lie.
    if     ($line -match "Run Consistency for '(?<n>[^']+)'")            { [PSCustomObject]@{ i=$i; hms=$hms; n=$Matches.n; k='fire'  } }
    elseif ($line -match 'Starting consistency for (?<n>\S+)')           { [PSCustomObject]@{ i=$i; hms=$hms; n=$Matches.n; k='start' } }
    elseif ($line -match "run_consistency for '(?<n>[^']+)' execution completed in (?<s>\d+)") { [PSCustomObject]@{ i=$i; hms=$hms; n=$Matches.n; k='done' } }
  }
}

Write-Host "【ログの生の流れ（直近）】" -ForegroundColor Cyan
$ev | Select-Object -Last 14 | ForEach-Object {
  $label = switch ($_.k) { 'fire' { 'タイマー発火' } 'start' { '  → 実行開始' } 'done' { '  → 実行完了' } }
  $color = switch ($_.k) { 'fire' { 'DarkGray' } 'start' { 'Yellow' } 'done' { 'Green' } }
  Write-Host ("  {0}  {1}  {2}" -f $_.hms, $label, $_.n) -ForegroundColor $color
}

Write-Host ""
Write-Host "【評価の状況】" -ForegroundColor Cyan
$names = $ev | Select-Object -ExpandProperty n -Unique | Sort-Object
$rows = foreach ($n in $names) {
  $mine      = $ev | Where-Object { $_.n -eq $n }
  $lastFire  = $mine | Where-Object { $_.k -eq 'fire'  } | Select-Object -Last 1
  $lastStart = $mine | Where-Object { $_.k -eq 'start' } | Select-Object -Last 1
  $lastDone  = $mine | Where-Object { $_.k -eq 'done'  } | Select-Object -Last 1

  # "Run Consistency" is sometimes logged just after "Starting consistency" for
  # the same assignment, so a finished item would look like it is queued. Treat
  # a completed run as done; only something that never started is waiting.
  $state = '─'
  if ($lastStart -and (-not $lastDone -or $lastDone.i -lt $lastStart.i)) { $state = '★ 実行中' }
  elseif ($lastDone) { $state = '完了' }
  elseif ($lastFire) { $state = '順番待ち' }

  [PSCustomObject]@{
    '割り当て'   = $n
    '最後の発火' = if ($lastFire)  { $lastFire.hms }  else { '─' }
    '実行開始'   = if ($lastStart) { $lastStart.hms } else { '─' }
    '実行完了'   = if ($lastDone)  { $lastDone.hms }  else { '─' }
    '状態'       = $state
  }
}
$rows | Format-Table '割り当て','最後の発火','実行開始','実行完了','状態' -AutoSize

# One running and the rest waiting is the normal shape of a serial queue, not a
# fault. What actually breaks the demo is the heavy baseline audit coming back.
$heavy = $rows | Where-Object { $_.'割り当て' -eq 'AzureWindowsBaseline' }
if ($heavy) {
  Write-Host "  ⚠️ AzureWindowsBaseline が戻ってきています。テナント既定の" -ForegroundColor Red
  Write-Host "     「Azure セキュリティ ベンチマーク」の監査で、1周が 2300 秒級。" -ForegroundColor Red
  Write-Host "     これがいると、他の割り当ての自己修復が数十分止まります。" -ForegroundColor Red
  Write-Host "     イニシアチブのパラメータ設定を確認してください。" -ForegroundColor Red
} else {
  Write-Host "  1本ずつ順番に回っています。1件あたり1分弱。詰まりはありません。" -ForegroundColor Green
  Write-Host "" 
  Write-Host "  準備中はここに 1周 2321秒（38分41秒）の監査が居座っていて、" -ForegroundColor Gray
  Write-Host "  他の割り当ての自己修復を丸ごと止めていました。" -ForegroundColor Gray
  Write-Host "  今日のデモに限って一時的に無効にしてあります（本番で外すものではありません）。" -ForegroundColor DarkGray
}
Write-Host ""
Write-Host "  ※ 時刻が途中で飛んで見えるのは、タイムゾーンが壊れているからです。" -ForegroundColor DarkGray
Write-Next "D7-recover.ps1" "詰まりを解消する"
