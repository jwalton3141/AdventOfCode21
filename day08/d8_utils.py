def load_data():
    """Read Day 8 puzzle input into list."""
    with open("d8_input.csv") as f:
        entries = f.read().splitlines()
    return entries
