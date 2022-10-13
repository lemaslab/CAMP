import pandas as pd
import numpy as np


# Step 4: Load Uniport sequences and family information & filter out MHC families
# INPUT: the data from Step 3 & uniprot2seq from UniProt Website (a tab separated file with fields including Uniprot_id,Uniprot Sequence,Protein_name,Protein_families)
# OUTPUT: interacted peptide-protein pairs from PDB (a '#' separated file with fields including pdb_id,pep_chain,prot_chain,pep_seq,Uniprot_id,prot_seq,protein_families)

#def load_uni_seq(input_dataset,uniprot2seq_file):

# I am running code, line-by-line. I think we might need more data. 

	# import data
	input_dataset = pd.read_csv('df_predict_det3',sep = '\t',header = 0)
	df_uni2seq = pd.read_csv('uniprot2seq.txt',sep = '\t',header = 0)
	
	# format data
	#df_uni2seq = df_uni2seq.drop('uniprot',axis = 1)  # might not be necessary given data
	df_uni2seq = df_uni2seq.drop_duplicates(['Uniprot_id','Sequence'],keep = 'first')
	df_uni2seq = df_uni2seq.fillna('Unknown_from_uniprot')

	# join by uniprot id (stopped here)
	df_predict_det4 = pd.merge(input_dataset,df_uni2seq,how = 'left',left_on = ['SP_PRIMARY'],right_on = ['Uniprot_id'])
	#df_predict_det4 = df_predict_det4.drop(['Uniprot_id','Protein_name','prot_seq','prot_seq_len','peptide_seq_score'],axis = 1) # might not be necessary given data
	#df_predict_det4 = df_predict_det4.drop_duplicates(['pdb_id','pep_seq','SP_PRIMARY','Sequence'],keep = 'first') # might not be necessary given data

	# filter out MHC
	df_predict_det4["MHC_flag"] = df_predict_det4.Protein_families.apply(lambda x: x.lower().find('mhc'))
	df_mhc = df_predict_det4.loc[df_predict_det4.MHC_flag!=-1][["pdb_id","Protein_families"]]
	df_mhc.columns = ['pdb_id_mhc','prot_family_mhc']

	# join by  PDB id only(if a pdb contains mhc proteins,remove all records of the PDB id)
	df_predict_det5 = pd.merge(df_predict_det4, df_mhc,left_on = ['pdb_id'], right_on = ['pdb_id_mhc'], how='left')
	df_predict_det5 = df_predict_det5.loc[df_predict_det5.pdb_id_mhc!=df_predict_det5.pdb_id_mhc]
	df_predict_det5 = df_predict_det5.drop(['pdb_id_mhc','prot_family_mhc','MHC_flag'],axis =1)
	df_predict_det5.drop_duplicates(inplace=True)

	df_predict_det2_no_uni = df_predict_det2_no_uni.drop(['prot_seq_len','peptide_seq_score'],axis = 1)
	df_predict_det2_no_uni = df_predict_det2_no_uni[['pdb_id','pep_chain','predicted_chain','pep_seq','pep_seq_len','SP_PRIMARY','prot_seq']]
	df_predict_det2_no_uni.rename(columns={'prot_seq': 'Sequence'}, inplace=True)
	df_predict_det2_no_uni['Protein_families'] = pd.Series(['Unknown Uniprot_ids' for x in range(df_predict_det2_no_uni.shape[0])])
	df_predict_det6 = pd.concat([df_predict_det2_no_uni,df_predict_det5],ignore_index=True)
	df_predict_det6['plip_prot_chain'] = df_predict_det6.predicted_chain.apply(lambda x: x.upper())
	df_predict_det6 = df_predict_det6.drop_duplicates(['pep_seq','Sequence'],keep='first')
	df_predict_det6 = df_predict_det6.reset_index(drop=True) #8184
	df_predict_det6['prot_seq_len'] = df_predict_det6.Sequence.apply(lambda x: len(str(x)))
	df_predict_det6 = df_predict_det6[df_predict_det6.prot_seq_len<=5000]

	df_pdb_pairs = df_predict_det6[['pdb_id','pep_chain','plip_prot_chain','pep_seq','SP_PRIMARY','Sequence','Protein_families']]
	df_pdb_pairs.columns = ['pdb_id','pep_chain','prot_chain','pep_seq','Uniprot_id','prot_seq','protein_families']
	file_name = 'train_pairs_pdb'
	df_pdb_pairs.to_csv(file_name, encoding = 'utf-8', index = False, sep = '#')


	return df_pdb_pairs

#df_pdb_pairs = load_uni_seq('df_predict_det3','uniprot2seq')
