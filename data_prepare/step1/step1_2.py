import pandas as pd
import numpy as np

def check_abnormal_aa(peptide_seq):
	len_seq = len(peptide_seq)
	cnt = 0
	standard_aa = ['G','A','P','V','L','I','M','F','Y','W','S','T','C','N','Q','K','H','R','D','E']
	for i in peptide_seq:
		if i in standard_aa :
			cnt = cnt+1
	score = float(cnt)/len_seq
	return score

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


# Step 2: Get fasta sequence of the predicted interacting chains
# INPUT:  pdbid_all_fasta from Step 0
# OUTPUT: -
def load_all_fasta(all_fasta_file,plip_predict_result): # pdbid_all_fasta_demo # df_predict (plip_predict_result)
	# import data
	input_dataset = pd.read_csv('plip_predict_result',sep = '\t', header = 0)
	
	df_fasta = pd.read_csv(all_fasta_file,sep = '\t', header = 0)
	
	df_fasta_protein = df_fasta.loc[df_fasta.PDB_type=='protein']
	
	df_fasta_vocabulary = df_fasta_protein[['PDB_id','chain','PDB_seq']]

	df_predict_det = pd.merge(input_dataset,df_fasta_vocabulary,	how='left', left_on = ['pdb_id','pep_chain'],right_on = ['PDB_id','chain'])

	df_predict_det1 = pd.merge(df_predict_det,df_fasta_vocabulary,how='left',\
							 left_on = ['pdb_id','predicted_chain'],right_on = ['PDB_id','chain'])
	df_predict_det1 =df_predict_det1.drop(['PDB_id_x','chain_x','PDB_id_y','chain_y'],axis =1)
	df_predict_det1.columns = ['pdb_id','pep_chain','predicted_chain','pep_seq','prot_seq']
	df_predict_det1['pep_seq_len'] = df_predict_det1.pep_seq.apply(lambda x: len(x))
	df_predict_det1['prot_seq_len'] = df_predict_det1.prot_seq.apply(lambda x: len(x))


	# check sequence length(peptide<=50 & protein >50)
	df_predict_det1 = df_predict_det1.loc[(df_predict_det1.pep_seq_len <= 50) & (df_predict_det1.prot_seq_len > 50)]


	# remove records with more than 20% AA is abnormal
	df_predict_det1['peptide_seq_score'] = df_predict_det1.pep_seq.apply(lambda x: check_abnormal_aa(x))
	df_predict_det1 = df_predict_det1[df_predict_det1.peptide_seq_score >= 0.8]

	print('finish removing sequences without too many non-standard residues')
	print('-----------------------------------------------------')

	# save organized data formatted 
	file_name = "df_predict_det1"
	df_predict_det1.to_csv(file_name, encoding='utf-8', index=False, sep='\t')

	return df_predict_det1
	
df_predict_det1 = load_all_fasta('pdbid_all_fasta_demo','plip_predict_result')

