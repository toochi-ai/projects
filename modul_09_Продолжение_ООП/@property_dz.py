class Dog:
    _happiness = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def human_age(self):
        return self.age * 7

    @property
    def happiness(self):
        return self._happiness

    @happiness.setter
    def happiness(self, value):
        if value <= 100 and value >= 0:
            self._happiness = value
        else:
            raise ValueError("Happiness must be between 0 ... 100")


ressi = Dog("Ressi", 2)
ressi.happiness = 100
print(ressi.human_age)
print(ressi.happiness)

print('---')


class ParentClass:
    @classmethod
    def method(cls, arg):
        print("%s classmethod. %d" % (cls.__name__, arg))

    @classmethod
    def call_original_method(cls):
        cls.method(5)

    def call_class_method(self):
        self.method(10)


class ChildClass(ParentClass):

    @classmethod
    def call_original_method(cls):
        cls.method(6)


ParentClass.method(0)
ParentClass.call_original_method()

ChildClass.method(1)
ChildClass.call_original_method()

my_obj = ParentClass()
my_obj.method(1)
my_obj.call_class_method()

print('---')


class Square:
    _a = None

    def __init__(self, a):
        self.a = a

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value

    @property
    def area(self):
        return self.a ** 2


m = Square(35)
print(m.area)

print('---')

try:
    print("перед исключением")
    a = int(input("a: "))
    b = int(input("b: "))
    c = a / b
    print(c)
except ZeroDivisionError as e:
    print("на ноль делить нельзя")
    a = int(input("a: "))
    b = int(input("b: "))
    c = a / b
    print(c)
else:
    print("все ништяк")
finally:
    print("Всегда все ништяк!!! finally на месте! ")
print("после после исключения")

try:
    age = int(input("Сколько тебе лет? "))
    if age > 100 or age < 0:
        raise ValueError("Брехня! ахах")
    print(f"Тебе {age} )))")
except ValueError:
    print("Не бибикай!!!)")

print('---')

try:
    a = int(input("жду: \t"))
    print("Bravo")
except ValueError:
    print("нужно число))")
else:
    print(f'вы ввели {a}')
finally:
    print("выйти из программы")
