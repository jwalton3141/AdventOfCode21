#! /usr/bin/env python3

from utils import load_data, pad_array, step


def main():
    # Load data and pad for easier comparisons
    energies = pad_array(load_data())

    count = 0
    for i in range(100):
        energies, count = step(energies, count)

    # Print solution
    print(f"After 100 steps there will have been {count} flashes.")
    return count


if __name__ == "__main__":
    main()
