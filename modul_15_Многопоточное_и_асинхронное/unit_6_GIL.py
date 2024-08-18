import multiprocessing
import threading
import time


# функция, которая увеличивает число на 1 tics раз
def tic(tics):
    res = 0
    for i in range(tics):
        res += 1


if __name__ == '__main__':
    tics = 10000000
    # t1 и t2 используются для вычисления прошедшего времени
    t1 = time.time()
    tic(tics)
    t2 = time.time()

    print(t2 - t1)
print('---')


#  Теперь попробуем сделать то же самое в многопоточной среде:
def tic(tics):
    res = 0
    for i in range(tics):
        res = res + 1


if __name__ == "__main__":
    # создаём n потоков, для каждого из которых вызываем функцию
    # tic с tics/количество потоков, чтобы всё было по-честному
    tics = 10000000
    threads = []
    threads_count = 2
    for i in range(threads_count):
        threads.append(threading.Thread(target=tic, args=(int(tics / threads_count),)))

    t1 = time.time()
    for thread in threads:
        thread.start()

for thread in threads:
    thread.join()

t2 = time.time()

print(t2 - t1)
print('---')


#  Если мы теперь попробуем переписать наш скрипт, перейдя с потоков на процессы, то увидим другую картину:

def tic(tics):
    res = 0
    for i in range(tics):
        res += 1


if __name__ == '__main__':
    tics = 10000000
    processes = []
    processes_count = 2
    for i in range(processes_count):
        processes.append(multiprocessing.Process(target=tic, args=(int(tics / processes_count),)))

    t1 = time.time()
    for process in processes:
        process.start()

    for process in processes:
        process.join()

    t2 = time.time()

    print(t2 - t1)
