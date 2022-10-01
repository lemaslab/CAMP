#!/bin/bash
#SBATCH --job-name=step1_parse1       #Job name	
#SBATCH --mail-type=END,FAIL          # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=djlemas@ufl.edu   # Where to send mail	
#SBATCH --ntasks=1                    # Run on a single CPU	
#SBATCH --mem=1gb                     # Per processor memory
#SBATCH --time=01:30:00               # Walltime
#SBATCH --output=step1_parse1.%j.out  # Name output file 
pwd; hostname; date

module load python

echo "Running plot script on a single CPU core"

#Run script 
python /blue/djlemas/share/CAMP/data_prepare/step1_pdb_parse1.py

date