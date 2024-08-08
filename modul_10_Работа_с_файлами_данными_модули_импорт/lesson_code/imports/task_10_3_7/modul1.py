PI = 3.14


def square_circle(r):
    return r ** 2 * PI


def square_rectangle(a):
    return a ** 2


if __name__ == '__main__':
    assert square_circle(5) == 78.5
    assert square_rectangle(8) == 64
