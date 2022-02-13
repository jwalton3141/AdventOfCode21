#! /usr/bin/env python3

import numpy as np

from utils import load_data


def step(polymer, rules):
    """Apply one step of rules to the polymer."""
    for i in range(len(polymer) - 1):
        polymer = (
            polymer[: 2 * i + 1]
            + rules[polymer[2 * i : 2 * i + 2]]
            + polymer[2 * i + 1 :]
        )
    return polymer


def main():
    # Load puzzle input
    polymer, rules = load_data()
    
    # Apply 10 update steps
    for i in range(10):
        polymer = step(polymer, rules)
    
    # Count occurences of each letter
    _, counts = np.unique(list(polymer), return_counts=True)
    
    # Subtract most common count from least common count
    answer = np.ptp(counts)
    
    # Print solution
    print(
        f"If you take the quantity of the most common element and subtract the quantity of the least common element you get {answer}."
    )
    return answer


if __name__ == "__main__":
    main()
