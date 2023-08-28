from starlette.responses import FileResponse

from core.cms_components.cms_hyperlink import CmsHyperlink
from core.cms_components.cms_images import CmsImages
from core.cms_components.cms_page_container import CmsPageContainer
from core.cms_components.cms_page_header import CmsHeading
from core.cms_header import CmsPageHeader
from src.core.cms_page import CmsPage


class CmsServer:
    async def get_page(self, endpoint: str) -> CmsPage:
        clear_endpoint = CmsServer.delete_prefix(endpoint)
        if CmsServer.is_str_none_or_blank(clear_endpoint):
            return await self.get_generator_page()
        return await self.get_error_page()

    async def get_index_page(self) -> CmsPage:
        content = CmsServer.read_page_content('static/index.html')
        cms_page = CmsPage('0', 'index', content)
        return cms_page

    async def get_error_page(self) -> CmsPage:
        content = CmsServer.read_page_content('static/error.html')
        cms_page = CmsPage('0', 'error', content)
        return cms_page

    async def get_generator_page(self) -> CmsPage:
        cms_page = CmsPage('0', 'Главная страница', '0')
        navig_bar = {
            'url_hyperlink1': 'описание1',
            'url_hyperlink2': 'описание2',
            'url_hyperlink3': 'описание3',
        }

        cms_header = CmsPageHeader('id', 'ссылка на лого', 'описание меню сайта', navig_bar, 'класс_хеадера')

        cms_header.render()
        cms_page.add(cms_header)
        cms_page.add(CmsPageContainer.create(1, 'green_text').
                     add(CmsHeading('Заголовок сайта1', 1)).
                     add(CmsHeading('Заголовок сайта2', 1)).
                     add(CmsImages('pic.img', 'cool_pic')).
                     add(CmsHyperlink('yandex.ru', 'cool_link', 'cool_link'))
                     )

        content = cms_page.render()
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
