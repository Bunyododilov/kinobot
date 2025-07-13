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
    "50": "BAACAgIAAxkBAAPHaHNRR2IdB4J3gSSe753EZ72LLbgAAtaBAAIyH4BLA-qd9omVwU82BA",
    "51": "BAACAgIAAxkBAAPzaHOhY-ClEQkoexeISgdf6SXMqOgAAqVsAAL9BZFLUuuLFJkuCvI2BA",
    "52": "BAACAgEAAxkBAAP1aHOhlpQCaVpVEkFgs1cSn10I0NQAAnwBAALbTWhF3efHa5YeJbQ2BA",
    "53": "BAACAgQAAxkBAAP3aHOhzL7xtpVwishupjk_Trqeu4sAAlYIAAIdeYhRlVwpvrQLqR42BA",
    "54": "BAACAgQAAxkBAAP5aHOh_kdVzjtkxQ-7Y_iizAWZ64YAAoEIAALf2whQxum7HsQDbEg2BA",
    "55": "BAACAgIAAxkBAAP7aHOiXs2JKhL-SOlyaukX50KMNOIAAuwKAAIkZxlKpOSQylt_aYg2BA",
    "56": "BAACAgQAAxkBAAP9aHOiqizzRr-x_gu_s5pq4mo5tR4AArAJAALkqiFSD1z6r43vE7o2BA",
    "57": "BAACAgQAAxkBAAP_aHOizYkWf43TuNRvbSu1o24GWz8AAgUIAAIXQwFS1j3j2T2eaXM2BA",
    "58": "BAACAgEAAxkBAAIBAWhzovM6ujmj-CLonV-T7NY0HPhIAALjAQACv28oRbnNwVfb4_pONgQ",
    "59": "BAACAgIAAxkBAAIBA2hzox4tOXsr7N350UWAMvQCl9wdAAJcEgACLdlJSF6VF53B7AfZNgQ",
    "60": "BAACAgQAAxkBAAIBBWhzo0D9QoyXSE9SH5vhdtLG8ze3AAI8CwAC8n_hUv266YF8D8JpNgQ",
    "61": "BAACAgIAAxkBAAIBB2hzo1_iWqU4JRV8mFWO2M-0bcj0AALrBwACkymxSlhwvFEw4WVMNgQ",
    "62": "BAACAgIAAxkBAAIBCWhzo3r1VuUFbGnsMG24_HLD3jTIAAJ-CAAC69WwStgQPeA_6IDbNgQ",
    "63": "BAACAgQAAxkBAAIBC2hzo5rseaN11gNEuNbWpTutO5JgAAIdCwAC2ZrBUf4_rB2ouN01NgQ",
    "64": "BAACAgQAAxkBAAIBDWhzo8EP64TLA_hg8arMRXqHA4fVAALsCQACX0XRUcgJ9vI8vNYTNgQ",
    "65": "BAACAgQAAxkBAAIBD2hzo-LHNc1wEKSz_3KrfgABXOUHKQACdw0AAnfUOFOdX16Ogb3YGTYE",
    "66": "BAACAgIAAxkBAAIBEWhzpAOq91y_RErdRqTfrvTR9mkFAAJhBQACLojZSdJcZdc5LUhDNgQ",
    "67": "BAACAgIAAxkBAAIBE2hzpDh9O6VNqf-vP7fEj_bqKZ8qAAK6CAACRYpgSDDwqmgVJbeoNgQ",
    "68": "BAACAgIAAxkBAAIBFWhzpF-Mrj2bJ72oxh9v-CLIoRg_AALvAQACxUwBSfRSq9ZuF4PINgQ",
    "69": "BAACAgEAAxkBAAIBF2hzpH1HmS7nSxia8AsES1y_ns9FAALDAQACVQABsEcQHsZUysgEPzYE",
    "70": "BAACAgQAAxkBAAIBGWhzpKJhDY4XXckIYF4FlJX83ckJAAI5CQAC8pJAUIafGDcO-b57NgQ",
    "71": "BAACAgQAAxkBAAIBG2hzpMKlfsiKTBsx9kwsDEzVV4KAAALyCgACwO4xUSep4DZmvUuzNgQ",
    "72": "BAACAgQAAxkBAAIBHWhzpO94H7aIXZODeQc6l6OP4f6KAAL-CgACwO4xUWCagpKBZejKNgQ",
    "73": "BAACAgIAAxkBAAIBH2hzpQvY2z7RKGLCsZytm7E8jmzeAAIxCAACq685SdsvVKvL58xrNgQ",
    "74": "BAACAgQAAxkBAAIBIWhzpS_63NUr56-gAwIGEDASIE1TAALSDAACg_-oUVtfFsDVYyvANgQ",
    "75": "BAACAgQAAxkBAAIBI2hzpVz4tRFxanmLq4aYCi5a3erRAAJpCQACmPYwUhyTMUWIf5xJNgQ",
    "76": "BAACAgIAAxkBAAIBJWhzpX3bS42UeibdkA48lmWJ8aZoAAKnCAACBlfwSMdBz_pBwwomNgQ",
    "77": "BAACAgQAAxkBAAIBJ2hzpaWQggjGJjbWoVjXEB4l4bNqAAK0CAACOrYwUehTblex_X1ZNgQ",
    "78": "BAACAgEAAxkBAAIBKWhzpcPdpNzZy9NWeCkWx3OQRggNAAJnAQACwRhoRhJ83VtaboWwNgQ",
    "79": "BAACAgEAAxkBAAIBK2hzpeU67n9Iuq5uLKRvlVz_8wk_AALDBQACr_ewRzztJlacRfSuNgQ",
    "80": "BAACAgQAAxkBAAIBLWhzpgxDa_OJktIERDJ-0MDNzgm9AAJdEgACIl1oUZGL3yuxYnGkNgQ"
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


 
