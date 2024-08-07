import re

text = 'По реке плывет лодка, в ней сидит рыбак'
match = re.match(r'рыб', text)
print(match)
print('---')

text = 'В темном лесу щебечут птицы'
search_result = re.search(r'лес', text)
print(search_result, search_result.span(), search_result.string, search_result.group(), sep='\n')
print('---')

text = 'Бегемот плавает, не слыша шума.'
matches = re.findall(r'бег', text, re.IGNORECASE)
print(matches)
print('---')

text = "Солнце светит ярко и согревает."
result = re.split(r' ', text, 1)
print(result)
print('---')

text = "Лиса ловко лазает по деревьям."
res = re.sub(r'лиса', 'кошка', text, flags=re.IGNORECASE)
print(res)
print('---')

pattern = re.compile('лет')
matches1 = pattern.findall("Летом в лесу летают бабочки.")
matches2 = pattern.findall("Летний вечер освещает летящих жуков.")
matches3 = re.findall(r'[вл]', "Летний вечер освещает летящих жуков.")
print(matches1, matches2, matches3, sep='\n')
print('---')

test_text = ("Контактный email: contact@example.com. Неверный адрес: test@test. "
             "Проверка: admin@mailserver1.org, another.email@test.co.uk")
result_step1 = re.findall(r'\S+@\S+\.\S+', test_text)
print(result_step1)
print('---')

test_text1 = ("Контактный email: contact@example.com. "
              "Неверный адрес: test@test. Проверка: admin@mailserver1.org, "
              "another.email@test.co.uk. Тестовый email: !!alex!!@mail.org")
result_step2 = re.findall(r'[a-zA-Z0-9]+@[a-zA-Z0-9.]+\.[a-zA-Z]{2,}', test_text1)
print(result_step2)
print('---')


log_data = """
2023-03-15 Error: Failed to load resource
2023-03-16 Info: Resource loaded successfully
2023-03-17 Warning: Resource load time is high
"""

pattern = r'\d{4}-\d{2}-\d{2}'
dates = re.findall(pattern, log_data)


print(dates)
