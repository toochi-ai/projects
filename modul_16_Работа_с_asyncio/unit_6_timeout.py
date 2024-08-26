import time
import asyncio


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
