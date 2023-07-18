from starlette.responses import FileResponse

from src.core.cms_page import CmsPage


class CmsServer:
    async def get_page(self, endpoint: str, params: str) -> CmsPage:
        if CmsServer.is_str_none_or_blank(endpoint):
            return await self.get_index_page()
        return await self.get_error_page()

    async def get_index_page(self) -> CmsPage:
        cms_page = CmsPage('0', 'index', 'static/index.html')
        return cms_page

    async def get_error_page(self) -> CmsPage:
        cms_page = CmsPage('0', 'error', 'static/error.html')
        return cms_page

    @staticmethod
    def is_str_none_or_blank(endpoint: str):
        if endpoint is None:
            return True
        if type(endpoint) is not str:
            return True
        if endpoint.strip() == '':
            return True
        return False

