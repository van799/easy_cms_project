import os

from jinja2 import FileSystemLoader, Environment

from src.core.cms_page import CmsPage


class CmsServer:
    async def get_page(self, endpoint: str) -> CmsPage:
        clear_endpoint = CmsServer.delete_prefix(endpoint)
        if CmsServer.is_str_none_or_blank(clear_endpoint):
            return await self.get_index_page()
        return await self.get_error_page()

    async def get_index_page(self) -> CmsPage:
        content = CmsServer.read_page_content('static/templates/test_index.html')
        cms_page = CmsPage('Тайтл главной тсранице', 'index', 'header', '0', 'index_test', content)
        return cms_page

    async def get_error_page(self) -> CmsPage:
        content = CmsServer.read_page_content('static/error.html')
        cms_page = CmsPage('0', 'error', content)
        return cms_page

    @staticmethod
    def read_page_content(file_name: str):
        path = os.path.join(os.path.dirname(__file__), '../static/templates')
        file_loader = FileSystemLoader(searchpath=path)
        env = Environment(loader=file_loader)

        template = env.get_template('test_index.html')
        msg = template.render(title='тайтл лучшего сайта на свете', content='саммый лучший CMS на свете')
        return msg

    @staticmethod
    def delete_prefix(endpoint: str):
        return endpoint.removeprefix('/')

    @staticmethod
    def is_str_none_or_blank(endpoint: str):
        if endpoint is None:
            return True
        if type(endpoint) is not str:
            return True
        if endpoint.strip() == '':
            return True
        return False