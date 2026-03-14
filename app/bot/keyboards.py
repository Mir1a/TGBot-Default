from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

from app.bot import Btn


def main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        [
            [Btn.ABOUT_BOT, Btn.ABOUT_ME],
            [Btn.CONTACTS, Btn.STACK],
        ],
        resize_keyboard=True,
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
