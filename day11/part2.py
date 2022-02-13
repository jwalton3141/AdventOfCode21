#! /usr/bin/env python3

import numpy as np

from utils import load_data, pad_array, step


def main():
    # Load data and pad for easier comparisons
    energies = pad_array(load_data())
    
    i = 0
    while not np.all(energies[1:-1, 1:-1] == 0):
        energies, _ = step(energies, 0)
        i += 1
    
    # Print solution
    print(f"The octos all flashed simultaneously at step {i}.")
    return i


if __name__ == "__main__":
    main()
