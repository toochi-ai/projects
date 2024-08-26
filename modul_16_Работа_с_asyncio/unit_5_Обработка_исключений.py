import asyncio
import time


def handle_exception(loop, context):
    # context["message"] will always be there; but context["exception"] may not
    msg = context.get("exception", context["message"])
    print(f"Перехвачено исключение: {msg}")
    print("Выполняем очистку ресурсов...")


async def async_func_exception():
    print(f'Асинхронная задача начата')
    await asyncio.sleep(1)
    raise RuntimeError('Во время выполнения асинхронной задачи произошел сбой')


async def main():
    try:
        # добавляем обработчик исключений к циклу событий
        loop = asyncio.get_event_loop()
        loop.set_exception_handler(handle_exception)
        # работаем дальше как обычно
        await asyncio.wait([async_func_exception(), async_func_exception()])
    except Exception as e:
        print(f'Exception: {e}')
    print('Завершение выполнения асинхронных задач')

    if __name__ == "__main__":
        tm = time.time()

        asyncio.run(main())
        print(f'Общее время работы {time.time() - tm}')


print('---')


async def async_funk_exception():
    try:
        print(f'Асинхронная задача начата')
        await asyncio.shield(asyncio.sleep(5))
        raise RuntimeError('Во время выполнения асинхронной задачи произошел сбой')
    except asyncio.exceptions.CancelledError as e:
        print('Задача была отменена')
        raise


async def main_():
    try:
        t1 = asyncio.create_task(async_funk_exception())
        t2 = asyncio.create_task(async_funk_exception())
        await asyncio.sleep(1)

        t1.cancel()
        result = await asyncio.gather(t1, t2, return_exceptions=True)
        print(result)
    except Exception as e:
        print(f'Exception: {e}')
    except asyncio.exceptions.CancelledError as e:
        print('Задача прервана {e}')
    print('Завершение выполнения асинхронных задач')

    if __name__ == '__main__':
        tm = time.time()
        asyncio.run(main())
        print(f'Общее время работы {time.time() - tm}')
