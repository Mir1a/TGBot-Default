from telegram import Update
from telegram.ext import ContextTypes

from app.bot import texts
from app.bot.keyboards import Btn, contacts_keyboard, main_keyboard


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        return
    match update.message.text:
        case Btn.ABOUT_BOT:
            await update.message.reply_text(texts.ABOUT_BOT, parse_mode="MarkdownV2")
        case Btn.ABOUT_ME:
            await update.message.reply_text(texts.ABOUT_ME, parse_mode="MarkdownV2")
        case Btn.CONTACTS:
            await update.message.reply_text(
                texts.CONTACTS,
                parse_mode="MarkdownV2",
                reply_markup=contacts_keyboard(),
            )
        case Btn.STACK:
            await update.message.reply_text(texts.STACK, parse_mode="MarkdownV2")
        case _:
            await update.message.reply_text(
                "Використовуйте кнопки меню нижче:",
                reply_markup=main_keyboard(),
            )
