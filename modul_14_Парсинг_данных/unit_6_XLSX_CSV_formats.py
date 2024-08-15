import pandas as pd
from pandas import read_excel
from pandas import read_csv


marks_data = read_excel('marks.xlsx')

print(marks_data.to_dict(orient='records'))

marks_second = [
    {'Год рождения': 1997, 'Имя': 'Сергей', 'Фамилия': 'Васильев', 'Оценка': 5},
    {'Год рождения': 1998, 'Имя': 'Андрей', 'Фамилия': 'Кружков', 'Оценка': 4},
    {'Год рождения': 1997, 'Имя': 'Василий', 'Фамилия': 'Кротов', 'Оценка': 5},
    {'Год рождения': 1997, 'Имя': 'Алексей', 'Фамилия': 'Трушкин', 'Оценка': 5},
    {'Год рождения': 1998, 'Имя': 'Артем', 'Фамилия': 'Матрасов', 'Оценка': 4}
]

marks_second_df = pd.DataFrame(marks_second)
marks_second_df.to_excel('marks_second.xlsx', index=False)
print('---')

goods_data = pd.read_excel('goods.xlsx')
goods_data = goods_data.to_dict()
goods_data.pop('Продавец')
goods_data_df = pd.DataFrame(goods_data)
goods_data_df.to_excel('goods_second.xlsx', index=False)
print('---')

marks_data = read_csv('marcs.csv')

print(marks_data.to_dict(orient='records'))
