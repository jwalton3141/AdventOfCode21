import pandas as pd


def load_data():
    """Read Day 2 puzzle input into pandas DataFrame."""
    return pd.read_csv("input.txt",
                       sep=" ",
                       header=None,
                       names=["direction", "distance"])
