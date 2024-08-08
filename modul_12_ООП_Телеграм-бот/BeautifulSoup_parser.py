import requests
from bs4 import BeautifulSoup

base = 'https://ru.stackoverflow.com'  # выносим базовую ссылку
# в отдельную переменную, она нам потом
html = requests.get(base).content  # с помощью библиотеки requests
# получаем html код странички целиком
soup = BeautifulSoup(html, 'lxml')  # создаём объект супа.
# Первый аргумент в конструкторе - это весь html код.
# Второй аргумент - сама библиотека для парсинга. В нашем случае lxml
div = soup.find('div', id='question-mini-list')  # находим с помощью метода find() нужный нам див уточняя id

a = div.find_all('a', class_='s-link')
for _ in a:
    print((_.getText(), base + _.get('href')))

# a = div.find('a', class_='s-link')  # попробуем найти первый тег а
# parent = a.find_parent()  # находим первого родителя тега а
# print(parent) # Печатаем тег родитель. В данном случае это должен быть тег <h3>
