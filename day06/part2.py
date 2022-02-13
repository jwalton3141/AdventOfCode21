#! /usr/bin/env python3

import numpy as np

from utils import load_data


def main():
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
    num_lanterns = int(tally.sum())
    print(f"After 256 days there would be {num_lanterns} lanternfish.")
    return num_lanterns


if __name__ == "__main__":
    main()
