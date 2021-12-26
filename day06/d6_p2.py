#! /usr/bin/env python3

import numpy as np

from d6_utils import load_data


timers = load_data()

tally = np.zeros(9)
values, counts = np.unique(timers, return_counts=True)
tally[values] = counts

for i in range(256):
    to_reset = tally[0]
    # Shift every timer down one
    tally[:-1] = tally[1:]
    # Reset to 6 days
    tally[6] += to_reset
    # Birth new juveniles
    tally[8] = to_reset

# Print solution
print(f"After 256 days there would be {int(tally.sum())} lanternfish.")
