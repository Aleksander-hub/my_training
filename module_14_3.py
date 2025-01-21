from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import asyncio


logging.basicConfig(level= logging.INFO)
api = '7266456982:AAHD3565fBvroH2CqC3dHrOKO7nquuQeQzI'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

in_kb = InlineKeyboardMarkup()
button1 = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
in_kb.row(button1, button2)


kb_Product = InlineKeyboardMarkup()
but1 = InlineKeyboardButton('Продукт 1', callback_data='Product')
but2 = InlineKeyboardButton('Продукт 2', callback_data='Product')
but3 = InlineKeyboardButton('Продукт 3', callback_data='Product')
but4 = InlineKeyboardButton('Продукт 4', callback_data='Product')
kb_Product.row(but1, but2, but3, but4)



kb = ReplyKeyboardMarkup(resize_keyboard=True)
button3 = KeyboardButton(text='Рассчитать')
button4 = KeyboardButton(text='Информация')
button5 = KeyboardButton(text='Купить')
kb.row(button3, button4)
kb.add(button5)




class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()



@dp.message_handler(text='Купить')
async def main_product(message):
    with open('photo/2.jpg', "rb") as img2:
        await message.answer_photo(img2, 'Продукт1 цена 100р')
    with open('photo/3.jpg', "rb") as img3:
        await message.answer_photo(img3, 'Продукт2 цена 200р')
    with open('photo/4.jpg', "rb") as img4:
        await message.answer_photo(img4, 'Продукт3 цена 300р')
    with open('photo/5.jpg', "rb") as img5:
        await message.answer_photo(img5, 'Продукт4 цена 400р')
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_Product)


@dp.callback_query_handler(text='Product')
async def get_product(call):
    await call.message.answer('Вы успешно приобрели продукт!')



@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выбери опцию:', reply_markup=in_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    f = 'Формула Миффлина-Сан Жеора:\n' \
        'для мужчин: 10 х вес + 6.25 x рост – 5 х возраст + 5\n' \
        'для женщин: 10 x вес + 6.25 x рост – 5 x возраст – 161'
    await call.message.answer(f)


@dp.message_handler(text='Информация')
async def info(message):
    with open('1.jpg', "rb") as img:
        await message.answer_photo(img, 'Я бот, рассчитывающий норму калорий')


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст: ')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(ag=message.text)
    await message.answer('Введите свой рост, пожалуйста')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(grow=message.text)
    await message.answer('Введите свой вес, пожалуйста')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weig=message.text)
    data = await state.get_data()
    calories = int(10 * int(data['weig']) + 6.25 * int(data['grow']) - 5 * int(data['ag']) - 161)
    await message.answer(f"Ваша норма {calories} калорий.")
    await message.answer("Совет! Не жрать на ночь.")
    await state.finish()




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)