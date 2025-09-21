from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "8193283489:AAGcv2EwmIUB1b02KgnMhvA4KxCtyeX5_fA"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(
        text="Открыть Shanyraq",
        web_app=types.WebAppInfo(url="https://fond4180-crypto.github.io/HANN/")
    )
    kb.add(btn)
    await message.answer("Привет! 👋 Жми кнопку, чтобы открыть Shanyraq", reply_markup=kb)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
