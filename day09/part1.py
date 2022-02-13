#! /usr/bin/env python3

import numpy as np

from utils import load_data, get_min_mask


def main():
    # Load data
    heights = load_data()

    # Get boolean mask identifying low points
    min_mask = get_min_mask(heights)

    # Compute risk
    total_risk = (heights[min_mask] + 1).sum()

    # Print solution
    print(f"The sum of the risk levels of all low points is {total_risk}.")
    return total_risk


if __name__ == "__main__":
    main()
