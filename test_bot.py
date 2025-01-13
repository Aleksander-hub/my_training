from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token= api)
dp = Dispatcher(bot, storage= MemoryStorage())


menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text ='info')],
        [
            KeyboardButton(text ='shop'),
            KeyboardButton(text = 'donate')
        ]
    ], resize_keyboard = True
)

kb = InlineKeyboardMarkup()
bt = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data = 'calories')
bt2 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data = 'formulas')
kb.add(bt)
kb.add(bt2)

@dp.message_handler(text = 'info')
async def info(message):
    await message.answer("Bot info!")

@dp.message_handler(text = 'shop')
async def shop(message):
    await message.answer("Bot shop!")

@dp.message_handler(text = 'donate')
async def donate(message):
    await message.answer("Bot donate!")


@dp.message_handler(text = 'Start')
async def start(message):
    await message.answer("Мы рады вас видеть.", reply_markup = kb)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('calories = 10 * weight + 6.25 * growth - 5 * age - 161')
    await call.answer()

@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()

# Этот хэндлер будет срабатывать на остальные любые сообщения
@dp.message_handler()
async def all_massages(message):
    #await message.answer(message.text) # эхо ответ
    await message.answer("Привет! Я бот.", reply_markup = menu)




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

