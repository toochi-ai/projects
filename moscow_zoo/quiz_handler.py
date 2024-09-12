import json

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from aiogram import F

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router, types
from random import sample

from questions import QUESTIONS, ANIMALS

router = Router()


class Quiz(StatesGroup):
    quest = State()
    feedback = State()
    text_to_stuff = State()

    quiz_result = State()
    questions = State()


# Обработчик ошибок
@router.message(Quiz.quest)
async def make_question(message: types.Message, state: FSMContext):
    data = await state.get_data()
    quiz_result, questions = data['quiz_result'], data['questions']

    if message.text.strip().lower() not in ['1', '2', '3', 'старт']:
        await message.answer(f'Выберите ответ: 1, 2 или 3')
        return

    if message.text in ['1', '2', '3']:
        if message.text == '1':
            quiz_result['one'] += 1
        elif message.text == '2':
            quiz_result['two'] += 1
        elif message.text == '3':
            quiz_result['three'] += 1
        await state.update_data({'quiz_result': quiz_result})

    # Дополнительная информация
    if not questions:
        await state.clear()
        win_category = max(quiz_result, key=quiz_result.get)
        for category, animals in ANIMALS.items():
            if category == win_category:
                win_animal = sample(animals, 1)[0]

                result_message = f'🐾 <a href="{win_animal["url"]}">{win_animal["name"]}</a> 🐾 \n\n' \
                                 f'С животным можно подружиться\n' \
                                 f' Жми сюда: ' \
                                 f'<a href="https://moscowzoo.ru/about/guardianship">«Клуб друзей зоопарка»</a>'

                await state.set_data({'result_name': win_animal['name']})
                kb = [
                    [InlineKeyboardButton(text='Еще разок!', callback_data='replay')],
                    [InlineKeyboardButton(text='Связаться с сотрудником Зоопарка', callback_data='contact')],
                    [InlineKeyboardButton(text='Поделиться в VK', callback_data='replay',
                                          url=f'https://vk.com/share.php?url={win_animal["url"]}'
                                              f'&title=@totem_zoo_bot\nТвое тотемное животное: {win_animal["name"]}'
                                              f'&image={win_animal["photo"]}', )],
                    [InlineKeyboardButton(text='Оставить отзыв', callback_data='feedback')]
                ]
                inlinekb = InlineKeyboardMarkup(inline_keyboard=kb)

                # Окончание викторины
                await message.answer(f'Твое тотемное животное в Московском зоопарке – {win_animal["name"]}',
                                     reply_markup=types.ReplyKeyboardRemove())
                await message.answer_photo(photo=win_animal['photo'])

                await message.answer(result_message, parse_mode='HTML', reply_markup=inlinekb)

                return

    question = sample(questions, 1)[0]
    questions.pop(questions.index(question))
    answers = question['answers']
    await state.update_data({'questions': questions})
    builder = ReplyKeyboardBuilder()
    num = ['1', '2', '3']
    for _ in num:
        builder.add(types.KeyboardButton(text=_))
    builder.adjust(4)

    await message.answer(
        f"{question['question']} \n"
        f"1 - {answers[0]}\n"
        f"2 - {answers[1]}\n"
        f"3 - {answers[2]}\n",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )


# Повтор викторины
@router.callback_query(F.data == 'replay')
async def replay(callback: types.CallbackQuery, state: FSMContext):
    await state.set_data(
        {'quiz_result': {
            'one': 0,
            'two': 0,
            'three': 0},
            'questions': QUESTIONS.copy()}
    )

    # Старт викторины
    await state.set_state(Quiz.quest.state)
    kb = [[types.KeyboardButton(text='Старт')]]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await callback.message.answer(f'Жми кнопку Старт и начинаем!', reply_markup=keyboard)
    await callback.answer()


# Контакты и обратная связь
@router.callback_query(F.data == 'contact')
async def contact(callback: types.CallbackQuery, state: FSMContext):
    feedback = await state.get_data()
    buttons = [[types.KeyboardButton(text=f'Результат опроса: \n{feedback}')]]
    kb = types.ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )
    await callback.message.answer(f'Наши контакты: \n\n'
                                  f' Telegram: @Moscowzoo_official\n'
                                  f' E-mail: zoofriends@moscowzoo.ru \n'
                                  f' телефон: +7 (499) 252 - 29 - 51', reply_markup=kb)
    await state.set_state(Quiz.text_to_stuff.state)
    await callback.answer()


@router.message(Quiz.text_to_stuff)
async def text_to_stuff(message: types.Message, state: FSMContext):
    await message.copy_to(chat_id=1875707606, reply_markup=types.ReplyKeyboardRemove())
    await state.clear()


# Отзыв
@router.callback_query(F.data == 'feedback')
async def feedback_state(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Quiz.feedback.state)
    await callback.message.answer(
        f'Твой отзыв важен для нас')
    await callback.answer()


@router.message(Quiz.feedback)
async def feedback_add(message: types.Message, state: FSMContext):
    with open('feedback.json', 'r', encoding='utf8') as fb_file:
        fb = json.load(fb_file)
        with open('feedback.json', 'w', encoding='utf8') as new_fb_file:
            new = {
                'feedback': message.text,
                'user': message.from_user.username
            }
            fb.append(new)
            new_data = json.dumps(fb, indent=4, ensure_ascii=False)
            new_fb_file.write(new_data)

    await message.answer(f'Да прибудет с тобой сила!')
    await state.clear()
