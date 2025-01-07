from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
api = "BOT TOKEN HERE" 
bot = Bot(token= api)
dp = Dispatcher(bot, storage= MemoryStorage())


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message_handler(commands=['start'])
async def start(message):
    print("Привет! Я бот помогающий твоему здоровью.")


# Этот хэндлер будет срабатывать на остальные любые сообщения
@dp.message_handler()
async def all_massages(message):
    print("Введите команду /start, чтобы начать общение.")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
