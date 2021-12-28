# Map open paren to closing
pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}


def load_data():
    """Read Day 10 puzzle input into ."""
    with open("d10_input.csv") as f:
        data = f.read().splitlines()
    return data


def parse(line):
    """Loop over characters in line. If line is legal return True and list of
    any open chunks. If line is not legal return False and illegal
    character."""
    open_chunks = []
    # Loop over parentheses in line
    for char in line:
        # If opening chunk
        if char in "([{<":
            # Append to opened chunks
            open_chunks.append(char)
        # If closing a chunk
        elif char == pairs[open_chunks[-1]]:
            # Remove from list of chunks still open
            open_chunks = open_chunks[:-1]
        else:
            return False, char

    return True, open_chunks
