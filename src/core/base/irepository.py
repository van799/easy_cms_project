from abc import ABC
from typing import TypeVar, Generic, Type

# зависимость от CmsEntity класса базовой модели
T = TypeVar("T", bound=CmsEntity)
# ModelType = TypeVar("ModelType", bound=CmsEntity)


class IRepository(ABC, Generic[T]):
    def add(self, item: Type[T]) -> None:
        raise NotImplementedError

    def get(self, id: str) -> Type[T]:
        raise NotImplementedError

    def get_all(self) -> list[Type[T]]:
        raise NotImplementedError

    def update(self, id: str, item: Type[T]) -> None:
        raise NotImplementedError

    def delete(self, id: str) -> None:
        raise NotImplementedError
