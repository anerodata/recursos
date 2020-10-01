import pandas as pd
from matplotlib import pyplot as plt

# Simple chart 
"""
x = [1900, 1910, 1930]
y = [1, 6, 9]
z = [10, 5, 0] 
plt.plot(x, y)
plt.plot(x, z)
plt.title('gráfico de prueba')
plt.xlabel('x')
plt.ylabel('y - z')
plt.legend(['y', 'z'])
plt.show()
"""
"""
sample_data = pd.read_csv('data/sample_data.csv')
plt.plot(sample_data.column_a, sample_data.column_b, 'o')
plt.plot(sample_data.column_a, sample_data.column_c)
plt.show()
"""


countries = pd.read_csv('data/countries.csv')
us = countries[countries.country == 'United States']
china = countries[countries.country == 'China']
plt.plot(us.year, us.population / us.population.iloc[0] * 100)
plt.plot(china.year, china.population / china.population.iloc[0] * 100)
plt.legend(['US', 'China'])
plt.xlabel('Years')
plt.ylabel('Population growth (Base 100)') 
plt.show()