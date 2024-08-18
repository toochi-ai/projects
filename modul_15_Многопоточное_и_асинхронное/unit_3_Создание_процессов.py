import os
from multiprocessing import Process


# определяем функцию, которую будем передавать в процесс
def procFunc(parameter):
    print("process procFunc parameter:", parameter)


if __name__ == "__main__":
    # создаём объект Process, передаём ему функцию и параметры вызова
    p = Process(target=procFunc, args=("#proc parameter",))
    # запускаем процесс на выполнение
    p.start()
    # ожидаем завершения процесса
    p.join()


def procFunc(parameter):
    # выводим информацию о дочернем процессе
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())
    print("process procFunc parameter:", parameter)


if __name__ == "__main__":
    # выводим информацию о родительском процессе
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())

    # создаём дочерние процессы и запускаем их на выполнение, каждый со своим аргументом
    p1 = Process(target=procFunc, args=("proc 1 parameter",))
    p2 = Process(target=procFunc, args=("proc 2 parameter",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

print('---')
