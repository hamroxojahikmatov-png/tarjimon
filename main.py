from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.types import FSInputFile
from aiogram.client.session.aiohttp import AiohttpSession

import asyncio
import os
import logging
from gtts import gTTS
from inline import lang_btn
from tarjimon import tarjimon

logging.basicConfig(level=logging.INFO)

PROXY_URL = "http://proxy.server:3128"
session = AiohttpSession(proxy=PROXY_URL)
TOKEN = "8550855524:AAHbykH2ZOqwVPpgZ3jPHtELbRVrvAJJJZY"
CHANNEL_ID = "8168638997"

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"), session=session)


dp = Dispatcher()



@dp.message(CommandStart())
async def start_hendler(message: types.Message):
    full_name = message.from_user.full_name
    await message.answer(f"Salom <b>{full_name}</b> botga xush kelibsiz\nTarjima qilmoqchi bo'lgan matningizni kiriting")


user_data = {

}


@dp.message(F.text)
async def get_text(message: types.Message):
    user_text = message.text
    user_data[message.from_user.id] = user_text
    await message.answer("Qaysi tilga tarjima qilmoqchisiz?", reply_markup=lang_btn)

@dp.message(F.text == "/admin")
async def admin_panel(message: types.Message):
    if message.from_user.id == 8168638997:
        await message.answer("Xush kelibsiz admin, qaysi tilni qoshmoqchisiz?")
        await message.answer("Mavjud tillar: O'zbek, Rus, Ingliz, Fransuz, Arab, Italyan, Xitoy")
        await message.answer("Yangi tilni kiriting:")
        @dp.message(F.text)
        async def add_new_language(message: types.Message):
            new_language = message.text
            await message.answer(f"Yangi til qo'shildi: {new_language}")
    else:
        await message.answer("Siz admin emassiz")

@dp.callback_query()
async def get_user_lang(callback: types.CallbackQuery):
    await callback.answer()

    user_id = callback.from_user.id
    user_lang = callback.data
    user_text = user_data.get(user_id)

    if not user_text:
        callback.message.answer ("Avval matn yuboring")
        return
    
    tarjima_matn = await tarjimon(user_text, user_lang)

    file_name = f"voice_{user_id}.mp3"
    try:
        tts = gTTS(text=tarjima_matn, lang=user_lang)
        tts.save(file_name)

        voice = FSInputFile(file_name)
        await callback.message.answer_voice(
        voice=voice,
        caption=tarjima_matn
        )
        os.remove(file_name)
    except:
        await callback.message.answer(f"Uzur bu {user_lang} tilga tarjima qilinmadi😔")



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())