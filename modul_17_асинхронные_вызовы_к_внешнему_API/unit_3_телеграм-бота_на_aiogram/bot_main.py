from aiogram import Dispatcher, types
from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section
)

from weather_handler import router

dp = Dispatcher()
dp.include_router(router)


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    kb = [
        [
            types.KeyboardButton(text="Команды"),
            types.KeyboardButton(text="Описание бота"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer(f"Привет! С чего начнем?", reply_markup=keyboard)


@dp.message(F.text.lower() == "команды")
async def commands(message: types.Message):
    response = as_list(
        as_marked_section(
            Bold("Команды:"),
            "/weather - weather by city",
            "/forecast - forecast 1 - 5 days",
            "/weather_time - weather by date/time",
            marker="✅ ",
        ),
    )
    await message.answer(
        **response.as_kwargs()
    )


@dp.message(F.text.lower() == "описание бота")
async def description(message: types.Message):
    await message.answer("Этот бот предоставляет информацию о погоде.")
