# 🤖 naadegda_bot

Telegram-бот для автоматического приветствия новых участников канала [@shitnadegda](https://t.me/shitnadegda) и предоставления полезных ссылок. Разработан в рамках проекта **«Щит Надежды» 🇮🇱** — добровольческой инициативы поддержки израильских солдат.

---

## 🚀 Возможности

- 📩 Отправка приветственного сообщения при запуске
- 📎 Прикрепление медиа (баннер и QR-код)
- 💬 Инлайн-кнопки: «О канале», «Написать боту», «Поддержать», «Полезные ссылки»

---

## 📦 Установка

```bash
git clone https://github.com/Alllexx4/naadegda_bot.git
cd naadegda_bot
python -m venv venv
venv\Scripts\activate   # или source venv/bin/activate в Linux/macOS
pip install -r requirements.txt
```

---

## ⚙️ Настройка

Создайте `.env` файл в корне проекта:

```env
BOT_TOKEN=ваш_токен_бота
CHANNEL_ID=@shitnadegda
```

---

## ▶️ Запуск

```bash
python bot.py
```

Или в Windows:

```bash
run_bot.bat
```

---

## 📁 Структура проекта

```
naadegda_bot/
├── bot.py               # Основной код бота
├── config.py            # Загрузка конфигурации из .env
├── welcome_text.md      # Текст приветствия
├── run_bot.bat          # Быстрый запуск на Windows
├── requirements.txt     # Зависимости
├── .gitignore
├── media/
│   ├── 1platyg.png      # QR-код
│   └── Designer_1.png   # Баннер
```

---

## 💙 Поддержать проект

[QR-ссылка на оплату](https://bitpay.co.il/?phone=9725281511113)

---

## 🛡 Автор и проект

Проект поддерживается волонтёрами Telegram-канала [@shitnadegda](https://t.me/shitnadegda).  
Контакт для сотрудничества: [@naadegda_bot](https://t.me/naadegda_bot)