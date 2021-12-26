#! /usr/bin/env python3

import numpy as np

from d5_utils import load_data, make_grid


def get_coords(line, delta):
    """Compute coordinates which line passes through."""
    coord = [
        range(line[:, i].min(), line[:, i].max() + 1) if delta[i] else line[0, i]
        for i in (0, 1)
    ]
    return coord


lines = load_data()
grid = make_grid(lines)

# Compute max - min for each coord in each line
deltas = np.ptp(lines, axis=1)

# Loop over lines
for line, delta in zip(lines, deltas):
    # Only consider horizontal and vertical lines
    if 0 in delta:
        # Get coordinates which line passes through
        coords = get_coords(line, delta)
        # Increment grid
        grid[coords[1], coords[0]] += 1

# Count the number of times two or more lines cross
num_mult_overlaps = (grid >= 2).sum()

# Print Solution
print(f"At {num_mult_overlaps} points two or more lines overlap.")
