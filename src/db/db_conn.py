from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel import create_engine, text

from config import settings

engine = AsyncEngine(create_engine(settings.DATABASE_URL, echo=True))


async def init_db():
    async with engine.begin() as conn:
        await conn.execute(text("SELECT 'HELLO';"))
