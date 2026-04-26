from telegram import Update
from telegram.ext import ContextTypes

from app.bot.keyboards import get_language_keyboard, get_main_keyboard
from app.bot.texts import get_text
from app.db import get_user_language


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        return

    user_id = update.message.from_user.id
    lang = await get_user_language(user_id)

    if lang:
        await update.message.reply_text(
            get_text(lang, "welcome"),
            parse_mode="MarkdownV2",
            reply_markup=get_main_keyboard(lang),
        )
    else:
        await update.message.reply_text(
            "👋 Вітаю\\! / Welcome\\!\n\nОберіть мову / Choose language:",
            parse_mode="MarkdownV2",
            reply_markup=get_language_keyboard(),
        )
