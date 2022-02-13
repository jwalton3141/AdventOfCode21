#! /usr/bin/env python3

from utils import load_data


def main():
    # Read input data
    depths = load_data()

    # Count the number of times the depth increases, per rolling window
    windowed_step_downs = (depths.rolling(window=3).sum().diff() > 0).sum()[0]

    # Print solution
    print(f"The windowed depth measurement increases {windowed_step_downs} times.")

    return windowed_step_downs


if __name__ == "__main__":
    main()
