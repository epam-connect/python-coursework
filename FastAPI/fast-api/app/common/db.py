from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.common.settings import settings


ENGINE = create_async_engine(settings.DB_URL)

session_maker = async_sessionmaker(bind=ENGINE)

async def get_session():
    session = session_maker()
    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise 
    finally:
        await session.close()

