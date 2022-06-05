#! /usr/bin/env python3

from utils import load_data


def main():
    # Read input data
    instructions = load_data()

    # Pivot by direction
    direction = (
        instructions.pivot(columns="direction", values="distance").fillna(0).astype(int)
    )

    # Compute the aim at each step
    direction["aim"] = (direction["down"] - direction["up"]).cumsum()

    # Horizontal displacment
    h = direction["forward"].sum()
    # Vertical displacement
    v = (direction["aim"] * direction["forward"]).sum()
    product = h * v

    # Print solution
    print(f"The product of the horizonal and vertical displacement is: {product}.")
    return product


if __name__ == "__main__":
    main()
