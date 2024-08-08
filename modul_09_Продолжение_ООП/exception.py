# try:
#     *код, который может вызвать ту или иную ошибку*
# except *ошибка*:
#     *код, который выполнится в случае возникновения ошибки*
# else:
#     *код, который выполнится только в случае, если в try ничего не сломалось*
# finally:
#     *код, который выполнится по-любому*

try:
    print("Before exception")
    a = int(input("a: "))
    b = int(input("b: "))
    print(a / b)
except ZeroDivisionError as e:
    print(e)
    print("After exception")
else:
    print("Very well")
finally:
    print("Finally here")

print("After after exception")

print('---')

try:
    age = int(input("how are you old? - "))
    if age > 100 or age <= 0:
        raise ValueError("Тебе не может быть столько лет")

    print(f"Тебе {age} лет!")

except ValueError:
    print("Неправильный возраст")

print('---')


try:
    number = int(input("Введите число: "))
except ValueError as e:
    print("Вы ввели неправильное число")
else:
    print(f"Вы ввели {number}")
finally:
    print("Выход из программы")
