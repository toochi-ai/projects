import random
import time


def decorator(func):
    def wrapper(*args, **kwargs):
        print('Делаем что-то перед вызовом функции - изменяем ее поведение')
        res = func(*args, **kwargs)
        print('Делаем что-то после вызова функции — изменяем ее поведение')
        return res + '+ Изменяем возвращаемое значение в wrapper'

    return wrapper


def demo_func(parameter1, parameter2):
    print('Работает целевая функция')
    print(parameter1)
    print(parameter2)
    return 'Возвращаемое значение оригинальной функции'


changed_function = decorator(demo_func)

result = changed_function('Параметр декорированной функции_1',
                          'Параметр декорированной функции_2')

print(result)
print('---')


def decorator(func):
    def wrapper(*args, **kwargs):
        print('Отработал декоратор')
        res = func(*args, **kwargs)
        return res

    return wrapper


@decorator
def demo_func():
    print('Отработала оригинальная функция')


demo_func()
print('---')


#  Оценка времени работы функции

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        work_time = time.time() - start_time
        print(f'Функция {func.__name__} отработала за {work_time} секунд')
        return res

    return wrapper


@timeit
def large_sum(n):
    return sum(range(n))


@timeit
def prime_numbers(n):
    primes = []
    for possiblePrime in range(2, n):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
        if isPrime:
            primes.append(possiblePrime)
    return primes


prime_numbers(193700)
large_sum(193700)
print('---')


# Генерация пароля

def create_password_generator(length, symbols):
    used_passwords = set()

    def generator():
        nonlocal used_passwords
        while True:
            password = ''.join(random.choice(symbols) for _ in range(length))
            if password not in used_passwords:
                used_passwords.add(password)
                return password

    return generator


symbols_for_password = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
password_generator = create_password_generator(10, symbols_for_password)
print(password_generator())
print(password_generator())
