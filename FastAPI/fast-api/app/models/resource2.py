from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from .base import ORMBase

class Resource2ORM(ORMBase):
    __tablename__ = "resource2"

    id: Mapped[int] = mapped_column(primary_key=True)
    attr: Mapped[int] = mapped_column()

async def create(session: AsyncSession, attr: int) -> Resource2ORM:
    stmt = insert(Resource2ORM).values(attr=attr).returning(Resource2ORM)
    res = await session.execute(stmt)
    return res.scalar()

async def get(session: AsyncSession, id: int) -> Resource2ORM:
    stmt = select(Resource2ORM).where(Resource2ORM.id==id)
    res = await session.execute(stmt)
    return res.scalar()
