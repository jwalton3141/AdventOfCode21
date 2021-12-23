import pandas as pd


def load_data():
    """Read Day 3 puzzle input into pandas DataFrame."""
    with open("d3_input.csv") as f:
        binaries = f.read()
    return pd.read_fwf(binaries.splitlines(), header=None)


def row2bin(row):
    """Compute decimal value which values in row represent."""
    # Concatenate values in row
    binstr = "".join(row.astype(str))
    # Convert to an integer (base 2)
    return int(binstr, 2)
