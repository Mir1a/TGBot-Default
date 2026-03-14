from fastapi import APIRouter, Request

from app.api.service import process_update
from app.bot.application import application

router = APIRouter()


@router.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    await process_update(data, application)
    return {"ok": True}


@router.get("/health")
async def health():
    return {"status": "ok"}
