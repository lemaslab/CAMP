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

## PDB Used in Paper

histone H3 lysine 9 (PDB ID: 3QO2 [http://doi.org/10.2210/pdb3QO2/pdb])

T3 phosphorylated H3(1-15) peptide (PDB ID: 3UIG [http://doi.org/10.2210/pdb3UIG/pdb])

3IOL

4ZGM

Semaglutide-GlP-1R complex (PDB ID: 4ZGM [http://doi.org/10.2210/pdb4ZGM/pdb]) 

# From READme.txt
1. 下载sequence和residues：crawl.py
2.  生成peptide，receptor的target和query sequence
3.  生成query的sequence vector: query_mapping.py
4.  生成target的sequence vector：target_mapping.py
5. 下载binding inter：download_inter.py
6.  生成matrix:matrix.py