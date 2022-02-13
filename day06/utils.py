import pandas as pd


def load_data():
    """Read Day 6 puzzle input into numpy array."""
    return pd.read_csv("input.csv", header=None).to_numpy()[0]
