import asyncio


async def async_task():
    return print('Задача выполнена')


async def main():
    # поставили в расписание async_task()для выполнение в ближайшее время
    # в конкурентном режиме вместе с main()
    task = asyncio.create_task(async_task())

    # объект task можем теперь использовать для управления состоянием
    # задачи или для ожидания ее завершения через await
    await task


asyncio.run(main())
print('---')


# корутина для выполнения некоторой задачи
async def my_task():
    print('Старт')
    # выполняем некоторую асинхронную задачу в течение 0.5 сек
    await asyncio.sleep(0.5)
    print('Я не должен выполняться')


# основная корутина
async def main():
    # создаем асинхронную задачу из корутины
    asyncio.create_task(my_task())
    # ждем завершение еще одной задачи
    await asyncio.sleep(0.5)
    print('Хватит')


asyncio.run(main())
