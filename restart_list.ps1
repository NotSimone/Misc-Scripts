Start-Transcript -Path .\log.txt

$Computers = Get-Content .\list.txt
Restart-Computer -ComputerName $Computers -Force

Stop-Transcript