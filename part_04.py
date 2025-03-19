import pandas as pd  #редактирование и удаление данных
df = pd.read_csv('animal.csv')
print(df)
# df.fillna(0, inplace=True)
# df.dropna(inplace=True)  #удаляется вся сторка
# print(df)
group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)
