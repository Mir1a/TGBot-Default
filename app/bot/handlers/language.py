from telegram import Update
from telegram.ext import ContextTypes

from app.bot.keyboards import get_main_keyboard
from app.bot.texts import get_text
from app.db import set_user_language


async def handle_language_selection(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if not query or not query.data:
        return

    await query.answer()

    lang = query.data.replace("lang_", "")  # "lang_uk" -> "uk", "lang_en" -> "en"
    user_id = query.from_user.id

    await set_user_language(user_id, lang)
    await query.edit_message_reply_markup(reply_markup=None)
    await query.message.reply_text(
        get_text(lang, "welcome"),
        parse_mode="MarkdownV2",
        reply_markup=get_main_keyboard(lang),
    )
