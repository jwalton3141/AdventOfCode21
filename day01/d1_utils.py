import pandas as pd


def load_data():
    """Read Day 1 puzzle input into pandas DataFrame."""
    return pd.read_csv("d1_input.csv", header=None)
