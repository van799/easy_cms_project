import unittest

from core.cms_server import CmsServer


class TestRepositoryBase(unittest.IsolatedAsyncioTestCase):

    def test_is_str_none_or_blank(self):
        self.assertTrue(CmsServer.is_str_none_or_blank(''))
        self.assertTrue(CmsServer.is_str_none_or_blank('    '))
        self.assertTrue(CmsServer.is_str_none_or_blank(1))
        self.assertTrue(CmsServer.is_str_none_or_blank(None))
        self.assertFalse(CmsServer.is_str_none_or_blank('endpoint'))

    async def test_get_page_error(self):
        cms_server = CmsServer()
        result = await cms_server.get_page('hello', 'param')
        self.assertEqual(result.page_name, 'error')

    async def test_get_page_index(self):
        cms_server = CmsServer()
        result = await cms_server.get_page('', 'param')
        self.assertEqual(result.page_name, 'index')
