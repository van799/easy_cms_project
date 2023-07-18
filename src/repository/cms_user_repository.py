from typing import Type

from sqlalchemy import select

from core.base.irepository import T
from core.base.repository_base import RepositoryBase
from db.models import CmsUsers


class CmsUserRepository(RepositoryBase):
    def __init__(self, engine):
        super().__init__(engine, CmsUsers)

    async def get_by_name(self, name: str) -> Type[T]:
        statement = select(self.__model).filter(self.__model.name == name)
        results = await self.__session.execute(statement=statement)
        return results.scalar_one_or_none()
