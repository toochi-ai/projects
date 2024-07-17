import json

import requests

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # попробуем поймать json-ответ
texts = json.loads(r.content)  # делаем из полученных байтов Python-объект для удобной работы

print(type(texts))  # проверяем тип сконвертированных данных

for text in texts:  # Выводим полученный текст. Но для того чтобы он влез в консоль,
    # оставим только первые 50 символов.
    print(text[:50], '\n')

print('---')

r = requests.get('https://api.github.com')
d = json.loads(r.content)  # делаем из полученных байтов Python-объект для удобной работы
print(d['following_url'])  # обращаемся к полученному объекту как к словарю и
# попробуем напечатать одно из его значений

print('---')
# POST-запрос
# --------------

r = requests.post('https://httpbin.org/post', data={'key': 'value'})  # отправляем POST-запрос

print(r.content)  # содержимое ответа и его обработка происходит так же,
# как и с GET-запросами, разницы никакой нет
