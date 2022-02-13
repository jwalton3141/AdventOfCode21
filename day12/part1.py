#! /usr/bin/env python3

from utils import load_data, get_paths_from


def main():
    # Load puzzle input
    cave_map = load_data()

    # Realise all possible paths through cave system
    paths = get_paths_from("start", cave_map)

    num_paths = len(paths)
    # Print solution
    print(
        f"There are {num_paths} paths through this cave system that visit small caves at most once."
    )
    return num_paths


if __name__ == "__main__":
    main()
