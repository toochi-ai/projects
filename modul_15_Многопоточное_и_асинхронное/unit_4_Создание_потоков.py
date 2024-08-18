import threading
import time


# функция, которая будет исполняться в потоке
def threadFunc(parameter):
    print(f"thread started with parameter {parameter}")
    time.sleep(3)
    print("tread finished")


if __name__ == '__main__':
    print("script started")
    # создаём объект Thread
    thread = threading.Thread(target=threadFunc, args=(1,))
    # запускаем его на выполнение
    thread.start()
    # ожидаем завершения
    thread.join()

    print("script finished")
print('---')


def threadFunc(parameter):
    print(f"thread started with parameter {parameter}")
    this_thread = threading.current_thread()
    print(this_thread)
    print(f"name = {this_thread.name}")
    print(f"getName = {this_thread.name}")
    print(f"is_alive = {this_thread.is_alive()}")
    print(f"isDaemon = {this_thread.daemon}")
    print(f"ident = {this_thread.ident}")
    print(f"native_id = {this_thread.native_id}")
    print("thread finished")


if __name__ == '__main__':
    print("script started")
    thread = threading.Thread(target=threadFunc, args=(1,))
    thread.start()
    thread.join()
    print("script finished")
