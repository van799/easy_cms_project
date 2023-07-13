import unittest

from sqlalchemy import select, insert, Select

from src.tests.common.common_test_base_init import TestDatabase
from src.tests.common.models import TestCommon
from src.tests.common.test_repository import TestRepository


class TestRepositoryBase(unittest.IsolatedAsyncioTestCase):

    async def test_repository_add(self):
        test_database = TestDatabase()
        test_common = TestCommon()
        test_common.test_str = 'test'

        async with await test_database.create_session() as session:
            repository = TestRepository(session)
            await repository.add(test_common)

        async with test_database.get_engine().begin() as conn:
            await repository.add(test_common)
            result = [row for row in await conn.execute(select(TestCommon))]

        test_database.dispose()
        self.assertEqual(result[0][0], test_common.test_str)



