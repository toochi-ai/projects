import http.client
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

