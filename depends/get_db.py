from database.session import SessionLocal

async def get_db():
    try:
        db = SessionLocal()

        async with db as session:
            yield session
    except:
        await session.rollback()
        raise
    finally:
        await session.close()