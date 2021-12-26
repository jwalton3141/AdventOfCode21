#! /usr/bin/env python3

import numpy as np

from d6_utils import load_data


timers = load_data()

for day in range(80):
    # Count down
    timers -= 1
    # Bool representing which timers to reset
    to_reset = timers == -1
    # Reset any timers which hit -1
    timers[to_reset] = 6
    # Add juvenlies
    timers = np.hstack([timers, np.ones(to_reset.sum()) * 8])

# Print solution
print(f"After 80 days there would be {len(timers)} lanternfish.")
