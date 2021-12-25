#! /usr/bin/env python3

import numpy as np

from d4_utils import load_data, get_win_status


# Load input data
calls, boards = load_data()

# Bool representing all board's win status
has_won = np.zeros(len(boards), dtype=bool)

i = 0
# Continue until all boards have won
while not np.all(has_won):
    # Discard any winning boards
    boards = boards[~has_won]

    # Call next number
    call = calls.iloc[0, i]
    # Mark matches on board with a -1
    boards[boards == call] = -1
    # Compute updated win status
    has_won = get_win_status(boards)
    i += 1


losing_board = boards[0]
# Sum unmarked numbers
sum_unmarked = losing_board[losing_board != -1].sum()

# Compute score
score = sum_unmarked * call

# Print solution
print(f"The score on the losing board would be {int(score)}.")
