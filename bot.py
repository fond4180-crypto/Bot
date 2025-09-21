import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# токен бота (лучше брать из переменных окружения Render → Environment → TOKEN)
TOKEN = os.getenv("TOKEN", "8193283489:AAGcv2EwmIUB1b02KgnMhvA4KxCtyeX5_fA")

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    kb = [
        [KeyboardButton(
            text="Открыть Shanyraq",
            web_app=WebAppInfo(url="https://fond4180-crypto.github.io/HANN/")
        )]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Привет! 👋 Жми кнопку, чтобы открыть Shanyraq", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
