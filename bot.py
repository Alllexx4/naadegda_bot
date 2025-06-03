from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN, CHANNEL_ID
import logging
import os

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode="Markdown")
dp = Dispatcher(bot)

# Чтение приветственного текста
with open("welcome_text.md", "r", encoding="utf-8") as f:
    WELCOME_TEXT = f.read()

# Команда для ручного теста приветствия
@dp.message_handler(commands=["sendtest"])
async def send_test_welcome(message: types.Message):
    if message.chat.type == "private":
        buttons = types.InlineKeyboardMarkup(row_width=2)
        buttons.add(
            types.InlineKeyboardButton("📌 О канале", url="https://t.me/shitnadegda"),
            types.InlineKeyboardButton("💬 Написать боту", url="https://t.me/naadegda_bot"),
            types.InlineKeyboardButton("💰 Поддержать", url="https://bitpay.co.il/?phone=9725281511113"),
            types.InlineKeyboardButton("📎 Полезные ссылки", url="https://t.me/shitnadegda")
        )

        await bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=open("media/Designer_1.png", "rb"),
            caption=WELCOME_TEXT,
            reply_markup=buttons
        )

        await bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=open("media/1platyg.png", "rb"),
            caption="📲 QR-код для поддержки проекта"
        )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
