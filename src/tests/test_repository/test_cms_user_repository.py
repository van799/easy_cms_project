import unittest

from sqlalchemy import select, insert

from db.models import CmsUsers
from repository.cms_user_repository import CmsUserRepository
from src.tests.common.common_test_base_init import TestDatabase


class TestRepositoryBase(unittest.IsolatedAsyncioTestCase):

    async def test_base_repository_get_by_username(self):
        test_database = TestDatabase()

        values_dict = [{'id': 1, 'username': 'test_user_1', 'password': 'test_password_1'},
                       {'id': 2, 'username': 'test_user_2', 'password': 'test_password_2'},
                       {'id': 3, 'username': 'test_user_3', 'password': 'test_password_3'}]

        await test_database.create_session()

        async with test_database.get_engine().begin() as conn:
            await conn.execute(insert(CmsUsers).values(values_dict))
            await conn.commit()

        async with await test_database.create_session() as session:
            cms_user_repository = CmsUserRepository(session)
            result = await cms_user_repository.get_by_username('test_user_2')

        test_database.dispose()
        self.assertEqual(result.username, 'test_user_2')
