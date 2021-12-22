import pandas as pd


def load_data():
    """Read Day 2 puzzle input into pandas DataFrame."""
    return pd.read_csv("d2_input.csv",
                       sep=" ",
                       header=None,
                       names=["direction", "distance"])
