# CAMP: a Convolutional Attention-based Neural Network for Multi-level Peptide-protein Interaction Prediction

CAMP is a sequence-based deep learning framework for multifaceted prediction of peptide-protein interactions, including not only binary peptide-protein interactions, but also corresponding peptide binding residues.

https://download.igb.uci.edu/

# note: We need to install dependencies. https://download.igb.uci.edu/SCRATCH-1D_2.0_readme.txt

Building dockerfile

docker pull ubuntu:latest

# boot into container
docker run -it ubuntu:latest bash

# inside container
apt update && apt -y install \
   build-essential \
   wget  
   
  