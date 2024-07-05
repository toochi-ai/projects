from modul1 import *


def main():
    r = int(input("Введите радиус круга: "))
    a = int(input("Введите сторону квадрата: "))
    print('-----')

    if square_rectangle(a) > square_circle(r):
        print("Площадь квадрата =", square_rectangle(a))
    else:
        print("Площадь круга =", square_circle(r))


if __name__ == '__main__':
    main()
