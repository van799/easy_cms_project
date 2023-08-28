from yattag import Doc, indent

from core.cms_components.cms_hyperlink import CmsHyperlink
from core.cms_components.cms_images import CmsImages
from core.cms_components.cms_page_container import CmsPageContainer
from core.cms_components.cms_page_header import CmsHeading
from core.cms_header import CmsPageHeader


class CmsPage:
    def __init__(self, id: str, page_name: str, content: str):
        self._id = id
        self._page_name = page_name
        self._content = content
        self._elements = []

    @property
    def id(self) -> str:
        return self._id

    @property
    def page_name(self) -> str:
        return self._page_name

    @property
    def content(self) -> str:
        return self._content

    def add(self, element):
        self._elements.append(element)

    def render(self) -> str:
        doc, tag, text = Doc().tagtext()
        doc.asis('<!DOCTYPE html>')
        doc.stag('meta', charset='utf-8')

        with tag('head'):
            with tag('title'):
                text(f'{self.page_name}')
        doc.asis(self._render_body())
        result = indent(
            doc.getvalue(),
            indentation='    ',
            newline='\r\n',
            indent_text=True
        )

        return result

    def _render_body(self):
        doc, tag, text = Doc().tagtext()
        with tag('body'):
            for element in self._elements:
                doc.asis(element.render())
        return doc.getvalue()


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

print(cms_page.render())
