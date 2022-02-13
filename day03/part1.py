#! /usr/bin/env python3

from utils import load_data, row2bin


def main():
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
    return power


if __name__ == "__main__":
    main()
