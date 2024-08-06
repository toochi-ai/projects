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
