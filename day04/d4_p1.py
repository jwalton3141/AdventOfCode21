#! /usr/bin/env python3

import numpy as np

from d4_utils import load_data, get_win_status


# Load input data
calls, boards = load_data()

# Bool representing all board's win status
has_won = np.zeros(len(boards), dtype=bool)

i = 0
# Continue while no winners
while not any(has_won):
    # Call next number
    call = calls.iloc[0, i]
    # Mark matches on board with a -1
    boards[boards == call] = -1
    # Compute updated win status
    has_won = get_win_status(boards)
    i += 1

# Extract the winning board
winning_board = boards[np.where(has_won)][0]
# Sum unmarked numbers
sum_unmarked = winning_board[winning_board != -1].sum()

# Compute score
score = sum_unmarked * call

# Print solution
print(f"The score on the winning board would be {int(score)}.")
