# CAMP: a Convolutional Attention-based Neural Network for Multi-level Peptide-protein Interaction Prediction

CAMP is a sequence-based deep learning framework for multifaceted prediction of peptide-protein interactions, including not only binary peptide-protein interactions, but also corresponding peptide binding residues.

### CAMP
#### 1. navigate to /data_prepare directory  
```
cd ~/CAMP/data_prepare/
```

## Download all sequence data from PDB
# website: https://www.rcsb.org/docs/programmatic-access/file-download-services

## unzip the data

pdb_seqres.txt.gz --> pdb_seqres.txt

## run step1_pdb_parse1.py
# requires: Python 3.10.7, pandas and numpy installed

python .\step1_pdb_parse1.py

#### PLIP Dockerhub: https://hub.docker.com/r/pharmai/plip
```
docker pull pharmai/plip
```

#### Run PLIP
```
docker run -v ${PWD}:/results -w /results pharmai/plip:latest -i 1A0M -yv

docker run -v ${PWD}:/results -w /results pharmai/plip:latest -i 1A0M --peptides A -vx
```