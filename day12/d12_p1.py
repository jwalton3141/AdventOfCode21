#! /usr/bin/env python3

from d12_utils import load_data, get_paths_from


# Load puzzle input
cave_map = load_data()

# Realise all possible paths through cave system
paths = get_paths_from("start", cave_map)

# Print solution
print(
    f"There are {len(paths)} paths through this cave system that visit small caves at most once."
)
