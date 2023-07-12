from typing import Type

from src.core.base.irepository import IRepository, T


class RepositoryBase(IRepository):
    def __init__(self, session: AsyncSession, model: Type[T]):
        self.__session = session
        self.__model = model

    def add(self, id: str) -> None:
        db.add(self.__model)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    def get(self, id: str) -> Type[T]:
        statement = select(self.__model).where(self.__model.id == id)
        results = await self.__session.execute(statement=statement)
        return results.scalar_one_or_none()

    def get_all(self, id: str) -> list[Type[T]]:
        raise NotImplementedError

    def update(self, id: str, item: Type[T]) -> None:
        raise NotImplementedError

    def delete(self, id: str) -> None:
        raise NotImplementedError
