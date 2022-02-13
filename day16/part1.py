#! /usr/bin/env python3

from utils import Transmission


def main():
    transmission = Transmission()
    transmission.decode()

    ver_sum = transmission.version_sum
    print(f"The versions in the transmission packets sum to: {ver_sum}.")
    return ver_sum


if __name__ == "__main__":
    main()
