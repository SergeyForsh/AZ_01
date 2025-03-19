import pandas as pd
df = pd.read_csv('hh.csv')
df['Test'] = [new for new in range(50)]
print(df)
df.drop('Test', axis=1, inplace=True)   #axis=1 колонка, а axis=0 строка
print(df)