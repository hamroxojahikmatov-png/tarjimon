from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


lang_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="🇺🇿 Uzb", callback_data="uz"),
        ],
        [
        InlineKeyboardButton(text="🇷🇺 Russia", callback_data="ru"),
        ],
        [
        InlineKeyboardButton(text="🇺🇸 English", callback_data="en"),
        ],
        [
        InlineKeyboardButton(text="🇫🇷 France", callback_data="fr"),
        ],
        [
        InlineKeyboardButton(text="🇸🇦 Arabic", callback_data="ar"),
        ],
        [
        InlineKeyboardButton(text="🇮🇹 Italy", callback_data="it"),
        ],
        [
        InlineKeyboardButton(text="🇨🇳 China", callback_data="zh"),
        ],
    ],
)