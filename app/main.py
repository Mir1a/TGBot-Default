from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import router
from app.bot.application import application
from app.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    await application.initialize()
    await application.start()

    if settings.WEBHOOK_URL:
        await application.bot.set_webhook(settings.WEBHOOK_URL)

    yield

    await application.stop()
    await application.shutdown()


app = FastAPI(lifespan=lifespan)
app.include_router(router)
