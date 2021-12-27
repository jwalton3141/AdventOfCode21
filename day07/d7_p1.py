#! /usr/bin/env python3

import numpy as np

from d7_utils import load_data


positions = load_data()

# The optimum position for individuals to align at is represented by the median
best_position = np.median(positions)
# Fuel consumed gettting everyone in line
fuel_consumption = np.abs(positions - best_position).sum()

# Print solution
print(
    f"The crabs must expend a minimum of {int(fuel_consumption)} units of fuel to align."
)
