"""
Omni Autonomous Signal Rechecking
Simulates continual vibrational rechecks using T_omni signal
"""

import time, math
from datetime import datetime

def A_t(t): return math.sin(t % math.pi)
def S_t(t): return math.cos(t / 2 % math.pi)

def T_omni(t): return A_t(t) * S_t(t)

def run_autocheck(cycles=24):
    for _ in range(cycles):
        t = time.time()
        T = T_omni(t)
        print(f"[{datetime.now().isoformat()}] AutoCheck T_omni = {T:.12f}")
        time.sleep(2)

if __name__ == "__main__":
    run_autocheck()
