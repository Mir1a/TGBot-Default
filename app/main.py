import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import router
from app.bot.application import application
from app.config import settings
from app.db.session import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    await application.initialize()
    await application.start()
    

    bot_info = await application.bot.get_me()
    logger.info("Bot connected: @%s (id=%d)", bot_info.username, bot_info.id)

    if settings.WEBHOOK_URL:
        await application.bot.set_webhook(settings.WEBHOOK_URL)
        logger.info("Webhook set: %s", settings.WEBHOOK_URL)
    else:
        logger.warning("WEBHOOK_URL not set — bot will not receive updates")

    yield

    await application.stop()
    await application.shutdown()


app = FastAPI(lifespan=lifespan)
app.include_router(router)
