import requests
import pandas as pd
import base64
import re
from time import sleep

df = pd.read_csv('../data/txt/url-sobotka.tsv', sep='\t')
print (df)

def get_as_base64(url, i):
    with open('../data/img/all/'+str(i)+".jpeg", "wb") as fh:
        fh.write(base64.b64decode(url))

def get_as_file(url, i):
    f = open('../data/img/all/'+str(i)+'.jpg','wb')
    f.write(requests.get(url).content)
    f.close()
    
for i, row in df.iterrows():
    if re.search('base64', row['url']):
        #get_as_base64(row['url'], i)
        print('a')
    else:
        print(row['url'])
        get_as_file(row['url'], i)
        sleep(2)
    