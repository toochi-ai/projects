import asyncio
import time


#  корутина или софункция которую можно исполнять в асинхронной среде
async def async_func():
    print('Запуск!')
    # ожидаем завершения асинхронной операции длительностью 1 секунду
    await asyncio.sleep(1)
    print('Готово!')


#  корутина или софункция которую можно исполнять в асинхронной среде
async def main():
    # ожидаем завершения асинхронной операции
    await async_func()


if __name__ == "__main__":
    tm = time.time()
    # запускаем асинхронную задачу на выполнение
    asyncio.run(main())
    print(f'total time elapsed {time.time() - tm}')
print('---')


def sync_func():
    print('Синхронный запуск')
    time.sleep(1)
    print('Синхронный готово')


async def async_func():
    print('Запуск')
    await asyncio.sleep(1)
    print('Готово!')


async def main():
    sync_func()
    await async_func()


if __name__ == "__main__":
    tm = time.time()
    asyncio.run(main())
    print(f'total time elapsed {time.time() - tm}')
print('---')


def sync_func():
    print('Синхронный запуск')
    time.sleep(1)
    print('Синхронный готово')


async def async_func():
    print('Запуск!')
    await asyncio.sleep(1)
    print('Готово!')


async def main():
    await async_func()
    await async_func()


if __name__ == "__main__":
    tm = time.time()
    asyncio.run(main())
    print(f'total time elapsed {time.time() - tm}')
print('---')


async def async_func():
    print('Запуск')
    await asyncio.sleep(1)
    print('Готово!')


async def main():
    # ожидаем выполнения нескольких корутин одновременно
    await asyncio.wait([async_func(), async_func()])


if __name__ == "__main__":
    tm = time.time()
    asyncio.run(main())
    print(f'total time elapsed {time.time() - tm}')
