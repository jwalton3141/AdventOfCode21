from itertools import product
import numpy as np


def load_data():
    """Read Day 11 puzzle input into numpy array."""
    with open("input.txt") as f:
        data = f.read().splitlines()
    # Convert to numpy array
    data = np.array([list(row) for row in data], dtype=int)
    return data


def get_neighbour_ind(pos):
    """Get locations of neighbours around pos."""
    return (pos + list(product([0, 1, -1], [0, 1, -1])))[1:]


def pad_array(energies, value=-np.inf):
    """Pad array for easier handling of edges."""
    padded_energies = np.ones((energies.shape[0] + 2, energies.shape[1] + 2)) * value
    padded_energies[1:-1, 1:-1] = energies
    return padded_energies


def flash(energies, flashed, count):
    """Octos with energy > 9 flash and increment neighbour energy."""
    # Increment counter
    count += (energies[~flashed] > 9).sum()

    # Loop over flashers
    for octo in np.argwhere(energies > 9):
        # If octo has already flashed, skip
        if flashed[octo[0], octo[1]]:
            continue

        # Increment neighbour energy
        neighbours = get_neighbour_ind(octo)
        energies[neighbours[:, 0], neighbours[:, 1]] += 1

        # Note octo as having flashed
        flashed[octo[0], octo[1]] = True

    return energies, flashed, count


def step(energies, count):
    """Model a single step increase."""
    # Increment
    energies += 1
    # Bool tracking which octos have flashed
    flashed = np.zeros(energies.shape, dtype=bool)

    # While energy levels of octos which haven't flashed yet are over 9
    while np.any(energies[~flashed] > 9):
        energies, flashed, count = flash(energies, flashed, count)

    # Reset energy of any flashers to zero
    energies[flashed] = 0

    return energies, count
