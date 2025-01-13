from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = "--"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='info')],
        [
            KeyboardButton(text='shop'),
            KeyboardButton(text='donate')
        ]
    ], resize_keyboard=True
)

kb = InlineKeyboardMarkup()
bt = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
bt2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb.add(bt)
kb.add(bt2)

class Form(StatesGroup):
    waiting_for_age = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Мы рады вас видеть.", reply_markup=kb)

@dp.message_handler(text='info')
async def info(message: types.Message):
    await message.answer("Bot info!")

@dp.message_handler(text='shop')
async def shop(message: types.Message):
    await message.answer("Bot shop!")

@dp.message_handler(text='donate')
async def donate(message: types.Message):
    await message.answer("Bot donate!")

@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer('calories = 10 * weight + 6.25 * growth - 5 * age - 161')
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await Form.waiting_for_age.set()  # Устанавливаем состояние
    await call.message.answer('Введите свой возраст:')
    await call.answer()

@dp.message_handler(state=Form.waiting_for_age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    # Здесь вы можете добавить логику для обработки возраста
    await message.answer(f'Ваш возраст: {age}')
    await state.finish()  # Завершаем состояние

# Этот хэндлер будет срабатывать на остальные любые сообщения
@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer("Привет! Я бот.", reply_markup=menu)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
