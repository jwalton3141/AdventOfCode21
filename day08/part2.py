#! /usr/bin/env python3

import numpy as np

from utils import load_data


def make_unique_seg_key(entry):
    """Make dict mapping from digit to string, for digits of unique length."""
    # Map from number of segments to digit
    length2digit = {2: 1, 4: 4, 3: 7}

    key = {
        # Map from string to digit
        length2digit[len(string)]: string
        # Loop over unique strings
        for string in np.unique(entry)
        # If string is of length 2, 3 or 4
        if len(string) in length2digit.keys()
    }

    # Eight is always the same
    key[8] = "abcdefg"
    return key


def make_key(entry):
    """Make dict mapping from string to digit."""
    # Map from digit to string for digits of unique length
    key = make_unique_seg_key(entry)

    # Return True if string has n digits in common with digit
    has_n_in_common = (
        lambda string, n, digit: len(set(string).intersection(key[digit])) == n
    )

    # Loop over strings not decoded
    for string in set(np.unique(entry)) - set(key.values()):
        if len(string) == 5:
            if has_n_in_common(string, 2, 1):
                # 3 is the only string of len 5 which has 2 characters in
                # common with 1
                key[3] = string
            elif has_n_in_common(string, 2, 4):
                # 2 is the only string of len 5 which has 2 characters in
                # common with 4
                key[2] = string
            else:
                key[5] = string
        else:
            if has_n_in_common(string, 1, 1):
                # 6 is the only string of len 6 which has 1 characters in
                # common with 1
                key[6] = string
            elif has_n_in_common(string, 4, 4):
                # 9 is the only string of len 6 which has 4 characters in
                # common with 4
                key[9] = string
            else:
                key[0] = string

    # Invert dict (swap keys and values) for decoding
    key = {v: k for k, v in key.items()}
    return key


def decode(entry):
    """Decode output in entry."""
    # Get key mapping from string to digit
    key = make_key(entry)
    # Decode last four entries and join as a single int
    decoded = int("".join([str(key[string]) for string in entry[-4:]]))
    return decoded


def main():
    # Strip | and separate each digit to its own list entry
    entries = [entry.replace("| ", "").split(" ") for entry in load_data()]
    # Sort characters in each string (order doesn't matter)
    entries = [["".join(sorted(word)) for word in entry] for entry in entries]

    # Create array to store decoded outputs
    decoded = np.zeros(len(entries))
    # Loop over entries and decode
    for i, entry in enumerate(entries):
        decoded[i] = decode(entry)

    decoded_sum = int(decoded.sum())
    # Print solution
    print(f"The sum of the decoded output values is: {decoded_sum}.")
    return decoded_sum


if __name__ == "__main__":
    main()
