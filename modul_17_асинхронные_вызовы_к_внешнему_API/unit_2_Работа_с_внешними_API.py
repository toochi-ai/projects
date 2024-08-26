import base64
import http.client
from requests.auth import HTTPDigestAuth
import requests

connection = http.client.HTTPSConnection("www.google.com")
# открываем соединение по протоколу HTTPS на сайт google.com
connection.request("GET", "/")  # указываем тип запроса,
# в данном случае GET, т.к. нам необходимо просто получить веб-страницу и адрес,
# который указывается после домена, если такой есть, например example.com/about.
# В данном случае www.google.com/

response = connection.getresponse()  # выполняем запрос и получаем ответ от сервера
print(response.status)  # выводим в терминал статус запроса
print(response.read().decode("utf-8"))  # прочитаем данные страницы, необходимо произвести
# декодирование чтобы была поддержка кириллицы

connection.close()  # закрываем соединение
print('---')

response = requests.get("https://www.google.com")  # выполняем GET-запрос
print(response.status_code)  # выводим статус ответа в терминал
print(response.text)  # получаем результат запроса
print('---')

data = {"key": "value"}  # создаем словарь данных, который будем отправлять в запросе
response = requests.post("https://www.example.com/post", data=data)  # при отправке POST запроса,
# помимо адреса необходимо добавить тело запроса, в этом случае словарик data

print(response.status_code)
print(response.text)
print('---')


def base_64_auth(username, password):
    return base64.b64encode(f"{username}:{password}".encode()).decode()


requests.get(
    'https://example.ru',
    headers={
        'Authorization': f"Basic {base_64_auth('login', 'password')}"
    }
)
print('---')

requests.get(
    'https://example.ru',
    auth=HTTPDigestAuth('login', 'password')
)
print('---')

requests.get(
    'https://example.ru',
    headers={
        'PpiKey': "KGJHA42345HHSAEJGN3786r428793yhr2hf"
    }
)
