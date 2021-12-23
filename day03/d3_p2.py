#! /usr/bin/env python3

from d3_utils import load_data, row2bin


def get_criteria(binaries, position, get_least=False):
    """Compute criteria for binaries in current position."""
    # Compute criteria for most common
    # The .mean() handles the equally common case
    criteria = binaries[position].mode().values.mean()
    # Handle equally common case
    if criteria == 0.5:
        criteria = 1
    # Flip criteria if least common desired
    return int((criteria + get_least) % 2)


# Read input data
binaries = load_data()

life_support_rating = 1

# get_least = True  represents CO2
# get_least = False represents oxygen
for get_least in True, False:
    # Make a copy of the data for sieving
    sieve_data = binaries.copy()

    # Count from left-most bit
    bit_position = 0
    # While multiple entries remain
    while sieve_data.shape[0] > 1:
        # Compute criteria
        criteria = get_criteria(sieve_data, bit_position, get_least=get_least)
        # Discard entries which don't meet criteria
        sieve_data = sieve_data[sieve_data[bit_position] == criteria]
        # Move one position to the right
        bit_position += 1

    # Increment life support rating
    life_support_rating *= row2bin(sieve_data.values[0])

# Print solution
print(f"The life support rating of the submarine is {life_support_rating}.")
