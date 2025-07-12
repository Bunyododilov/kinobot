from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import F
import asyncio

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

bot = Bot(token="7874277238:AAFMjafESzwtn7eqGdreXvCLiiwUiUy_8Mk")
dp = Dispatcher()

videos = {
    "34": "BAACAgQAAxkBAAMWaGirX43xZF8ei5hPR2HrI329EE8AAuwFAAKTMqBTkQNk7LUmAxY2BA"
}

required_channels = ["@TELEFON_BOZOR_24_UZB", "@AVTO_BOZOR_24_UZB"]

async def is_subscribed(user_id):
    for channel in required_channels:
        try:
            member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
            if member.status not in ["member", "creator", "administrator"]:
                return False
        except:
            return False
    return True

@dp.message(F.text)
async def send_video(message: Message):
    if await is_subscribed(message.from_user.id):
        code = message.text.strip()
        if code in videos:
            await message.answer_video(videos[code])
            await message.answer_sticker("CAACAgIAAxkBAAEI2oRk8WqU_m_owQABlfK6ucpIRasOmgACoAcAAhZCawABIS3ViWxZKzYE")
        else:
            await message.answer("❌ Bunday kodli video topilmadi.")
    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📱 TELEFON_BOZOR_24_UZB", url="https://t.me/TELEFON_BOZOR_24_UZB")],
            [InlineKeyboardButton(text="🚗 AVTO_BOZOR_24_UZB", url="https://t.me/AVTO_BOZOR_24_UZB")]
        ])
        await message.answer("❗ Kodni yuborishdan oldin quyidagi kanallarga to‘liq obuna bo‘ling. So‘ng qaytadan urinib ko‘ring:", reply_markup=keyboard)
        await message.answer_sticker("CAACAgIAAxkBAAEI2oBk8Wp_sDRBG3U9D0ipkRIYQgOQzAACDgADVp29Cp77RBupC3mNGQQ")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    keep_alive()
    asyncio.run(main())


 
