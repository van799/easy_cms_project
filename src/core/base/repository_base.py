from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from src.core.base.irepository import IRepository, T


class RepositoryBase(IRepository):
    def __init__(self, session: AsyncSession, model: Type[T]):
        self._session = session
        self._model = model

    async def add(self, item: Type[T]) -> None:
        self._session.add(item)
        await self._session.commit()

    async def get(self, id: str) -> Type[T]:
        statement = select(self._model).filter(self._model.id == id)
        results = await self._session.execute(statement=statement)
        return results.scalar_one_or_none()

    async def get_all(self) -> list[Type[T]]:
        statement = select(self._model)
        results = await self._session.execute(statement=statement)
        return results.scalars().all()

    # удалить id, берем его из item
    async def update(self, id: str, item: Type[T]) -> None:
        values = dict(filter(lambda x: not x[0].startswith('_'), item.__dict__.items()))
        statement = update(self._model).filter(self._model.id == id).values(values)
        await self._session.execute(statement=statement)
        await self._session.commit()

    async def delete(self, id: str) -> None:
        statement = update(self._model).filter(self._model.id == id).values(deleted=True)
        await self._session.execute(statement=statement)
        await self._session.commit()