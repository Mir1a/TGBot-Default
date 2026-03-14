from telegram import Update
from telegram.ext import Application


async def process_update(data: dict, application: Application) -> None:
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
