import queue
import random
import threading
import time
from multiprocessing import Pool

gX = 0
threadsInfo = {}
lock = threading.Lock()


def threadFunc(threadMark):
    print('thread started')
    global gX
    while True:
        with lock:
            if gX >= 10000:
                break

            gX = gX + 1
            threadsInfo[threadMark] += 1
            print(f'thread {threadMark}: {gX}')


if __name__ == "__main__":
    threads = []
    for i in range(3):
        threadMark = f'Thread - {i}'
        threadsInfo[threadMark] = 0
        thread = threading.Thread(target=threadFunc, args=(threadMark,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(threadsInfo)
print('---')


# Попытка сделать потокобезопасный класс
class SomeLockClass:
    def __init__(self):
        # внутренние переменные
        self.a = 1
        self.b = 2
        # внутренний лок
        self.lock = threading.RLock()

    # потокобезопасный метод изменения параметра а
    def changeA(self, a):
        with self.lock:
            self.a = a

    # потокобезопасный метод изменения параметра b
    def changeB(self, b):
        with self.lock:
            self.b = b

    # потокобезопасный метод одновременной смены параметров
    def changeAB(self, a, b):
        # зачем-то мы ещё раз используем лок перед вызовом и без того потокобезопасных методов
        with self.lock:
            self.changeA(a)  # зависания не будет
            self.changeB(b)


# максимальный размер произведённой продукции
g_maxProduct = 100
# переменная склада
g_storage = []
# лок
g_lock = threading.Lock()


def producer():
    # код производителя
    for i in range(g_maxProduct):
        with g_lock:
            # отправляем продукцию на склад
            g_storage.append(random.randint(0, 100))


def consumer():
    # код потребителя
    pop_count = 0
    while True:
        with g_lock:
            # получаем продукцию со склада
            if g_storage:
                pop_count += 1
                print(f"{pop_count}: {g_storage.pop()}")
        if pop_count == g_maxProduct:
            break


if __name__ == '__main__':
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
print('---')

g_maxProduct = 100
g_storage = []
g_lock = threading.BoundedSemaphore(3)


def producer():
    for i in range(g_maxProduct):
        g_lock.acquire()
        g_storage.append(random.randint(0, 100))


def consumer():
    pop_count = 0
    while True:
        if g_storage:
            pop_count += 1
            print(f"{pop_count}: {g_storage.pop()}")
            g_lock.release()
        if pop_count == g_maxProduct:
            break


if __name__ == '__main__':
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
print('---')

#  События
#
# Объект Event — это потокобезопасный признак,
# который потоки могут устанавливать и снимать.

event = threading.Event()


def threadFunc():
    print("thread started")
    event.wait()
    print("event --> process")


if __name__ == "__main__":
    t = threading.Thread(target=threadFunc, args=())
    t.start()
    # пока мы не установим флаг,
    # ожидающие потоки будут приостановлены
    time.sleep(3)
    event.set()

    t.join()
print('---')

#  Состояния
#
# Объект Condition — это своеобразный гибрид объектов Lock и Event.
# Он позволяет захватывать событие при помощи метода acquire(),
# ожидать доступности методом wait() и оповещать о доступности методом notify()
#
# condition = threading.Condition()
#
#
# def producer():
#     condition.acquire()
#     # код производителя
#     condition.notify_all()
#     condition.release()
#
#
# def consumer():
#     condition.acquire()
#     # ожидаем доступности
#     condition.wait()
#     # код потребителя
#     condition.release()

g_lock = threading.Condition()


def producer():
    #  код производителя
    for i in range(g_maxProduct):
        #  захватываем лок
        with g_lock:
            g_storage.append(random.randint(0, 100))
            # говорим о том, что есть продукция
            g_lock.notify()


def consumer():
    # код потребителя
    pop_count = 0
    while True:
        with g_lock:
            # если склад пуст, ожидаем новых поступлений
            if not g_storage:
                g_lock.wait()
            pop_count += 1
            print(f"{pop_count}: {g_storage.pop()}")

        if pop_count == g_maxProduct:
            break


if __name__ == '__main__':
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
print('---')

#  Очереди
#
# Другой способ синхронизации заключается в использовании потокобезопасных очередей Queue,
# которые позволяют одному потоку (производителю) вставлять сообщения в очередь,
# а другому (потребителю) — извлекать их из очереди и использовать (как на конвейере).

# событие, которое служит для потребителя признаком,
# что событий можно больше не ждать
event = threading.Event()


# производитель, который производит 10 сообщений
# и кладёт их в очередь
def producerFunc(q):
    for i in range(1, 11):
        time.sleep(0.1)  # время, чтобы произвести сообщение
        q.put(f"message {i}")
    event.set()


# потребитель, который считывает события из очереди
def consumerFunc(q):
    while not event.is_set() or not q.empty():
        print(q.get())


if __name__ == '__main__':
    # создаём очередь, передаём её в потоки и запускаем на выполнение
    q = queue.Queue()
    producer = threading.Thread(target=producerFunc, args=(q,))
    consumer = threading.Thread(target=consumerFunc, args=(q,))

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

print('---')


#  Использование пулов (Pools)
#  Иногда нам нужно просто делегировать какое-то вычисление или обработку объектов потокам
#  или процессам-исполнителям и получить от них результат. Можно упростить себе жизнь и
#  воспользоваться пулами потоков/процессов. В этом случае нам не понадобится использование
#  очередей или других объектов синхронизации, поскольку объекты синхронизации уже включены
#  во внутреннюю реализацию пулов.
#
# Для того чтобы воспользоваться пулом процессов, нужно создать объект Pool из модуля multiprocessing.

def procFunc(number):
    return number * number


if __name__ == '__main__':
    # параметры, с которыми мы хотим проводить вычисление
    numbers = [5, 10, 20]
    # создаём объект Pool с указанием количества "работников"
    pool = Pool(processes=3)
    # для каждого объекта из списка Pool автоматически назначает работника
    mapped = pool.map(procFunc, numbers)
    print(mapped)
