import threading

# общая переменная
gX = 0

# функция, которая увеличивает на 1 gX 100000 раз
def threadFunc():
    print('thread started')
    global gX
    for i in range(100000):
        gX = gX + 1


if __name__ == "__main__":
    gX = 0

    # запускает выполнение функции в пяти потоках
threads = []
for i in range(10):
    threads.append(threading.Thread(target=threadFunc, args=()))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(gX)
