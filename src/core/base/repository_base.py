from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from src.core.base.irepository import IRepository, T


class RepositoryBase(IRepository):
    def __init__(self, session: AsyncSession, model: Type[T]):
        self.__session = session
        self.__model = model

    async def add(self, item) -> None:
        self.__session.add(item)
        await self.__session.commit()

    async def get(self, id: str) -> Type[T]:
        statement = select(self.__model).where(self.__model.id == id)
        results = await self.__session.execute(statement=statement)
        return results.scalar_one_or_none()

    async def get_all(self) -> list[Type[T]]:
        statement = select(self.__model)
        results = await self.__session.execute(statement=statement)
        return results.scalars().all()

    async def update(self, id: str, item: Type[T]) -> None:
        statement = update(self.__model).where(self.__model.id == id)
        await self.__session.execute(statement=statement)

    async def delete(self, id: str) -> None:
        raise NotImplementedError
