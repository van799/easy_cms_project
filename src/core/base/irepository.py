from abc import ABC
from typing import TypeVar, Generic, Type

from db.models import CmsEntity

T = TypeVar("T", bound=CmsEntity)


class IRepository(ABC, Generic[T]):
    def add(self, item: Type[T]) -> None:
        raise NotImplementedError

    def get(self, id: str) -> Type[T]:
        raise NotImplementedError

    def get_all(self) -> list[Type[T]]:
        raise NotImplementedError

    def update(self, item: Type[T]) -> None:
        raise NotImplementedError

    def delete(self, id: str) -> None:
        raise NotImplementedError
