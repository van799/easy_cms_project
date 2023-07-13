from src.core.base.repository_base import RepositoryBase
from src.tests.common.models import TestCommon


class TestRepository(RepositoryBase):
    """Класс репозитория для сохранения Test в БД."""

    def __init__(self, engine):
        super().__init__(engine, TestCommon)
