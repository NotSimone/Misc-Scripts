# Test the ntp server to see if its stable

import ntplib, time
from datetime import datetime, timezone

print("Starting NTP Monitoring")

c = ntplib.NTPClient()

server = ["time2.google.com"]

while (True):

    time.sleep(5)

    for x in server:
        try:
            response = c.request(x, version=3)
        except:
            # Check connection
            print(f"Failed to connect to {x} at {datetime.now()}")
        # Check accuracy
        current_time = datetime.now()
        ntp_time = datetime.fromtimestamp(response.tx_time)
        t_delta = abs(current_time - ntp_time)
        if t_delta.total_seconds() > 1:
            print(f"NTP Server {x} Drift: {current_time} (Current) vs {ntp_time} (NTP)")    
    
