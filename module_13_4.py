from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
api = "BOT TOKEN HERE"
bot = Bot(token= api)
dp = Dispatcher(bot, storage= MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text = "Calories")
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state= UserState.age)
async def age_handler(message, state):
    await state.update_data(age = message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state= UserState.growth)
async def growth_handler(message, state):
    await state.update_data(growth = message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state= UserState.weight)
async def weight_handler(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    calories = int(10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5)
    await message.answer(f"Ваша норма {calories} калорий")
    await state.finish()


# Этот хэндлер будет срабатывать на остальные любые сообщения
@dp.message_handler()
async def all_massages(message):
    await message.answer(message.text) # эхо ответ
    await message.answer("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Введите команду Calories, чтобы начать общение.")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)