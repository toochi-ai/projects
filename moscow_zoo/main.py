import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from questions import QUESTIONS
from quiz_handler import router, Quiz
from token_data import TOKEN

dp = Dispatcher()
dp.include_router(router)

bot = Bot(token=TOKEN)


@dp.message(CommandStart())
async def command_start_handler(message: types.Message, state: FSMContext):
    await state.set_state(Quiz.quest.state)

    kb = [[types.KeyboardButton(text='Старт')]]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True)
    await message.answer(
        f'Привет {message.from_user.first_name} {message.from_user.last_name}! \nНачинаем викторину какое у '
        f'тебя тотемное животное! \n\nЖми кнопку -Старт-',
        reply_markup=keyboard)

    await state.set_data(
        {'quiz_result': {
            'one': 0,
            'two': 0,
            'three': 0},
            'questions': QUESTIONS.copy()}
    )


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
# настройка pycharm для git после переустановки операционки
