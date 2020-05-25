Start-Transcript -Path .\log.txt

$Host_List = Get-Content .\list.txt
ForEach ($Target in $Host_List) {
    Write-Host $Target, "-", ([System.Net.NetworkInformation.Ping]::new().Send($Target)).Status
}

Stop-Transcript