def recursive_func(n=0):
    print('Вывод до запуска рекурсии:', n)
    if n < 3:
        recursive_func(n + 1)
    print('Вывод после запуска рекурсии:', n)


recursive_func()
print('---')


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
