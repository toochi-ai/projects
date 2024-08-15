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
print('---')

marcs_second = [
   {'год рождения': 1997, 'имя': 'Сергей', 'фамилия': 'Васильев', 'оценка': 5},
   {'год рождения': 1998, 'имя': 'Андрей', 'фамилия': 'Кружков', 'оценка': 4},
   {'год рождения': 1997, 'имя': 'Василий', 'фамилия': 'Кротов', 'оценка': 5},
   {'год рождения': 1997, 'имя': 'Алексей', 'фамилия': 'Трушкин', 'оценка': 5},
   {'год рождения': 1998, 'имя': 'Артем', 'фамилия': 'Матрасов', 'оценка': 4}
]

marcs_second_df = pd.DataFrame(marcs_second)
marcs_second_df.to_csv('marcs_second.csv', index=False)
