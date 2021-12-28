#! /usr/bin/env python3

from d10_utils import load_data, parse


# Load data
lines = load_data()

# List to store illegal characters
illegals = []
# Loop over lines
for line in lines:
    legal, out = parse(line)
    if not legal:
        illegals.append(out)

# Point associated with each character
score_sheet = {")": 3, "]": 57, "}": 1197, ">": 25137}
score = 0
# Tot up score
for illegal in illegals:
    score += score_sheet[illegal]

# Print solution
print(f"The final score is {score}.")
