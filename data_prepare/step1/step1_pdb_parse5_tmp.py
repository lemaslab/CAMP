import pandas as pd
import numpy as np

def lower_chain(input_str):
    chain_list = list(input_str)
    output_list = []
    for item in chain_list:
        if item.isalpha() :
            a=item.lower()
        else :
            a=item
        output_list.append(a)
    output_str = ''.join(output_list)
    return output_str

# Step 3: Map Uniprot ID for PDB complex by protein-chain & PDB id
# INPUT: data from Step 2 & pdb_chain_uniprot.tsv from SIFT
# OUTPUT: UniProt_ID_list ( all IDs are the searching query on https://www.uniprot.org/uploadlists/ for unified sequence)
def map_uniprot_chain(df_predict_det1, pdb_chain_uniprot): #df_predict_det1 #pdb_chain_uniprot.tsv
    input_dataset = pd.read_csv('df_predict_det1', sep = '\t', header = 0)
    df_sifts = pd.read_csv('pdb_chain_uniprot.tsv', sep = '\t', header = 1)
    df_sifts = df_sifts[['PDB','CHAIN','SP_PRIMARY']]
    df_sifts_keep = df_sifts[df_sifts['CHAIN'] !=  df_sifts['CHAIN']]
    df_sifts = df_sifts[df_sifts['CHAIN'] == df_sifts['CHAIN']]
    df_sifts['CHAIN'] = df_sifts.CHAIN.apply(lambda x: lower_chain(x))

    df_predict_det2 = pd.merge(input_dataset,df_sifts, how = 'left', \
                              left_on = ['pdb_id','predicted_chain'],right_on = ['PDB','CHAIN'])
    df_predict_det2 = df_predict_det2.drop(['PDB','CHAIN'],axis = 1)


    # subset records that don't have a matched protein chain Uniprot
    df_predict_det2_no_uni = df_predict_det2[df_predict_det2.SP_PRIMARY != df_predict_det2.SP_PRIMARY]
    df_predict_det2_no_uni = df_predict_det2_no_uni.reset_index(drop = True)
    
    df_predict_det2_no_uni = df_predict_det2_no_uni.drop(['prot_seq_len','peptide_seq_score'],axis = 1)
    df_predict_det2_no_uni = df_predict_det2_no_uni[['pdb_id','pep_chain','predicted_chain','pep_seq',\
                                     'pep_seq_len','SP_PRIMARY','prot_seq']]
    df_predict_det2_no_uni.rename(columns = {'prot_seq': 'Sequence'}, inplace=True)

    # focus on records with Uniprot Ids
    df_predict_det3 = df_predict_det2[df_predict_det2.SP_PRIMARY == df_predict_det2.SP_PRIMARY]

    # save matched uniport ID for retrieving information from Uniprot Website
    df_uni_id = df_predict_det3[['SP_PRIMARY']]
    #df_uni_id.drop_duplicates(inplace = True)
    file_name = 'df_predict_det3'
    df_uni_id.to_csv(file_name, encoding = 'utf-8', index = False, sep = '\t')

    return df_predict_det2_no_uni,df_predict_det3

df_predict_det2_no_uni,df_predict_det3 = map_uniprot_chain('df_predict_det1','pdb_chain_uniprot.tsv')
