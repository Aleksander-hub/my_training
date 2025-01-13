from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import asyncio


logging.basicConfig(level= logging.INFO)
api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button1 = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
kb.row(button1, button2)  # add

kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
button3 = KeyboardButton(text='Рассчитать')
button4 = KeyboardButton(text='Информация')
kb1.add(button3)
kb1.add(button4)



class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Расcчитать')
async def main_menu(message):
    await message.answer('Выбери опцию:', reply_markup=kb)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb1)


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст: ')
    await UserState.age.set()
    await call.answer


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    f = 'Формула Миффлина-Сан Жеора:\n' \
        'для мужчин: 10 х вес + 6.25 x рост – 5 х возраст + 5\n' \
        'для женщин: 10 x вес + 6.25 x рост – 5 x возраст – 161'
    await call.message.answer(f)


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Я бот, рассчитывающий норму калорий')


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост, пожалуйста')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес, пожалуйста')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = state.get_data
    try:
        age = float(data['age'])
        weight = float(data['weight'])
        growth = float(data['growth'])
    except:
        await message.answer(f'Не могу конвертировать введенные значения в числа.')
        await state.finish()
        return
    calories_man = 10 * weight + 6.25 * growth - 5 * age + 5
    calories_wom = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f'Норма (муж.): {calories_man} ккал')
    await message.answer(f'Норма (жен.): {calories_wom} ккал')
    await state.finish()




@dp.message_handler()
async def all_messages(message):
    print(f'Получено: {message.text}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
