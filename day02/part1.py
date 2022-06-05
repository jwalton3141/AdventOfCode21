#! /usr/bin/env python3

from utils import load_data


def main():
    # Read input data
    instructions = load_data()

    # Compute total distance travelled in each direction
    summed = instructions.groupby("direction").sum().T

    # Compute product of horizontal and vertical movement
    hv_product = (summed["forward"] * (summed["down"] - summed["up"]))[0]

    # Print solution
    print(f"The product of the horizonal and vertical displacement is: {hv_product}.")

    return hv_product


if __name__ == "__main__":
    main()
