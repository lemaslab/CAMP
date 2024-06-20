import requests
import pandas as pd
import time


# goes through ppdbench_metadata.csv and fills in the sequence column
# edge case on line 121(4e34) filled in manually

metadata = pd.read_csv('ppdbench_metadata.csv')
print(metadata)
for index, row in metadata.iterrows():
    id = row['pdb_id']
    data = requests.get(f'https://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/{id}').json()[id.lower()]
    metadata.at[index, 'sequence'] = data[0]['sequence']
    time.sleep(1)
    print(data[0]['sequence'])


metadata.to_csv('ppdbench_metadata.csv', index=False)
