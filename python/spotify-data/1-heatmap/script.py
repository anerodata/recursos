# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Import df and create pivot table
df = pd.read_json('../data/my_spotify_data/MyData/StreamingHistory0.json')

df['month'] = pd.DatetimeIndex(df['endTime']).month
df['year'] = pd.DatetimeIndex(df['endTime']).year
df['time'] = 1
df_pivot = pd.pivot_table(df, values='time', index=['trackName', 'month'], columns='year', aggfunc=np.sum)	
flattened = pd.DataFrame(df_pivot.to_records())
flattened.loc[flattened['trackName'] != 'Guaguancó', '2019'] = 0
flattened.loc[flattened['trackName'] != 'Guaguancó', '2020'] = 0
filtered = flattened.loc[flattened['trackName'] == 'Guaguancó']
print(flattened)
filtered =filtered.drop(columns='trackName')
filtered = filtered.set_index('month')
print(filtered)

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(filtered, annot=True, linewidths=.5, ax=ax)
plt.show()
