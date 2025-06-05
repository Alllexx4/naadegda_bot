import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from aiohttp import web
import asyncio

# Загрузка переменных окружения
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# Логирование
logging.basicConfig(level=logging.INFO)

# Telegram Bot
bot = Bot(token=BOT_TOKEN, parse_mode="Markdown")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    logging.info(f"Получена команда /start от: {message.from_user.full_name}")
    await message.answer("👋 Бот работает и слушает команды!")

async def on_startup(dp):
    logging.info("✅ Бот успешно запущен и готов к работе!")
    try:
        await bot.send_message(CHANNEL_ID, "🤖 Бот запущен и работает на Railway!")
    except Exception as e:
        logging.warning(f"Не удалось отправить сообщение в канал: {e}")

# HTTP-сервер для проверки "живости"
async def handle_health(request):
    return web.Response(text="OK")

async def start_web_app():
    app = web.Application()
    app.router.add_get("/health", handle_health)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()
    logging.info("🌐 HTTP-сервер запущен на порту 8080")

# Запуск бота и веб-сервера параллельно
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start_web_app())
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)