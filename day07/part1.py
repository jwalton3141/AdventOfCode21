#! /usr/bin/env python3

import numpy as np

from utils import load_data


def main():
    positions = load_data()

    # The optimum position for individuals to align at is represented by the median
    best_position = np.median(positions)
    # Fuel consumed gettting everyone in line
    fuel_consumption = int(np.abs(positions - best_position).sum())

    # Print solution
    print(
        f"The crabs must expend a minimum of {fuel_consumption} units of fuel to align."
    )
    return fuel_consumption


if __name__ == "__main__":
    main()
