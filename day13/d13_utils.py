import numpy as np
import pandas as pd


def load_data():
    """Read Day 13 puzzle input."""
    return load_paper(), load_instructions()


def load_paper():
    """Load dots data into numpy array."""
    # Read location of dots in
    dot_locs = pd.read_csv("d13_input_dots.csv", header=None).to_numpy()
    # Create boolean array to represent locations of dots
    paper = np.zeros(dot_locs.max(0)[::-1] + 1, dtype=bool)
    # Set location of dots to True
    paper[dot_locs[:, 1], dot_locs[:, 0]] = True
    return paper


def load_instructions():
    """Load fold data into pandas DataFrame."""
    with open("d13_input_folds.txt") as f:
        data = f.read().splitlines()
    # Strip "fold along " instruction and split direction and location of fold
    instructions = [fold.replace("fold along ", "").split("=") for fold in data]
    return pd.DataFrame(instructions, columns=["direction", "location"])


def fold(paper, instruction):
    """Fold paper according to instruction."""
    # Extract instructions
    direction = instruction["direction"]
    location = int(instruction["location"])

    # Boolean array representing if dimensions are of odd or even length
    odd = np.array(paper.shape) % 2

    if direction == "y":
        # If even pad with False's to make folding easier
        if not odd[0]:
            paper = np.vstack([paper, np.zeros((1, paper.shape[1]))])
        # Simulate folding
        paper = np.logical_or(paper[:location], paper[location + 1 :][::-1])
    else:
        # If even pad with False's to make folding easier
        if not odd[1]:
            paper = np.hstack([paper, np.zeros((paper.shape[0], 1))])
        # Simulating folding
        paper = np.logical_or(paper[:, :location], paper[:, location + 1 :][:, ::-1])

    return paper
