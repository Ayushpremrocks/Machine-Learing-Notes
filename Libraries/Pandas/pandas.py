# -*- coding: utf-8 -*-
"""Pandas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hOkCGjKwQYoAGP7YxelXbcJHDNPP7MFX

# Pandas
- Flexible with Python
- Working with big data

YT link: https://youtu.be/vmEHCJofslg?si=gPrFy3C4tejIk57O

# Installing Pandas
"""

pip install pandas

"""# Loading data into Pandas"""

import pandas as pd

"""# Printing Data

Printing Data
"""

x = pd.read_csv('pokemon_data.csv')
print(x)

"""Printing first 5 rows"""

print(x.head(5))

"""Printing last 5 rows"""

print(x.tail(5))

"""Getting the columns"""

#read headers
x.columns

"""Getting Data by Columns"""

#read each colums
print(x[['Name', 'HP']])

"""Read each row"""

#read each row
print(x.iloc[1:5])

"""Reading a specific location [R,C]"""

#read specific location (R,C)
print(x.iloc[4,1])

"""Iterating through each row"""

#iterate through each row
for index, row in x.iterrows():
    print(index, row['Name'])

"""Finding rows based on a specific condtion"""

#getting rows based on a specific condtion
x.loc[x['Type 1'] == 'Grass']

x.loc[(x['Type 2'] == 'Ghost')]

"""# Sorting/describing data

Getting count, mean, standard deviation, min and max values
"""

x.describe()

"""Sort values (ascending)"""

x.sort_values('Name')

"""Sort values (decending)"""

x.sort_values('Name', ascending=False)

x.sort_values(['Type 1', 'HP'], ascending=False)

x.sort_values(['Type 1', 'HP'], ascending=[1,0])

"""# Making changes to the data"""

x.head(10)

x['Total'] = x['HP'] + x['Attack'] + x['Defense'] + x['Sp. Atk'] + x['Sp. Def'] + x['Speed']
x

"""Removing a column"""

#remove a column
x.drop(columns=['Total'])

x['Total'] = x.iloc[:, 4:10].sum(axis=1)
x

"""Rearranging column"""

#rearranging columns
cols = list(x.columns)
x = x[cols[0:4] + [cols[-1]]+cols[4:12]]
x

"""# Saving our Data (Exporting into a desired format)"""

x.to_csv('modified.csv')
x.to_excel('modified.xlsx', index=False)
x.to_csv('modified.txt', index=False, sep='\t')

"""#Filtering data"""

new_x = x.loc[(x['Type 1'] == 'Grass') & (x['Type 2'] == 'Poison')]
new_x

new_x.reset_index(drop=True, inplace=True) # to reset indexing
new_x.to_csv('filtered.csv')
new_x

"""#Conditional changes"""

x.loc[x['Total'] > 500, ['Generation','Legendary']] = ['Test 1', 'Test 2']
x

"""#Aggregate statistics(groupby)"""

x= pd.read_csv('modified.csv')
x['count'] = 1
x.groupby(['Type 1', 'Type 2']).count()['count']

"""# Working with large amounts of data"""

new_x = pd.DataFrame(columns=x.columns)
for x in pd.read_csv('modified.csv', chunksize=5):
    results = x.groupby(['Type 1']).count()
    new_x = pd.concat([new_x, results])
    print(new_x)