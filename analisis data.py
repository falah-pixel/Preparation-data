import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

df_can = pd.read_excel('Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print ('Data read into a pandas dataframe!')

df_can.head()
df_can.columns.values
df_can.index.values
print(type(df_can.columns))
print(type(df_can.index))

df_can.columns.tolist()
df_can.index.tolist()

print (type(df_can.columns.tolist()))
print (type(df_can.index.tolist()))

df_can.shape
df_can.drop(['AREA','REG','DEV','Type','Coverage'], 
            axis=1, inplace=True)
df_can.head(2)

df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, 
              inplace=True)
df_can.columns

df_can['Total'] = df_can.sum()
df_can.isnull().sum()
df_can.describe()

df_can.Country
df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]]
df_can.set_index('Country', inplace=True)
df_can.head(3)

df_can.index.name = None

print(df_can.loc['Japan'])

# alternate methods
print(df_can.iloc[87])
print(df_can[df_can.index == 'Japan'].T.squeeze())

print(df_can.loc['Japan', 2013])

# alternate method
print(df_can.iloc[87, 36])
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])
print(df_can.iloc[87, [3, 4, 5, 6, 7, 8]])

df_can.columns = list(map(str, df_can.columns))

years = list(map(str, range(1980, 2014)))
years
condition = df_can['Continent'] == 'Asia'
print(condition)
df_can[condition]

df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]
print('data dimensions:', df_can.shape)
print(df_can.columns)
df_can.head(2)

import matplotlib as mpl
import matplotlib.pyplot as plt

print ('Matplotlib version: ', mpl.__version__)
print(plt.style.available)
mpl.style.use(['ggplot'])

haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
haiti.head()

haiti.plot()

haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show()

haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.text(2000, 6000, '2010 Earthquake') # see note below

plt.show()