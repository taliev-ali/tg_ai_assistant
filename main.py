print("⚡️ Стартуем бота с токеном:", BOT_TOKEN)
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

from handlers.tasks import register_task_handlers

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Регистрируем хендлеры
register_task_handlers(dp)

# Старт
if __name__ == "__main__":
    print("🚀 Бот запущен")
    executor.start_polling(dp, skip_updates=True)
