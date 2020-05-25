== Pagecycle Script ==
Cycles through web pages for various time durations. Written in Powershell.

== Instructions ==
Run the pagecycle.ps1 Powershell script, or if disabled by policy, the start.bat file.
The script will open all the webpages specified in the config.json with internet explorer and start cycling.

== Configuration ==
Configuration is done through the config.json file.
Logging is done to a log.txt file in same directory if logging is set to "true" in "config".
Pages will be open in full screen if "full_screen" is set to "true".
New entries can be added to the "webpages" list and must be objects of the following structure:

"url": "{url to navigate to}"
"time": "{time (seconds) to stay on that page}"
"refresh_cycles": "{how many cycles before a page refresh (set to 0 to disable)}"

The config must follow JSON structure, including curly braces and commas to separate objects.



- 24/01/2020 Simon