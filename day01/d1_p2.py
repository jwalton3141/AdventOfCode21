#! /usr/bin/env python3

from d1_utils import load_data


# Read input data
depths = load_data()

# Count the number of times the depth increases, per rolling window
windowed_step_downs = (depths.rolling(window=3).sum().diff() > 0).sum()[0]

# Print solution
print(f"The windowed depth measurement increases {windowed_step_downs} times.")
