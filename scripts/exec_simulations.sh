#!/bin/bash

root=$(git rev-parse --show-toplevel)

simulator="${root}/src/main.py"
plotter="${root}/src/plot/main.py"

outdir="${root}/out"
mkdir -p ${outdir}
outfile="${outdir}/simulation.jsonl"

# Simulation constants
length=2
simulation_time=1000.0
gen_const=1
queue_const=0.5
streams=5
dropped=4

python3 ${simulator} \
  -l ${length} \
  -t ${simulation_time} \
  -g ${gen_const} \
  -q ${queue_const} \
  -n ${streams} \
  -d ${dropped} >> ${outfile}
