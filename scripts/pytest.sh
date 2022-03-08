#! /bin/bash

set -e

for day in $(find -type f -name test_solutions.py -exec dirname {} + | sort); do
	echo -e \\nTesting $(basename $day)...; \
	cd $day && pytest ; \
    cd ..; \
done
