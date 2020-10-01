import pandas as pd
# 1 - open file
#df = pd.read_csv('data/pokemon_data.csv')
#df = pd.read_csv('data/pokemon_data.txt', sep='\t')
df = pd.read_excel('data/pokemon_data.xlsx')

# 2 - tail and head
df.tail(3)
df.head(3)

# 3 - value selection
df.columns
df['Name'][0:5]
df[['Name', 'Type 1', 'HP']][0:5]
df.head(4)
df.iloc[5:9]
print df.iloc[2, 1]

#4 - iterating in dataframe
for i, row in df.iterrows():
	(row['Name'])

#5 - filering
df.loc[df['Type 1'] == 'Water']

#6 - metainfo
df.describe()

#7 - sorting
df.sort_values(['Type 1', 'HP'], ascending = [True, False])

#8 - new column sum
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df ['Sp. Atk'] + df ['Sp. Def'] + df ['Speed'] 
df['Total'] = df.iloc[:,4:10].sum(axis=1)

#9 - delete column
df.drop(columns=['Total'])

#10 - change order of columns
cols = list(df.columns.values)
df = df [cols[0:4] + [cols[-1]] + cols[4:12]]

#11 - delete duplicates
"""df.sort_values('Name', inplace = True)
df.drop_duplicates(subset = 'Name', keep = 'first', inplace = True)"""

#12 - save data
"""df.to_csv('modified.csv', encoding='utf-8', index = False)
df.to_excel('modified.xlsx', encoding='utf-8', index=False)
df.to_csv('modified.txt', encoding='utf-8', index=False, sep='\t')"""

#13 - filtering
#newDf = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison' ) & (df['HP'] > 50) ]

#14 - reset index, con inplace el cambio se aplica en el mismo dataframe, ahorra memoria
#newDf.reset_index(drop = True, inplace=True)

#15 - los que contienen mega y los que no
df.loc[df['Name'].str.contains('Mega')]
df.loc[~df['Name'].str.contains('Mega')]

#16 - guego o hierba por regex obviando capitalizacion gracias al flag
import re
df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]

#17 - todos los que empizan por pi
df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]

#18 - cambiar un valor en una columna
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Fuegote'

#19 - Todos los de fuego, legendarios (en otra columna)

#df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True

#20 - Si la columna total es mayor que 500, las columnas generation y legendary valen test value
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'TEST VALUE'

#21 - Lo mismo pero con un nombre para cada columna
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['TEST VALUE 1', 'TEST VALUE 2']

#22 - groupby por Tipo de pokemon con la media de cada valor numerico ordenado por defensa
df.groupby(['Type 1']).mean().sort_values('HP', ascending=False)

#23 - groupby con tipo con la suma de cada valor                
df.groupby(['Type 1']).sum()

#23 - groupbycon la cuenta de cada tipo
df.groupby(['Type 1']).count()

#24 - Contar a traves de una columna igualada a 1 

df['count'] = 1

df.groupby(['Type 1', 'Type 2']).count()['count']

#25 - trabajar con grandes datasets (carga el fichero de 5 en 5 lineas). Ahorra memoria
newDf = pd.DataFrame(columns = df.columns)

for df in pd.read_csv('modified.csv', chunksize=5):
	res = df.groupby(['Type 1']).count()
	newDf = pd.concat([newDf, res], sort=False)
#print newDf