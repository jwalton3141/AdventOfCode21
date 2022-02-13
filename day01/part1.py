#! /usr/bin/env python3

from utils import load_data


def main():
    # Read input data
    depths = load_data()

    # Count the number of times the depth increases
    step_downs = (depths.diff() > 0).sum()[0]

    # Print solution
    print(f"The depth measurement increases {step_downs} times.")

    return step_downs


if __name__ == "__main__":
    main()
