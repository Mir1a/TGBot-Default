from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

from app.bot import BUTTONS


def get_main_keyboard(lang: str) -> ReplyKeyboardMarkup:
    btn = BUTTONS.get(lang, BUTTONS["uk"])
    return ReplyKeyboardMarkup(
        [
            [btn["about_bot"], btn["about_me"]],
            [btn["contacts"], btn["stack"]],
            [btn["language"]],
        ],
        resize_keyboard=True,
    )


def get_language_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🇺🇦 Українська", callback_data="lang_uk"),
                InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
            ]
        ]
    )


def contacts_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("GitHub", url="https://github.com/Mir1a"),
                InlineKeyboardButton(
                    "LinkedIn",
                    url="https://www.linkedin.com/in/matvey-bliznyuk-a735ab303/",
                ),
            ],
        ]
    )
