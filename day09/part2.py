#! /usr/bin/env python3

import numpy as np

from utils import load_data, get_min_mask, pad_array


def expand_basin(point, padded_heights, basin):
    """Add point to basin and recursively traverse."""
    # Append point to list of points in basin
    if point not in basin:
        basin.append(point)

    # Get height of current point
    point_height = padded_heights[point[0] + 1, point[1] + 1]

    # Compute co-ordinates of this point's neighbours
    neighbours = (point + np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])).tolist()
    # Loop over neighbours
    for neighbour in neighbours:
        # If point already captured, skip
        if neighbour in basin:
            continue
        # Height of neighbour
        neighbour_height = padded_heights[neighbour[0] + 1, neighbour[1] + 1]
        # If point is in basin
        if neighbour_height > point_height and neighbour_height not in (np.inf, 9):
            # Recurse!
            basin = expand_basin(neighbour, padded_heights, basin=basin)

    return basin


def main():
    # Load data
    heights = load_data()

    # Get boolean mask identifying low points
    min_mask = get_min_mask(heights)
    # Create list of arrays, where each array contains points in the basin
    minima = [list(point) for point in np.argwhere(min_mask)]

    # Pad heights with np.inf's for easier handling of edges
    padded_heights = pad_array(heights)

    # Create a basin entry for each minima
    basins = [0] * len(minima)
    # Loop over each minima
    for i, point in enumerate(minima):
        # Comput all points in basin around minima
        basins[i] = expand_basin(point, padded_heights, basin=[])

    # Compute product of size of 3 largest basins
    product = 1
    for basin in sorted(basins, key=len, reverse=True)[:3]:
        product *= len(basin)

    # Print solution
    print(f"The product of the 3 largest basin sizes multiplied together is {product}.")
    return product


if __name__ == "__main__":
    main()
