import numpy as np


def load_data():
    """Read Day 9 puzzle input into numpy array."""
    with open("input.txt") as f:
        data = f.read().splitlines()
    # Convert to numpy array
    data = np.array([list(row) for row in data], dtype=int)
    return data


def is_minima(heights, row, col):
    """Return True is heights[row, col] is smaller than all neighbours' heights."""
    neighbour_heights = np.array(
        [
            heights[row - 1, col],
            heights[row + 1, col],
            heights[row, col - 1],
            heights[row, col + 1],
        ]
    )
    return np.all(heights[row, col] < neighbour_heights)


def pad_array(heights, value=np.inf):
    """Pad array for easier handling of edges."""
    padded_heights = np.ones((heights.shape[0] + 2, heights.shape[1] + 2)) * value
    padded_heights[1:-1, 1:-1] = heights
    return padded_heights


def get_min_mask(heights):
    """Create boolean mask locating minima."""
    # Pad array with np.inf's for handling edges
    padded_heights = pad_array(heights)

    # Create boolean mask representing whether a point is a minima
    min_mask = np.zeros(heights.shape, dtype=bool)

    # Loop over rows and columns
    for i in range(heights.shape[0]):
        for j in range(heights.shape[1]):
            min_mask[i, j] = is_minima(padded_heights, i + 1, j + 1)

    return min_mask
