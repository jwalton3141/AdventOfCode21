#! /usr/bin/env python3

import matplotlib.pyplot as plt

from utils import load_data, fold


def main():
    # Load puzzle input
    paper, instructions = load_data()
    
    # Complete first fold
    for i, instruction in instructions.iterrows():
        paper = fold(paper, instruction)
    
    # Plot solution
    plt.imshow(paper)
    # Display solution
    plt.show()


if __name__ == "__main__":
    main()
