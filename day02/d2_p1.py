#! /usr/bin/env python3

from d2_utils import load_data


# Read input data
instructions = load_data()

# Compute total distance travelled in each direction
summed = instructions.groupby("direction").sum()

# Compute product of horizontal and vertical movement
hv_product = summed.loc["forward"] * (summed.loc["down"] - summed.loc["up"])

# Print solution
print(f"The product of the horizonal and vertical displacement is: {hv_product[0]}.")
