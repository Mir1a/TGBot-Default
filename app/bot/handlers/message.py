from telegram import Update
from telegram.ext import ContextTypes

from app.bot import BUTTONS
from app.bot.keyboards import contacts_keyboard, get_language_keyboard, get_main_keyboard
from app.bot.texts import get_text
from app.db import get_user_language


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        return

    user_id = update.message.from_user.id
    lang = await get_user_language(user_id) or "uk"
    btn = BUTTONS.get(lang, BUTTONS["uk"])
    text = update.message.text

    if text == btn["about_bot"]:
        await update.message.reply_text(get_text(lang, "about_bot"), parse_mode="MarkdownV2")
    elif text == btn["about_me"]:
        await update.message.reply_text(get_text(lang, "about_me"), parse_mode="MarkdownV2")
    elif text == btn["contacts"]:
        await update.message.reply_text(
            get_text(lang, "contacts"),
            parse_mode="MarkdownV2",
            reply_markup=contacts_keyboard(),
        )
    elif text == btn["stack"]:
        await update.message.reply_text(get_text(lang, "stack"), parse_mode="MarkdownV2")
    elif text == btn["language"]:
        await update.message.reply_text(
            "🌐 Оберіть мову / Choose language:",
            reply_markup=get_language_keyboard(),
        )
    else:
        await update.message.reply_text(
            get_text(lang, "unknown"),
            reply_markup=get_main_keyboard(lang),
        )
