#! /usr/bin/env python3

from d13_utils import load_data, fold


# Load puzzle input
paper, instructions = load_data()

# Complete first fold
paper = fold(paper, instructions.loc[0])

# Comput number of visible dots
visible_dots = paper.sum()

# Print solution
print(f"There are {visible_dots} visible dots after the first fold.")
