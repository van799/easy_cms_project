from abc import ABC
from typing import TypeVar, Generic, Type

T = TypeVar("T")


class IRepository(ABC, Generic[T]):
    def add(self, item: Type[T]) -> None:
        raise NotImplementedError

    def get(self, id: str) -> Type[T]:
        raise NotImplementedError

    def get_all(self, id: str) -> list[Type[T]]:
        raise NotImplementedError

    def update(self, id: str, item: Type[T]) -> None:
        raise NotImplementedError

    def delete(self, id: str) -> None:
        raise NotImplementedError
