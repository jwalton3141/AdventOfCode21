import pandas as pd


def load_data():
    """Read Day 7 puzzle input into numpy array."""
    return pd.read_csv("d7_input.csv", header=None).to_numpy()[0]
