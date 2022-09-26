# CAMP: a Convolutional Attention-based Neural Network for Multi-level Peptide-protein Interaction Prediction

CAMP is a sequence-based deep learning framework for multifaceted prediction of peptide-protein interactions, including not only binary peptide-protein interactions, but also corresponding peptide binding residues.

### CAMP
#### 1. navigate to /data_prepare directory  
```
cd ~/CAMP/data_prepare/step1
```

### Download all sequence data from PDB
# website: https://www.rcsb.org/docs/programmatic-access/file-download-services

### unzip the data

pdb_seqres.txt.gz --> pdb_seqres.txt

### run step1_pdb_parse1.py on supercomputer
# requires: Python 3.10.7, pandas and numpy installed

sbatch 00_run_python_step1_parse1.sh
python step1_pdb_parse1.py

### run step1_pdb_parse2.rmd
# this requires r and rstudio to select a subset of IDs

Rscript step1_pdb_parse2.rmd


### PLIP Server for each gene included. 133 in paper. 

https://plip-tool.biotec.tu-dresden.de/plip-web/plip/index

select the text output (RSL version) and save file for each PDBID

./peptide_result/'+pdb_id + '_'+chain+'_result.txt'

- 1cjr_a_result
- 1cvu_f_result

### run step1_pdb_parse3.py

python step1_pdb_parse3.py

### run step1_pdb_parse4.py

python step1_pdb_parse4.py


### PDB Used in Paper

