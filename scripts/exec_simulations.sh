#!/bin/bash

root=$(git rev-parse --show-toplevel)

simulator="${root}/src/main.py"
plotter="${root}/src/plot/main.py"

outdir="${root}/out"
mkdir -p ${outdir}
outfile="${outdir}/simulation.jsonl"

# Simulation constants
length=8
simulation_time=2.0
gen_const=8e-5
queue_const=1.56e-5
lambda_on=5
lambda_off=5
streams=6
dropped=2

python3 ${simulator} \
  -l ${length} \
  -t ${simulation_time} \
  -g ${gen_const} \
  -q ${queue_const} \
  -o ${lambda_on} \
  -f ${lambda_off} \
  -n ${streams} \
  -d ${dropped} >> ${outfile}
