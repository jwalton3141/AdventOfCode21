#! /usr/bin/env python3

import numpy as np

from d5_utils import load_data, make_grid


def get_coords(line, delta):
    """Compute coordinates which line passes through."""
    coords = [0, 0]
    for i in 0, 1:
        # If change is non-zero
        if delta[i]:
            # Get range of points
            points = range(line[:, i].min(), line[:, i].max() + 1)
            # Reverse order if needed
            coords[i] = list(points)[:: delta[i] // abs(delta[i])]
        else:
            coords[i] = line[0, i]
    return coords


lines = load_data()
grid = make_grid(lines)

# Compute change in each co-ordinate for every line
deltas = np.diff(lines, axis=1)[:, 0]

# Loop over lines
for line, delta in zip(lines, deltas):
    # Only consider horizontal, vertical and 45 degree lines
    if 0 in delta or abs(delta[0]) == abs(delta[1]):
        # Get coordinates which line passes through
        coords = get_coords(line, delta)
        # Increment grid
        grid[coords[1], coords[0]] += 1

# Count the number of times two or more lines cross
num_mult_overlaps = (grid >= 2).sum()

# Print Solution
print(f"At {num_mult_overlaps} points two or more lines overlap.")
