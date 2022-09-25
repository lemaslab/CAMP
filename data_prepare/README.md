# CAMP: a Convolutional Attention-based Neural Network for Multi-level Peptide-protein Interaction Prediction

CAMP is a sequence-based deep learning framework for multifaceted prediction of peptide-protein interactions, including not only binary peptide-protein interactions, but also corresponding peptide binding residues.

### CAMP
#### 1. navigate to /data_prepare directory  
```
cd ~/CAMP/data_prepare/
```

#### PLIP Dockerhub: https://hub.docker.com/r/pharmai/plip
```
docker pull pharmai/plip
```

#### Run PLIP
```
docker run -v ${PWD}:/results -w /results pharmai/plip:latest -i 1A0M -yv

docker run -v ${PWD}:/results -w /results pharmai/plip:latest -i 1A0M --peptides A -vx
```