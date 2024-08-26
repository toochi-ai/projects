import asyncio
import time

async def some_long_async_task():
    try:
        print('Длительная задача начата')
        await asyncio.sleep(60)
        print('Длительная задача завершена')
    except asyncio.exceptions.CancelledError:
        print('Длительная задача прервана')


async def main():
    try:
        await asyncio.wait_for(asyncio.shield(some_long_async_task()), 2.0)
    except asyncio.exceptions.TimeoutError:
        print('Таймаут выполнения задачи')
    except Exception as e:
        print(f'Exception: {e}')
    except asyncio.exceptions.CancelledError as e:
        print(f'Задача прервана')
    print('Завершение выполнения асинхронных задач')


if __name__ == '__main__':
    tm = time.time()
    asyncio.run(main())
    print(f'Общее время работы {time.time() - tm}')
print('---')


async def some_async_task(timeout):
    try:
        print('Длительная задача начата')
        await asyncio.sleep(timeout)
        print('Длительная задача завершена')
    except asyncio.exceptions.CancelledError:
        print('Длительная задача прервана')


async def main():
    try:
        done, undone = await asyncio.wait(
            [some_async_task(0.5), some_async_task(1.0), some_async_task(5), some_async_task(10)], timeout=2.0)
        print(f'Задачи готовы {[t.get_name() for t in done]}')
        print(f'Задачи не готовы {[t.get_name() for t in undone]}')
    except asyncio.exceptions.TimeoutError:
        print('Таймаут выполнения задачи')
    except Exception as e:
        print(f'Exception: {e}')
    except asyncio.exceptions.CancelledError as e:
        print(f'Задача прервана')
    print('Завершение выполнения асинхронных задач')


if __name__ == "__main__":
    tm = time.time()
    asyncio.run(main())
    print(f'Общее время работы {time.time() - tm}')
print('---')


async def some_async_task(timeout):
    try:
        print('Длительная задача начата')
        await asyncio.sleep(timeout)
        print('Длительная задача завершена')
    except asyncio.exceptions.CancelledError:
        print('Длительная задача прервана')
        return None
    return f'Результат за {timeout} секунд'


async def main():
    try:
        # перебираем все задачи начиная с тех которые выполняются раньше
        for task in asyncio.as_completed(
                [some_async_task(0.5), some_async_task(1.0), some_async_task(5), some_async_task(10)], timeout=2.0):
            earliest_result = await task
            print(earliest_result)
    except asyncio.exceptions.TimeoutError:
        print('Таймаут выполнения задачи')
    except Exception as e:
        print(f'Exception: {e}')
    except asyncio.exceptions.CancelledError as e:
        print(f'Задача прервана')
    print('Завершение выполнения асинхронных задач')


if __name__ == "__main__":
    tm = time.time()
    asyncio.run(main())
    print(f'Общее время работы {time.time() - tm}')
print('---')
