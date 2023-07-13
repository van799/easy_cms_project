import os
import os.path
import time

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from src.db.db import Base


class TestDatabase:
    def __init__(self):
        self.path = f'test_sql_app_{hash(time.time())}.db'
        self.SQLALCHEMY_DATABASE_URL = f"sqlite+aiosqlite:///./{self.path}"
        self.test_engine = create_async_engine(
            self.SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
        )

    async def create_session(self):
        await self.metadate_create_all()
        return AsyncSession(self.test_engine)

    async def metadate_create_all(self):
        async with self.test_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    def dispose(self):
        self.remove_database_file()

    def remove_database_file(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def get_engine(self):
        return self.test_engine
