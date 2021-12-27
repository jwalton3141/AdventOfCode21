#! /usr/bin/env python3

import numpy as np

from d7_utils import load_data


def move_cost(n):
    """Compute cost of moving n times."""
    return n * (n + 1) / 2


def align_cost(positions, align_at):
    """Compute cost to move from positions to align_at."""
    # Number of moves each individual must make to align
    moves_to_align = np.abs(positions - align_at)
    # Cost of aligning all individuals
    cost_to_align = move_cost(moves_to_align).sum()
    return cost_to_align


positions = load_data()

lowest_cost = np.inf

# Loop over all possible align positions
for align_at in range(positions.min(), positions.max() + 1):
    # Compute cost of aligning all at position
    cost = align_cost(positions, align_at)
    if cost < lowest_cost:
        lowest_cost = cost

# Print solution
print(f"The crabs must expend a minimum of {int(lowest_cost)} units of fuel to align.")
