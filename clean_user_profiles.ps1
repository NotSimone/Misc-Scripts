# Clear User Profiles
# Ignores system profiles, administrator, and currently logged in users
# Removes the rest

# Get all the user profiles
$profiles = $null
$profiles = Get-WmiObject -class Win32_UserProfile | `
# Filter out special profiles, admin, loaded, and own profile
Where {
(!$_.Special) `
-and ($_.LocalPath -ne "C:\Users\Administrator") `
-and ($_.LocalPath -ne $env:USERPROFILE) `
-and (!$_.Loaded)
}

# Clear the profiles
if ($profiles -ne $null) {

	Write-Output("Removing Profiles:`n")
	foreach($user in $profiles) {
		Write-Output($user.Localpath)
	}

	# Confirmation prompt
	$title = "Continue Removing?"
	$prompt = ""
	$yes = New-Object System.Management.Automation.Host.ChoiceDescription "&Yes","Removes Profiles"
	$no = New-Object System.Management.Automation.Host.ChoiceDescription "&No","Abort"
	$options = [System.Management.Automation.Host.ChoiceDescription[]] ($yes,$no)
	$choice = $host.ui.PromptForChoice($title,$prompt,$options,1)

	if ($choice -eq 1) {
		exit
	} else {
		foreach($user in $profiles) {
			Write-Output("Removing: $($user.Localpath)")
			$user.Delete()
		}
		Write-Output("`nDone")
        [void](Read-Host "Press Enter to Exit")
	}

} else {
	Write-Output("Error: No Valid Profiles Found")
    [void](Read-Host "Press Enter to Exit")
}
