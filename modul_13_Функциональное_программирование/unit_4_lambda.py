people = [
    {'name': 'Anna', 'age': 20},
    {'name': 'Boris', 'age': 25},
    {'name': 'Victor', 'age': 19}
]

print(*people)
print('---')

# def get_age(person):
#     return person['age']
#
#
# def get_name(person):
#     return person['name']
#
#
# sorted_people = sorted(people, key=get_age)
# print(*sorted_people)
# print('---')


sorted_people = sorted(people, key=lambda person: person['age'])
print(*sorted_people)
print('---')

squared = map(lambda x: x ** 2, [1, 2, 3, 4])

print(list(squared))
print('---')

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))
print('---')

test_cases = [
    {"id": 1, "category": "UI", "description": "Тестирование интерфейса"},
    {"id": 2, "category": "Backend", "description": "Тестирование API"},
    {"id": 3, "category": "UI", "description": "Проверка элементов управления"},
]

ui_tests = filter(lambda x: x['category'] == 'UI', test_cases)
print(list(ui_tests))
print('---')

tests = [
    {'name': 'test_login', 'executed': True},
    {'name': 'test_registration', 'executed': False},
    {'name': 'test_profile_update', 'executed': False}
]

pending_tests = filter(lambda x: not x['executed'], tests)

for test in pending_tests:
    print(f'Running test: {test['name']}')
print('---')

# -----------------------------------------------------------------------------------------
#                   lambda-функции для быстрой обработки данных
# -----------------------------------------------------------------------------------------
# Задача — обработать список и изменить строковое значение ключа status на булевое:
# True, если pass, и False, если fail

test_results = [
    {'name': 'test1', 'status': 'fail', 'time': 2.5},
    {'name': 'test2', 'status': 'pass', 'time': 1.1},
    {'name': 'test3', 'status': 'fail', 'time': 3.1},
    {'name': 'test4', 'status': 'pass', 'time': 0.9}
]

for result in test_results:
    result['status'] = (lambda x: x == 'pass')(result['status'])

for test in test_results:
    print(test)

print('---')

test_reports = [
    {'name': 'test1', 'status': 'fail', 'time': 2.5, 'details': {'error': 'NullPointerException', 'attempt': 1}},
    {'name': 'test2', 'status': 'pass', 'time': 1.1, 'details': {'attempt': 1}},
    {'name': 'test3', 'status': 'fail', 'time': 3.1, 'details': {'error': 'AssertionError', 'attempt': 2}},
    {'name': 'test4', 'status': 'pass', 'time': 0.9, 'details': {'attempt': 1}}
]


#  Задача — создать функцию, которая принимает список отчётов и функцию извлечения,
#  а затем возвращает список нужных значений

def extract_data(reports, extraction_func):
    # Применяем переданную функцию к каждому словарю и генерируем новый список
    return [extraction_func(report) for report in reports]


execution_times = extract_data(test_reports, lambda x: x['time'])
print(execution_times)

attempt_counts = extract_data(test_reports, lambda x: x['details']['attempt'])
print(attempt_counts)

numbers = [1, 2, 3, 4, 5]
apply_function = map(lambda x: x ** 2, numbers)
print(list(apply_function))

print('---')

people = [("Anna", 23), ("John", 21), ("Alice", 25)]
sort_by_age = sorted(people, key=lambda x: x[-1])
print(sort_by_age)

print('---')

prices_in_usd = [10, 20, 30, 40, 50]
exchange_rate = 0.85

prices_in_euro = map(lambda x: x * exchange_rate, prices_in_usd)

print(tuple(prices_in_euro))
