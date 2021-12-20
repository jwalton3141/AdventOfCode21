#! /usr/bin/env python3

from d1_utils import load_data


# Read input data
depths = load_data()

# Count the number of times the depth increases
step_downs = (depths.diff() > 0).sum()[0]

# Print solution
print(f"The depth measurement increases {step_downs} times.")
