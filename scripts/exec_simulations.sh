#!/bin/bash

root=$(git rev-parse --show-toplevel)

simulator="${root}/src/main.py"
plotter="${root}/src/plot/main.py"

outfile="${root}/out/simulation.jsonl"

python3 ${simulator} -l 2 -t 10000.0 -g 1 -q 0.5 -n 5 -d 4 >> ${outfile}
