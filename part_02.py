import pandas as pd     #(датафрейм)
df = pd.read_csv('global_energy_consumption.csv')  #df=pd.read_excel df = pd.read_csv
#print(df.describe())   #по умолчанию 5 или прописать пример - 3
#или последние (df.head())  (df.tail())  (df.info()) (df.describe()) - среднее
#print(df['Country'])
#print(df[['Country', 'Year']])
#print(df.loc[56])  #индекс
#print(df.loc[56, 'Renewable Energy Share (%)'])  #показатель на строке 56
print(df[df['Renewable Energy Share (%)'] > 0.4])
