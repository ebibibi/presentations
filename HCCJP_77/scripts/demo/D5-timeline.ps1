. C:\hccjp77\demo\_demo.ps1
Write-Title "D5  エージェントのログ ─ 何を、いつ評価したか"
Write-Host "  C:\ProgramData\GuestConfig\arc_policy_logs\gc_agent.log" -ForegroundColor DarkGray
Write-Host ""

Write-Host "【1】読みやすく整形したもの" -ForegroundColor Cyan
Write-Host ""
Invoke-OnArc {
  $log = "C:\ProgramData\GuestConfig\arc_policy_logs\gc_agent.log"
  Get-Content $log -Tail 400 | ForEach-Object {
    if ($_ -match '^\[(?<t>[\d\-: \.]+)\].*Starting consistency for (?<n>\S+)')      { "{0}  評価 開始  {1}" -f $Matches.t.Substring(11,8), $Matches.n }
    elseif ($_ -match '^\[(?<t>[\d\-: \.]+)\].*run_consistency for ''(?<n>[^'']+)'' execution completed in (?<s>\d+) seconds') { "{0}  評価 完了  {1}  ({2} 秒)" -f $Matches.t.Substring(11,8), $Matches.n, $Matches.s }
  } | Select-Object -Last 16
}

Write-Host ""
Write-Host "【2】生のログ（そのまま・直近30行）" -ForegroundColor Cyan
Write-Host "  上の整形は、この中から2種類の行を拾っているだけです。" -ForegroundColor DarkGray
Write-Host "  ────────────────────────────────────────────────────────────" -ForegroundColor DarkGray
Invoke-OnArc {
  Get-Content "C:\ProgramData\GuestConfig\arc_policy_logs\gc_agent.log" -Tail 30
} | ForEach-Object { Write-Host $_ -ForegroundColor DarkGray }
Write-Host "  ────────────────────────────────────────────────────────────" -ForegroundColor DarkGray

Write-Host ""
Write-Host "  ログの時刻がズレて見えたら、それはタイムゾーンが壊れている証拠です。" -ForegroundColor Yellow
Write-Host "  直ると時刻表記も戻ります。" -ForegroundColor Yellow
Write-Next "D6-queue.ps1" "なぜ直らないのか ─ 順番待ちを見る"
