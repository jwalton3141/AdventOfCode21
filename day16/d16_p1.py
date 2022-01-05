#! /usr/bin/env python3

from d16_utils import Transmission


transmission = Transmission()
transmission.decode()

print(f"The versions in the transmission packets sum to: {transmission.version_sum}.")
