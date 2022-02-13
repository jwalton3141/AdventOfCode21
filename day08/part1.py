#! /usr/bin/env python3

from utils import load_data


def main():
    # Split data at | to get outputs only
    outputs = [entry.split(" | ")[1] for entry in load_data()]

    # Split and rejoin so every string is a single entry
    outputs = " ".join(outputs).split(" ")

    count = 0
    # Loop over strings in output
    for output in outputs:
        # If entry is 1, 4, 7 or 8:
        if len(output) in (2, 3, 4, 7):
            count += 1

    # Print solution
    print(f"The digits 1, 4, 7, and 8 appear {count} times in the output")
    return count


if __name__ == "__main__":
    main()
