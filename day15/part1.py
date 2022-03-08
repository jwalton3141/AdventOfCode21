#! /usr/bin/env python3

from utils import load_data, get_lowest_risk


def main():
    # Load puzzle input
    risk = load_data()

    # Get lowest risk of possible paths
    lowest_risk = get_lowest_risk(risk)

    # Print solution
    print(f"The path with lowest risk has a risk level of {lowest_risk}.")
    return lowest_risk


if __name__ == "__main__":
    main()
