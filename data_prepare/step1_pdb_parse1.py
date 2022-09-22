import pandas as pd
import numpy as np

# Step 0: parse the fasta file downloaded from the RCSB PDB
# INPUT : pdb_seqres.txt
# OUTPUT: pdb_pep_chain, pdbid_all_fasta
raw_str=''
with open('pdb_seqres_small.txt','r') as f:
    for line in f.readlines():
        raw_str = raw_str+line.replace('\n','###')
raw_list = raw_str.split('>')
del raw_list[0]

PDB_id_lst = [x.split('_')[0] for x in raw_list]
PDB_chain_lst = [x.split('_')[1].split(' ')[0].lower() for x in raw_list]
PDB_type_lst = [x.split('mol:')[1].split(' ')[0] for x in raw_list]
PDB_seq_lst = [x.split('###')[1] for x in raw_list]
PDB_seq_len_lst = [len(x) for x in PDB_seq_lst]
df_fasta_raw =pd.DataFrame(list(zip(PDB_type_lst, PDB_seq_len_lst,PDB_seq_lst,PDB_id_lst,PDB_chain_lst)),\
                       columns=['PDB_type','PDB_seq_len','PDB_seq','PDB_id','chain'])
df_fasta = df_fasta_raw[(df_fasta_raw.PDB_seq_len<=50)&(df_fasta_raw.PDB_type=='protein')]
df_fasta_raw.to_csv('pdbid_all_fasta', encoding='utf-8', index=False, sep = '\t')
df_fasta.to_csv('pdb_pep_chain', encoding='utf-8', index=False, sep = '\t')

print('Step 0 is finished by generating two files : pdb_pep_chain & pdbid_all_fasta!')
