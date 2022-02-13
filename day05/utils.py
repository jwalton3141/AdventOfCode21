import numpy as np


def make_grid(lines):
    """Return an empty grid for displaying lines."""
    return np.zeros(lines.max(axis=(0, 1)) + 1, dtype=int)


def load_data():
    """Read Day 5 puzzle input into numpy arrays."""
    with open("input.txt") as f:
        lines = f.read()
    # Remove arrow and seperate at spaces
    lines = lines.replace("->", "").split()
    # Split at commas and make into numpy array
    lines = np.array([line.split(",") for line in lines], dtype=int)
    # A single line is stored as a 2x2 array of the form:
    # np.array([[x1, y1],
    #           [x2, y2]])
    # `lines` has 2x2 line entries stacked along a 3rd axis
    return np.stack((lines[::2], lines[1::2]), axis=1)
