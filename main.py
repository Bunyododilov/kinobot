from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram import F
import asyncio

# ——— Replit/Render uchun server qismi
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot ishlayapti!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
# ———————————————————

# Bot tokeningiz
bot = Bot(token="7874277238:AAFMjafESzwtn7eqGdreXvCLiiwUiUy_8Mk")
dp = Dispatcher()

# Kodlar va video file_id lar
videos = {
    "34": "BAACAgQAAxkBAAMWaGirX43xZF8ei5hPR2HrI329EE8AAuwFAAKTMqBTkQNk7LUmAxY2BA"
}

@dp.message(F.text)
async def send_video(message: Message):
    code = message.text.strip()
    if code in videos:
        await message.answer_video(videos[code])
    else:
        await message.answer("❌ Bunday kodli video topilmadi.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    keep_alive()
    asyncio.run(main())
