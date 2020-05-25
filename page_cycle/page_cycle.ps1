# Cycle through web pages depending on a config file
# - 24/01/2020 Simon

# Parse settings
$config = Get-Content -Raw -Path .\config.json | ConvertFrom-Json

# Enable logging if required
if ($config.config.logging -eq "True") {
    Start-Transcript -Path .\log.txt
}

# Open internet explorer browser for each web page and store relevant data
$data = @()
foreach ($webpage in $config.webpages) {
    # Open browser and create window object
    Write-Output("($(Get-Date)) Opening browser for $($webpage.url)")
    $window = new-object -ComObject "InternetExplorer.Application"
    $window.navigate($webpage.url)
    $window.Visible = $true
    if ($config.config.full_screen -eq "True") {
        $window.FullScreen = $true
    }

    # Create custom browser object to hold webpage specific data
    $browser = New-Object -TypeName psobject
    $browser | Add-Member -MemberType NoteProperty -Name Window -Value $window
    $browser | Add-Member -MemberType NoteProperty -Name CycleTime -Value $webpage.time
    $browser | Add-Member -MemberType NoteProperty -Name RefreshCycles -Value $webpage.refresh_cycles
    $browser | Add-Member -MemberType NoteProperty -Name CurrentCycles -Value 0
    
    # Add to the data array
    $data += $browser
}

Write-Output("($(Get-Date)) Data objects created")
Write-Output($data)

# Start cycling through the browsers
while ($true) {
    foreach ($browser in $data) {
        Write-Output("($(Get-Date)) Opening window $($browser.Window.LocationName) for $($browser.CycleTime) seconds")
        # Activate the correct window and sleep for the specified time
        (New-Object -ComObject WScript.Shell).AppActivate($browser.Window.LocationName)
        Start-Sleep -Seconds ($browser.CycleTime)
        # Check if we need to refresh the page while its in the background
        # Do not bother if "refresh_cycles" is set to 0
        if ($browser.RefreshCycles -gt 0) {
            $browser.CurrentCycles += 1
            if ($browser.CurrentCycles -ge $browser.RefreshCycles) {
                Write-Output("($(Get-Date)) Refreshing $($browser.Window.LocationURL)")
                $browser.Window.refresh()
            }
        }
    }
}
