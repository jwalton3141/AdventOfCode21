#! /usr/bin/env python3

import numpy as np

from utils import load_data, get_lowest_risk


def main():
    # Load puzzle input
    risk = load_data()
    # Get number of rows and columns
    nrow, ncol = risk.shape

    # Tile risk map
    risk = np.tile(risk, (5, 5))

    # Loop over tiles
    for i in range(5):
        for j in range(5):
            # Extract tile for convenience
            tile = risk[nrow * i : nrow * (i + 1), ncol * j : ncol * (j + 1)]
            # Increment tile by position
            tile += i + j
            # Apply wrapping
            tile[tile > 9] += 1
            tile %= 10
            # Insert tile back in
            risk[nrow * i : nrow * (i + 1), ncol * j : ncol * (j + 1)] = tile

    # Get lowest risk of possible paths
    lowest_risk = get_lowest_risk(risk)

    # Print solution
    print(f"The path with lowest risk has a risk level of {lowest_risk}.")
    return lowest_risk


if __name__ == "__main__":
    main()
