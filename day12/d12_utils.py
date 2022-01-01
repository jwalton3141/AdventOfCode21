import numpy as np


def load_data():
    """Read Day 12 puzzle input into dictionary."""
    with open("d12_input.txt") as f:
        data = f.read().splitlines()
    # Split data into list of tuples
    passages = [(edge.split("-")[0], edge.split("-")[1]) for edge in data]

    # Create dictionary to store data
    cave_map = {cave: [] for cave in np.unique(passages)}
    # Loop over edges
    for from_cave, to_cave in passages:
        # Can't travel back to start or anywhere after end
        if "start" != to_cave and "end" != from_cave:
            cave_map[from_cave].append(to_cave)

        # Can't travel back to start or anywhere after end
        if "start" != from_cave and "end" != to_cave:
            cave_map[to_cave].append(from_cave)

    return cave_map


def get_paths_from(
    cave, cave_map, paths=[], traverse_attempt=[], max_visits=1, target="end"
):
    """Follow the cave_map to get paths from 'cave' to the exit"""
    # Make a copy of current traverse attempt
    traverse = traverse_attempt.copy()
    # Record move
    traverse.append(cave)

    # Get adjacent caves
    adjacent_caves = cave_map[cave]
    # Get list of small caves already visited

    visited_small_caves = [cave for cave in traverse if is_small_cave(cave)]
    # Count visits of small caves
    _, counts = np.unique(visited_small_caves, return_counts=True)

    # Apply max small cave visit rule
    if np.any(counts >= max_visits):
        # Valid moves are adjacent caves, with small caves not visited twice
        valid_moves = set(adjacent_caves) - set(visited_small_caves)
    else:
        valid_moves = adjacent_caves

    # If there are valid moves, continue exploration
    if valid_moves:
        for move in valid_moves:
            # Recurse
            paths = get_paths_from(
                move,
                cave_map,
                paths=paths,
                traverse_attempt=traverse,
                max_visits=max_visits,
                target=target,
            )
    # If traverse was successful
    elif cave == target:
        paths.append(traverse)

    return paths


def is_small_cave(cave):
    """Return True if cave is 'small' and False if cave is 'large'."""
    return cave.lower() == cave
