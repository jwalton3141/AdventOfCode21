#! /usr/bin/env python3

from d2_utils import load_data


# Read input data
instructions = load_data()

# Pivot by direction
direction = instructions.pivot(columns="direction", values="distance").fillna(0)

# Compute the aim at each step
direction["aim"] = (direction["down"] - direction["up"]).cumsum()

# Horizontal displacment
h = direction["forward"].sum()
# Vertical displacement
v = (direction["aim"] * direction["forward"]).sum()

# Print solution
print(f"The product of the horizonal and vertical displacement is: {int(h * v)}.")
