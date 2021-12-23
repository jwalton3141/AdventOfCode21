#! /usr/bin/env python3

from d3_utils import load_data, row2bin


# Load input data
binaries = load_data()

# Compute the mode of each column
gamma_row = binaries.mode().values[0]
# Compute epsilon as the inverse of gamma
epsilon_row = (gamma_row + 1) % 2

# Compute power from gamma and epsilon
power = row2bin(gamma_row) * row2bin(epsilon_row)

# Print solution
print(f"The power consumption of the engine is: {power}.")
