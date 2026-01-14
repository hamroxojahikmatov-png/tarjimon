from googletrans import Translator


async def tarjimon(user_text, user_lang):
    translator = Translator()
    natja = await translator.translate(text=user_text, dest=user_lang)
    return natja.text