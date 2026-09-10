. C:\hccjp77\_lab.ps1
Invoke-OnArcwin {
  "--- Configuration\AzureWindowsBaseline CreationTime ---"
  (Get-Item "C:\ProgramData\GuestConfig\Configuration\AzureWindowsBaseline").CreationTime.ToString("yyyy-MM-dd HH:mm:ss")
  "--- its contents ---"
  Get-ChildItem "C:\ProgramData\GuestConfig\Configuration\AzureWindowsBaseline" -Recurse |
    Select-Object -First 12 | ForEach-Object { "  " + $_.Name + "  " + $_.LastWriteTime.ToString("HH:mm:ss") }
  "--- state files under GuestConfig (no logs) ---"
  Get-ChildItem "C:\ProgramData\GuestConfig" -Recurse -Include *.db,*.json,*.sqlite,*.dat -EA SilentlyContinue |
    Where-Object { $_.FullName -notmatch "logs" } |
    Select-Object -First 20 | ForEach-Object { "  " + $_.FullName }
  "--- Arc agent config dir ---"
  Get-ChildItem "C:\ProgramData\AzureConnectedMachineAgent" -Recurse -Include *.db,*.json -EA SilentlyContinue |
    Select-Object -First 15 | ForEach-Object { "  " + $_.FullName }
}

