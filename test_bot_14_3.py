import asyncio
import logging
from tkinter.tix import Form
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, state
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State


logging.basicConfig(level= logging.INFO)
bot = Bot(token='------------')
dp = Dispatcher()

in_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
    [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]])


kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Расcчитать'),
                                    KeyboardButton(text='Информация')]],
                               resize_keyboard=True,
                               input_field_placeholder='Выберите пункт меню...')



class User_State(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(F.text == 'Расcчитать')
async def main_menu(message: Message):
    await message.answer('Выбери опцию:', reply_markup=in_kb)


@dp.message(F.text == 'Информация')
async def info(message: Message):
    await message.answer('Я бот, рассчитывающий норму калорий')


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.callback_query(F.data == 'formulas')
async def get_formulas(callback: CallbackQuery):
    f = 'Формула Миффлина-Сан Жеора:\n' \
        'для мужчин: 10 х вес + 6.25 x рост – 5 х возраст + 5\n' \
        'для женщин: 10 x вес + 6.25 x рост – 5 x возраст – 161'
    await callback.message.answer(f)



@dp.callback_query(F.data == 'calories')
async def set_age(callback: CallbackQuery):
    await callback.message.answer('Введите свой возраст: ')
    await callback.state.set_state(User_State.age)

@dp.message(User_State.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост, пожалуйста')
    await state.set_state(User_State.growth)

@dp.message(User_State.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес, пожалуйста')
    await state.set_state(User_State.weight)

@dp.message(User_State.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = state.get_data()
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


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')


