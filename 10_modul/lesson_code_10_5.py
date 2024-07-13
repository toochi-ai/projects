import time
from datetime import datetime
from contextlib import asynccontextmanager


class Timer:
    def __init__(self):
        pass

    def __enter__(self):
        self.start = datetime.utcnow()
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Time passed: {(datetime.utcnow() - self.start).total_seconds()}")


with Timer():
    time.sleep(2)


with open('file.bin', 'wt') as f:
    f.write('test string')


@asynccontextmanager
def timer():
    start = datetime.utcnow()
    yield
    print(f"Time passed: {(datetime.utcnow() - start).total_seconds()}")


with timer():
    time.sleep(2)


class OpenFile:
    def __init__(self, path, type):
        self.file = open(path, type)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile('hello.txt', 'wt') as f:
    f.write('Мой контекстный менеджер делает то же самое!')
