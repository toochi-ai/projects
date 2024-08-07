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
    call_stack = []

    def wrapper(*args, **kwargs):
        call_stack.append(None)
        if len(call_stack) == 1:
            start_time = time.time()
            res = func(*args, **kwargs)
            work_time = time.time() - start_time
            print(f'Функция {func.__name__} отработала за {work_time} секунд')
            print(f'args: {args}')
            print(f'kwargs: {kwargs}')
        else:
            res = func(*args, **kwargs)
        call_stack.pop()
        return res

    return wrapper


@timeit
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


factorial(155)


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
@timeit
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
print('---')


@timeit
def power_sum(n, p):
    return sum(i ** p for i in range(n))


result = power_sum(10000, 2)

print(result)
print('---')

#  универсальный декоратор


def retry_on_failure(func):
    max_retries = 3

    def wrapper(*args, **kwargs):
        for _ in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Function {func.__name__} failed with error: {e}. Retrying...")
                time.sleep(1)  # В реальном кейсе нам чаще всего надо будет подождать нек-ое кол-во времени
        print(f"Function {func.__name__} failed after {max_retries} retries.")

    return wrapper


@retry_on_failure
def fragile_function(*args, **kwargs):
    if random.random() < 0.5:  # В 50% случаев функция будет "Ломаться"
        raise Exception("An error occurred")
    else:
        return "Success"


print(fragile_function())
