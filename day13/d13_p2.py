#! /usr/bin/env python3

import matplotlib.pyplot as plt

from d13_utils import load_data, fold


# Load puzzle input
paper, instructions = load_data()

# Complete first fold
for i, instruction in instructions.iterrows():
    paper = fold(paper, instruction)

# Plot solution
plt.imshow(paper)
# Display solution
plt.show()
