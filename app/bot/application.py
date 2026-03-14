from telegram.ext import Application, CommandHandler, MessageHandler, filters

from app.bot.handlers.message import handle_message
from app.bot.handlers.start import start
from app.config import settings


def create_application() -> Application:
    app = Application.builder().token(settings.TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    return app


application = create_application()
