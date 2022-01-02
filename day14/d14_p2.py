#! /usr/bin/env python3

import numpy as np

from d14_utils import load_data


def step(pair_counts):
    """Update counts of pairs to simulate a growth step."""
    # Make a copy to allow instantaneous updates
    updated_pair_counts = pair_counts.copy()
    # Loop over pairs
    for pair in pair_counts.keys():
        # Increase counts for newly formed pairs
        updated_pair_counts[pair[0] + rules[pair]] += pair_counts[pair]
        updated_pair_counts[rules[pair] + pair[1]] += pair_counts[pair]
        # Decrease count for interrupted pair
        updated_pair_counts[pair] -= pair_counts[pair]
    return updated_pair_counts


# Load puzzle input
polymer, rules = load_data()

# Create dictionary to record frequency of each pair
pair_counts = dict(zip(rules.keys(), [0] * len(rules)))
# Count pair occurences in initial state
for i in range(len(polymer) - 1):
    pair_counts[polymer[i : i + 2]] += 1

# Grow polymer 40 times
for i in range(40):
    pair_counts = step(pair_counts)

# Get component characters
chars = np.unique(list("".join(pair_counts.keys())))
# Create dictionary to record frequency of each character
char_counts = dict(zip(chars, [0] * len(chars)))

# Loop over pairs and update character count (as pairs overlap this will count
# each character twice!)
for pair in pair_counts.keys():
    char_counts[pair[0]] += pair_counts[pair]
    char_counts[pair[1]] += pair_counts[pair]

# Account for no double counting of characters at start and end of polymer
char_counts[polymer[0]] += 1
char_counts[polymer[-1]] += 1

char_counts = np.array(list(char_counts.values()))
# Subtract most common count from least common count (divide by two to account
# for double-counting)
answer = np.ptp(char_counts) / 2

print(
    f"If you take the quantity of the most common element and subtract the quantity of the least common element you get {int(answer)}."
)
