#! /usr/bin/env python3

import networkx as nx

from d15_utils import load_data, get_lowest_risk


# Load puzzle input
risk = load_data()

# Get lowest risk of possible paths
lowest_risk = get_lowest_risk(risk)

# Print solution
print(f"The path with lowest risk has a risk level of {lowest_risk}.")
