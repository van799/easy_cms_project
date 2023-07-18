from typing import Type

from sqlalchemy import select

from core.base.irepository import T
from core.base.repository_base import RepositoryBase
from db.models import CmsUsers


class CmsUserRepository(RepositoryBase):
    def __init__(self, engine):
        super().__init__(engine, CmsUsers)

    async def get_by_username(self, username: str) -> Type[T]:
        statement = select(self._model).filter(self._model.username == username)
        results = await self._session.execute(statement=statement)
        return results.scalar_one_or_none()
