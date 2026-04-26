from sqlalchemy import select

from app.db.models import User
from app.db.session import AsyncSessionLocal


async def get_user_language(telegram_id: int) -> str | None:
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar_one_or_none()
        return user.language if user else None


async def set_user_language(telegram_id: int, language: str) -> None:
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar_one_or_none()
        if user:
            user.language = language
        else:
            session.add(User(telegram_id=telegram_id, language=language))
        await session.commit()
