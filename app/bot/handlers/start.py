from telegram import Update
from telegram.ext import ContextTypes

from app.bot import texts
from app.bot.keyboards import main_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        return
    await update.message.reply_text(
        texts.WELCOME,
        parse_mode="MarkdownV2",
        reply_markup=main_keyboard(),
    )
