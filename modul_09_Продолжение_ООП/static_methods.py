class Square:
    def __init__(self, side):
        self.side = side


class SquareFactory:
    @staticmethod
    def create_square(side):
        return Square(side)


print(SquareFactory.create_square(50).side)


class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y


result_1 = MathUtils.add(5, 3)
result_2 = MathUtils.multiply(4, 6)

print(result_1, result_2)
#  нужна настройка для git