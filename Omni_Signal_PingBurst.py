"""
Omni Signal Ping Burst
Phase 5: Transdimensional satellite pings across theoretical locations
"""

import math, time
from datetime import datetime

def omni_ping_signature(t):
    return round(abs(math.sin(t) * math.cos(t / 3)) * 777, 7)

def ping_all_locations(cycles=33):
    print(":: OMNI SIGNAL PING BURST ACTIVE ::")
    for _ in range(cycles):
        t = time.time()
        ping = omni_ping_signature(t)
        print(f"[{datetime.now().isoformat()}] PING VALUE :: {ping}")
        time.sleep(0.75)

if __name__ == "__main__":
    ping_all_locations()
