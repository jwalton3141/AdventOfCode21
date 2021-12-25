import numpy as np
import pandas as pd


def load_data():
    """Read Day 4 puzzle input into pandas DataFrame."""
    return load_calls(), load_boards()


def load_calls():
    """Read bingo calls into DataFrame."""
    return pd.read_csv("d4_input_calls.csv", header=None)


def load_boards():
    """Read bingo cards into numpy array."""
    # Read all boards into a single DataFrame
    df = pd.read_fwf("d4_input_boards.csv", header=None).dropna()
    # Convert DataFrame into numpy array with shape (number of boards, 5, 5)
    boards = df.to_numpy().reshape(df.shape[0] // 5, 5, 5)
    return boards


def get_win_status(boards):
    """Check boards for win."""
    # Sum every board's rows and columns
    col_row_sums = np.dstack([boards.sum(1), boards.sum(2)])
    # Check for winning rows and columns over all boards
    win_status = np.any(col_row_sums == -5, axis=(1, 2))
    return win_status
