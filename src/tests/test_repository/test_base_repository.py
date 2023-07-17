import unittest

from sqlalchemy import select, insert
from src.tests.common.common_test_base_init import TestDatabase
from src.tests.common.models import TestCommon
from src.tests.common.test_repository import TestRepository


class TestRepositoryBase(unittest.IsolatedAsyncioTestCase):

    async def test_base_repository_add(self):
        test_database = TestDatabase()
        test_common = TestCommon()
        test_common.id = '1'
        test_common.test_str = 'test'

        async with await test_database.create_session() as session:
            repository = TestRepository(session)
            await repository.add(test_common)

        async with test_database.get_engine().begin() as conn:
            result = [row for row in await conn.execute(select(TestCommon))]

        test_database.dispose()
        self.assertEqual(result[0][2], 'test')

    async def test_base_repository_get_all(self):
        test_database = TestDatabase()

        values_dict = [{'id': 1, 'test_str': 'test1'},
                       {'id': 2, 'test_str': 'test2'},
                       {'id': 3, 'test_str': 'test3'}]

        await test_database.create_session()

        async with test_database.get_engine().begin() as conn:
            await conn.execute(insert(TestCommon).values(values_dict))
            await conn.commit()

        async with await test_database.create_session() as session:
            repository = TestRepository(session)
            result = await repository.get_all()

        test_database.dispose()
        self.assertEqual(result[0].id, '1')
        self.assertEqual(result[1].id, '2')
        self.assertEqual(result[2].id, '3')

    async def test_base_repository_get_id(self):
        test_database = TestDatabase()

        values_dict = [{'id': 1, 'test_str': 'test1'},
                       {'id': 2, 'test_str': 'test2'},
                       {'id': 3, 'test_str': 'test3'}]

        await test_database.create_session()

        async with test_database.get_engine().begin() as conn:
            await conn.execute(insert(TestCommon).values(values_dict))
            await conn.commit()

        async with await test_database.create_session() as session:
            repository = TestRepository(session)
            result = await repository.get('1')

        test_database.dispose()
        self.assertEqual(result.test_str, 'test1')

    async def test_base_repository_update(self):
        test_database = TestDatabase()
        test_common = TestCommon()

        values_dict = [{'id': 1, 'test_str': 'test1'},
                       {'id': 2, 'test_str': 'test2'},
                       {'id': 3, 'test_str': 'test3'}]

        await test_database.create_session()

        async with test_database.get_engine().begin() as conn:
            await conn.execute(insert(TestCommon).values(values_dict))
            await conn.commit()

        async with await test_database.create_session() as session:
            repository = TestRepository(session)
            test_common.test_str = 'test update'
            await repository.update('1', test_common)

        async with await test_database.create_session() as session:
            repository = TestRepository(session)
            result = await repository.get('1')

        test_database.dispose()
        self.assertEqual(result.test_str, 'test update')

    async def test_base_repository_deleted(self):
        test_database = TestDatabase()

        values_dict = [{'id': '1', 'deleted': False, 'test_str': 'test1'},
                       {'id': '2', 'deleted': False, 'test_str': 'test2'},
                       {'id': '3', 'deleted': False, 'test_str': 'test3'}]

        await test_database.create_session()

        async with test_database.get_engine().begin() as conn:
            await conn.execute(insert(TestCommon).values(values_dict))
            await conn.commit()

        async with await test_database.create_session() as session:
            repository = TestRepository(session)
            await repository.delete('1')

        async with await test_database.create_session() as session:
            repository = TestRepository(session)
            result = await repository.get_all()

        test_database.dispose()
        self.assertEqual(result[0].deleted, True)
