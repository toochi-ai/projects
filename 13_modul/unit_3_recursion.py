def recursive_func(n=0):
    print('Вывод до запуска рекурсии:', n)
    if n < 3:
        recursive_func(n + 1)
    print('Вывод после запуска рекурсии:', n)


recursive_func()
print('---')
