class Dog:
    _happiness = 10
    _cry = -1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def human_age(self):
        return self.age * 2.5

    @property
    def happiness(self):
        return self._happiness

    @happiness.setter
    def happiness(self, value):
        if 100 >= value >= 0:
            self._happiness = value
        else:
            raise ValueError("Happiness must be between 0 ... 100")

    @property
    def cry(self):
        return self._cry

    @cry.setter
    def cry(self, value):
        if 0 > value >= -5:
            self._cry = value
        else:
            raise ValueError("Cry must be between 0 ... -5")


jane = Dog("jane", 4)
jane.happiness = 10
jane.cry = -5
print("Happy =", jane.happiness)
print("Cry =", jane.cry)

print('-----')


class ParentClass:

    @classmethod
    def method(cls, arg):
        print("%s classmethod. %d" % (cls.__name__, arg))

    @classmethod
    def call_original_method(cls):
        cls.method(5)

    def cal_class_method(self):
        self.method(10)


class ChildClass(ParentClass):

    @classmethod
    def call_original_method(cls):
        cls.method(6)


ParentClass.method(0)
ParentClass.call_original_method()

ChildClass.method(0)
ChildClass.call_original_method()

my_obj = ParentClass()
my_obj.method(1)
my_obj.cal_class_method()

print('-------')


class Square:
    _side = 25

    def __init__(self, name, side):
        self.name = name
        self.side = side

    @property
    def side(self):
        return self._side

    @side.setter  # декораторы .setter должны называться так же, как и метод,
    # помеченный декоратором @property, для которого вы хотите
    # устанавливать значение, иначе интерпретатор выдаст ошибку
    def side(self, value):
        if value > 0:
            self.value = value

    @property
    def area(self):
        return self.side ** 2


print(Square("area =", 5).area)

print('---')
