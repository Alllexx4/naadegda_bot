from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN, CHANNEL_ID
from dotenv import load_dotenv
import logging
import os
import asyncio
from aiohttp import web

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
    logging.info(f"Получена команда /start от: {message.from_user.full_name}")
    await message.answer("👋 Бот успешно работает!")

# Уведомление при запуске
async def on_startup(dp):
    logging.info("✅ Бот успешно запущен и готов к работе!")
    try:
        await bot.send_message(CHANNEL_ID, "🤖 Бот запущен и работает на Railway!")
    except Exception as e:
        logging.error(f"Ошибка при отправке сообщения о запуске: {e}")

# Aiohttp-сервер для /health
async def handle_health(request):
    return web.Response(text="OK")

async def start_webserver():
    app = web.Application()
    app.router.add_get("/health", handle_health)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()
    logging.info("🌐 HTTP-сервер /health запущен на порту 8080")

# Совмещённый запуск: и бота, и HTTP-сервера
async def main():
    await asyncio.gather(
        start_webserver(),
        on_startup(dp),
        dp.start_polling()
    )

if __name__ == "__main__":
    logging.info("🚀 Запуск бота и веб-сервера...")
    asyncio.run(main())