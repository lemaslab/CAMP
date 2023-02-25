# CAMP: a Convolutional Attention-based Neural Network for Multi-level Peptide-protein Interaction Prediction

CAMP is a sequence-based deep learning framework for multifaceted prediction of peptide-protein interactions, including not only binary peptide-protein interactions, but also corresponding peptide binding residues.

https://download.igb.uci.edu/

# note: We need to install dependencies. https://download.igb.uci.edu/SCRATCH-1D_2.0_readme.txt

Building dockerfile

docker pull ubuntu:latest

docker build -t scratch1d_1.2 . 

docker tag 9e46ada61a14 dominicklemas/scratch1d:02_2023
docker push dominicklemas/scratch1d:02_2023   
  