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
    "49": "BAACAgQAAxkBAAMWaGirX43xZF8ei5hPR2HrI329EE8AAuwFAAKTMqBTkQNk7LUmAxY2BA",
    "50": "BAACAgIAAxkBAAMMaHM4p3lT7T_TzmheAAHg9GcYFfznAALWgQACMh-ASyh4oNNBJ6CdNgQ",
    "51": "BAACAgIAAxkBAAMOaHM46Dsnl7PZuY_gPhqF0Ndr-7oAAqVsAAL9BZFLtknhp84cF102BA",
    "52": "BAACAgEAAxkBAAMQaHM5G01uNXQWXTd1dsZKeLBMLQEAAnwBAALbTWhFRu8dc4Pa_Mo2BA",
    "53": "BAACAgQAAxkBAAMSaHM5TQ5fR11U_utEoGmL4RtGGGwAAlYIAAIdeYhRwT0IkCafqWU2BA",
    "54": "BAACAgQAAxkBAAMUaHM5eisEj-_9Mq4e1QeXEu1OsjIAAoEIAALf2whQCydEdJ1xWZQ2BA",
    "55": "BAACAgIAAxkBAAMWaHM5pTF9XGFfBC-zNFZ3kX75HIIAAuwKAAIkZxlKkP1ejxb80H82BA",
    "56": "BAACAgQAAxkBAAMYaHM52a94hUc4x9uHKEBG8lfmoXAAArAJAALkqiFSLB7DTbHimjo2BA",
    "57": "BAACAgQAAxkBAAMaaHM6GSRZIAi9EfkXkCye6GWx2dsAAgUIAAIXQwFSTAxZvdUagTA2BA",
    "58": "BAACAgEAAxkBAAMcaHM6X7oeS46ct4ZL41SettvD78AAAuMBAAK_byhF_fmldBbg4uA2BA",
    "59": "BAACAgIAAxkBAAMeaHM6g8F-1ci8LxhzwUiIgYINLPYAAlwSAAIt2UlIk34YrCCT-_I2BA",
    "60": "BAACAgQAAxkBAAMgaHM6spIpmzOC7A_lAAGyLX49ae1BAAI8CwAC8n_hUk7ACE8RF_ULNgQ",
    "61": "BAACAgIAAxkBAAMiaHM65oTZYLbNGczzruKYWXoTZfkAAusHAAKTKbFKxM8AAafVmpLjNgQ",
    "62": "BAACAgIAAxkBAAMkaHM7IPpAwTvLdjQSg9DzeB76sTEAAn4IAALr1bBK9uvyQkRIsGE2BA",
    "63": "BAACAgQAAxkBAAMmaHM7S_kPAZB7xrwRMrq9KLaLWQsAAh0LAALZmsFR1l9dRQABmaaZNgQ",
    "64": "BAACAgQAAxkBAAMoaHM7ddOxgd4Z--Il6G8zEKUr0doAAuwJAAJfRdFRetBCpVAWl2Q2BA",
    "65": "BAACAgQAAxkBAAMqaHM7s9UFJj60jNcWPzv8nfYCX2cAAncNAAJ31DhTCzQH7WubxSU2BA",
    "66": "BAACAgIAAxkBAAMsaHM73bcfUG3Nk-GtWeur0DZ80HIAAmEFAAIuiNlJHKN3DXyFUQY2BA",
    "67": "BAACAgIAAxkBAAMuaHM8DYzKDOTqIwj-jqYrf4FR1rcAAroIAAJFimBIU0nGc6wcKlk2BA",
    "68": "BAACAgIAAxkBAAMwaHM8QDwUBhnNQ8xg1hG7gWOapsQAAu8BAALFTAFJigZRrXwxAbw2BA",
    "69": "BAACAgEAAxkBAAMyaHM8fb93vXz75xN4vIYOI2JCDcMAAsMBAAJVAAGwR73jqrQuCt7BNgQ",
    "70": "BAACAgQAAxkBAAM0aHM8rZ6sFRgOh4SqLtBMVtKWI4sAAjkJAALykkBQ-g87-avm_mc2BA",
    "71": "BAACAgQAAxkBAAM2aHM84Wgk_oEqEbl9I1YDRB0dilAAAvIKAALA7jFRh_LVfjPx_Vg2BA",
    "72": "BAACAgQAAxkBAAM4aHM9C_2VfiokjIMaxdN7NE07FIAAAv4KAALA7jFRc8Yl_-6Kn0I2BA",
    "73": "BAACAgIAAxkBAAM6aHM9VGl9MP7wHv8xcoN1Q7SR6B4AAjEIAAKrrzlJXPC5d5EQPGo2BA",
    "74": "BAACAgQAAxkBAAM8aHM9gBklfh1Bpxrv2O33BvHehmIAAtIMAAKD_6hRyYE0h9Znakc2BA",
    "75": "BAACAgQAAxkBAAM-aHM9sTaDsmZsqVG-C6vjX1IZ2BkAAmkJAAKY9jBSiBUom5aFdpY2BA",
    "76": "BAACAgIAAxkBAANAaHM94dH_f19UKw50qS9JdNrNJlMAAqcIAAIGV_BIDZaXeoRofcA2BA",
    "77": "BAACAgQAAxkBAANCaHM-FPEetTPd3X7_z3Lh8GSPNt8AArQIAAI6tjBRrPd3vh-2UCk2BA",
    "78": "BAACAgEAAxkBAANEaHM-RBJ2frC0s2AK2wABlP3hpWWzAAJnAQACwRhoRgrUXlERWIhENgQ",
    "79": "BAACAgEAAxkBAANGaHM-fi7-0YUufcnZP1sU0UESovMAAsMFAAKv97BHrZvgDpCoOus2BA",
    "80": "BAACAgQAAxkBAANIaHM-qBgt2kx9Pp8kUbK-hjQH25UAAl0SAAIiXWhRUqz-DbfZe3o2BA"
    
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


 
