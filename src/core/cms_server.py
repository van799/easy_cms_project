from starlette.responses import FileResponse

from src.core.cms_page import CmsPage


class CmsServer:
    async def get_page(self, endpoint: str) -> CmsPage:
        clear_endpoint = CmsServer.delete_prefix(endpoint)
        if CmsServer.is_str_none_or_blank(clear_endpoint):
            return await self.get_index_page()
        return await self.get_error_page()

    async def get_index_page(self) -> CmsPage:
        content = CmsServer.read_page_content('static/index.html')
        cms_page = CmsPage('0', 'index', content)
        return cms_page

    async def get_error_page(self) -> CmsPage:
        content = CmsServer.read_page_content('static/error.html')
        cms_page = CmsPage('0', 'error', content)
        return cms_page

    @staticmethod
    def read_page_content(file_name: str):
        with open(file_name) as f:
            lines = f.readlines()
        return ''.join(lines)

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
