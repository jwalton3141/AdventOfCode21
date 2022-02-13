#! /usr/bin/env python3

import numpy as np

from utils import load_data, parse, pairs


def main():
    # Load data
    lines = load_data()
    
    # List to store missing closers
    chunks_to_close = []
    # Loop over lines
    for line in lines:
        legal, out = parse(line)
        if legal:
            chunks_to_close.append(out)
    
    # Compute missing characters to close all chunks
    missing = [[pairs[char] for char in chunk[::-1]] for chunk in chunks_to_close]
    
    # Points associated with each character
    score_sheet = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = [0] * len(missing)
    for i, line in enumerate(missing):
        for char in line:
            scores[i] *= 5
            scores[i] += score_sheet[char]
    
    middle_score = int(np.median(scores))
    
    # Print solution
    print(f"The middle score is {middle_score}.")
    return middle_score


if __name__ == "__main__":
    main()
