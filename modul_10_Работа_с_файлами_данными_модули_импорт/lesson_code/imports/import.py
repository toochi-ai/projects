import os
import sys

import requests

#import my_stack

MAIN_CONST = 3.14159265358


def main():
    print(MAIN_CONST)
    some_func()


def some_func():
    print(help(os))
    print(help(sys))
    print(help(requests))
 #   print(help(my_stack))


if __name__ == '__main__':
    main()
