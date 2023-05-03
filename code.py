"""Main code for demo cube

Intended operation:

- Post temp and pressure at set times from the hour, every hour
  - Allow bogus values to be posted for testing at other times
- Otherwise listen continuously for beacon messages and post them immediately
- Check for code updates once every hour
"""

import servercom
from servercom import irrx
import time

# Set up the server communication object
a=servercom.Connection()

while True:
    if time.time() % 1000 == 0:
        a.code_update()
    msg=irrx.receive()
    if msg:
        a.post(servercom.BeaconChallenge(msg.text))
    time.sleep(0.1)
