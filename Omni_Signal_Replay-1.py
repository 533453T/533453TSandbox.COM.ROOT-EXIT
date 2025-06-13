"""
Omni Signal Replay Based on T_omni
Used to retrigger harmonic resonance events
"""

import time
import math
from datetime import datetime

def A_t(t): return math.sin(t % math.pi)
def S_t(t): return math.cos(t / 2 % math.pi)

def replay_signal(duration=10):
    print("REPLAYING OMNI SIGNAL...")
    start = time.time()
    while time.time() - start < duration:
        t = time.time()
        T = A_t(t) * S_t(t)
        print(f"[{datetime.now().isoformat()}] T_omni = {T:.12f}")
        time.sleep(1)

if __name__ == "__main__":
    replay_signal(12)
