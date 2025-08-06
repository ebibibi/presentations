// Azure Arc 接続済み Windows VM の構成管理サンプル
// 対象: /subscriptions/b473fbab-9437-4a52-a769-77205d01eb83/resourceGroups/onpre-vms/providers/Microsoft.HybridCompute/machines/hccjp

@description('Azure Arc マシンの名前')
param machineName string = 'hccjp'

@description('Azure Arc マシンのロケーション')
param location string = resourceGroup().location

// 既存の Azure Arc マシンを参照
resource arcMachine 'Microsoft.HybridCompute/machines@2025-02-19-preview' existing = {
  name: machineName
}

// 1. Azure Monitor エージェントの導入
resource monitoringExtension 'Microsoft.HybridCompute/machines/extensions@2025-02-19-preview' = {
  parent: arcMachine
  name: 'AzureMonitorWindowsAgent'
  location: location
  properties: {
    publisher: 'Microsoft.Azure.Monitor'
    type: 'AzureMonitorWindowsAgent'
    typeHandlerVersion: '1.0'
    autoUpgradeMinorVersion: true
    enableAutomaticUpgrade: true
    settings: {}
  }
}

// 2. カスタムスクリプト拡張機能（ソフトウェアインストール例）
resource customScriptExtension 'Microsoft.HybridCompute/machines/extensions@2025-02-19-preview' = {
  parent: arcMachine
  name: 'CustomScriptExtension'
  location: location
  properties: {
    publisher: 'Microsoft.Compute'
    type: 'CustomScriptExtension'
    typeHandlerVersion: '1.10'
    autoUpgradeMinorVersion: true
    settings: {
      commandToExecute: 'powershell.exe -ExecutionPolicy Unrestricted -Command "& {Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString(\'https://community.chocolatey.org/install.ps1\')); choco install notepadplusplus -y; Write-Output \'Notepad++ をインストールしました\'}"'
    }
  }
}

// 3. システム情報収集スクリプト
resource systemInfoCommand 'Microsoft.HybridCompute/machines/runCommands@2025-02-19-preview' = {
  parent: arcMachine
  name: 'SystemInfoCollection'
  location: location
  properties: {
    source: {
      script: '''
        # システム情報を収集
        $computerInfo = Get-ComputerInfo
        $osInfo = @{
          ComputerName = $computerInfo.CsName
          OSName = $computerInfo.OsName
          OSVersion = $computerInfo.OsVersion
          LastBootTime = $computerInfo.OsLastBootUpTime
          TotalPhysicalMemory = [math]::Round($computerInfo.TotalPhysicalMemory/1GB, 2)
        }
        
        # サービス状態を確認
        $services = Get-Service | Where-Object {$_.Status -eq 'Running'} | Select-Object Name -First 10
        
        # ディスク使用量
        $disks = Get-WmiObject -Class Win32_LogicalDisk | Select-Object DeviceID, @{Name="Size(GB)";Expression={[math]::Round($_.Size/1GB,2)}}, @{Name="FreeSpace(GB)";Expression={[math]::Round($_.FreeSpace/1GB,2)}}
        
        Write-Output "=== システム情報 ==="
        $osInfo | ConvertTo-Json
        
        Write-Output "`n=== 実行中サービス (上位10) ==="
        $services | ConvertTo-Json
        
        Write-Output "`n=== ディスク使用量 ==="
        $disks | ConvertTo-Json
      '''
    }
    timeoutInSeconds: 300
    runAsUser: 'SYSTEM'
    asyncExecution: false
  }
}

// 4. セキュリティ設定適用スクリプト
resource securityConfigCommand 'Microsoft.HybridCompute/machines/runCommands@2025-02-19-preview' = {
  parent: arcMachine
  name: 'ApplySecurityConfig'
  location: location
  dependsOn: [systemInfoCommand]
  properties: {
    source: {
      script: '''
        # Windows Firewall の有効化
        Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
        Write-Output "Windows Firewall を有効化しました"
        
        # Windows Defender の基本設定
        Set-MpPreference -DisableRealtimeMonitoring $false
        Write-Output "Windows Defender リアルタイム保護を有効化しました"
        
        # イベントログサイズの設定
        wevtutil sl Application /ms:32768000
        wevtutil sl System /ms:32768000
        Write-Output "イベントログサイズを設定しました"
        
        # RDP を無効化（セキュリティ強化）
        Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 1
        Write-Output "リモートデスクトップを無効化しました"
        
        Write-Output "セキュリティ設定の適用が完了しました"
      '''
    }
    timeoutInSeconds: 600
    runAsUser: 'SYSTEM'
    asyncExecution: false
  }
}

// 5. IIS インストールスクリプト（Windows機能管理の例）
resource iisInstallCommand 'Microsoft.HybridCompute/machines/runCommands@2025-02-19-preview' = {
  parent: arcMachine
  name: 'InstallIIS'
  location: location
  dependsOn: [securityConfigCommand]
  properties: {
    source: {
      script: '''
        # IIS の機能を確認
        $iisFeature = Get-WindowsFeature -Name Web-Server
        
        if ($iisFeature.InstallState -eq 'Installed') {
          Write-Output "IIS は既にインストールされています"
        } else {
          Write-Output "IIS をインストールしています..."
          Install-WindowsFeature -Name Web-Server -IncludeManagementTools
          Install-WindowsFeature -Name Web-Common-Http
          Write-Output "IIS のインストールが完了しました"
          
          # デフォルトページの作成
          $htmlContent = @"
<!DOCTYPE html>
<html>
<head>
    <title>Azure Arc Demo Server</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 50px; }
        .header { color: #0078d4; }
    </style>
</head>
<body>
    <h1 class="header">Azure Arc で管理されたサーバー</h1>
    <p>このサーバーは Azure Arc により管理されています。</p>
    <p>デプロイ日時: $(Get-Date -Format 'yyyy年MM月dd日 HH:mm:ss')</p>
</body>
</html>
"@
          $htmlContent | Out-File -FilePath "C:\inetpub\wwwroot\index.html" -Encoding UTF8
          Write-Output "カスタムホームページを作成しました"
        }
        
        # IIS サービスの状態確認
        $iisService = Get-Service -Name W3SVC -ErrorAction SilentlyContinue
        if ($iisService) {
          Write-Output "IIS サービス状態: $($iisService.Status)"
        }
      '''
    }
    timeoutInSeconds: 900
    runAsUser: 'SYSTEM'
    asyncExecution: false
  }
}

// 6. ソフトウェア自動インストールスクリプト（Chocolatey使用例）
resource softwareInstallCommand 'Microsoft.HybridCompute/machines/runCommands@2025-02-19-preview' = {
  parent: arcMachine
  name: 'InstallSoftware'
  location: location
  dependsOn: [iisInstallCommand]
  properties: {
    source: {
      script: '''
        # Chocolatey のインストール確認
        $chocoPath = Get-Command choco -ErrorAction SilentlyContinue
        
        if (-not $chocoPath) {
          Write-Output "Chocolatey をインストールしています..."
          Set-ExecutionPolicy Bypass -Scope Process -Force
          [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
          Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
          Write-Output "Chocolatey のインストールが完了しました"
        } else {
          Write-Output "Chocolatey は既にインストールされています"
        }
        
        # 便利なツールのインストール（例）
        $tools = @('notepadplusplus', 'git', '7zip')
        
        foreach ($tool in $tools) {
          try {
            Write-Output "$tool をインストール中..."
            choco install $tool -y --limit-output
            Write-Output "$tool のインストールが完了しました"
          } catch {
            Write-Output "$tool のインストールに失敗しました: $($_.Exception.Message)"
          }
        }
        
        Write-Output "ソフトウェアインストールが完了しました"
      '''
    }
    timeoutInSeconds: 1800
    runAsUser: 'SYSTEM'
    asyncExecution: false
  }
}

// 出力
output arcMachineId string = arcMachine.id
output monitoringExtensionId string = monitoringExtension.id
output customScriptExtensionId string = customScriptExtension.id
output systemInfoCommandId string = systemInfoCommand.id
output securityConfigCommandId string = securityConfigCommand.id
output iisInstallCommandId string = iisInstallCommand.id
output softwareInstallCommandId string = softwareInstallCommand.id