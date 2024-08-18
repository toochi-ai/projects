import threading

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
