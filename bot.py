from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN, CHANNEL_ID
from dotenv import load_dotenv
import logging
import os

# Загрузка переменных из .env
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(token=BOT_TOKEN, parse_mode="Markdown")
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("👋 Бот успешно работает!")

# Уведомление при запуске
async def on_startup(dp):
    logging.info("✅ Бот успешно запущен и готов к работе!")
    try:
        await bot.send_message(CHANNEL_ID, "🤖 Бот запущен и работает на Railway!")
    except Exception as e:
        logging.error(f"Ошибка при отправке сообщения о запуске: {e}")

# Запуск бота
if __name__ == "__main__":
    logging.info("🚀 Запуск бота...")
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)