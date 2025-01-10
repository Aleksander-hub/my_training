from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
api = "BOT TOKEN HERE"
bot = Bot(token= api)
dp = Dispatcher(bot, storage= MemoryStorage())


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text = 'Информация')
button2 = KeyboardButton(text = 'Рассчитать')
kb.row(button1, button2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Я бот помогающий твоему здоровью.", reply_markup = kb)

@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Я бот, рассчитаю норму калорий в сутки, формула Миффлина-Сан МаЖора.')


@dp.message_handler(text = "Рассчитать")
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state= UserState.age)
async def age_handler(message, state):
    await state.update_data(ag = message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state= UserState.growth)
async def growth_handler(message, state):
    await state.update_data(grow = message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state= UserState.weight)
async def weight_handler(message, state):
    await state.update_data(weig = message.text)
    data = await state.get_data()
    calories = int(10 * int(data['weig']) + 6.25 * int(data['grow']) - 5 * int(data['ag']) - 161)
    await message.answer(f"Ваша норма {calories} калорий.")
    await message.answer("Совет! Не жрать на ночь.")
    await state.finish()


# Этот хэндлер будет срабатывать на остальные любые сообщения
@dp.message_handler()
async def all_massages(message):
    await message.answer(message.text) # эхо ответ
    await message.answer("Привет! Я бот.")
    await message.answer("Введите команду '/start', чтобы начать.")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
