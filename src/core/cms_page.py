from yattag import Doc, indent

from core.cms_components.cms_page_header import CmsPageHeader


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

        with tag('header'):
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

    def _render_header(self) -> str:
        return f"<head>{self._render_header_body()}</head>"

    def _render_header_body(self) -> str:
        return ""


cms_page = CmsPage('0', 'Главная страница', '0')

cms_page.add(CmsPageHeader('Заголовок сайта', 1))
cms_page.add(CmsPageHeader('Заголовок сайта', 2))
cms_page.add(CmsPageHeader('Заголовок сайта', 3))
cms_page.add(CmsPageHeader('Заголовок сайта', 4))

print(cms_page.render())


# doc, tag, text = Doc().tagtext()
# doc.asis('<!DOCTYPE html>')
# doc.stag('meta', charset='utf-8')
#
# with tag('html'):
#     with tag('head'):
#         doc.stag('link', rel='stylesheet', href='bootstrap.min.css')
#         # принцип создания тегов
#         with tag('title'):
#             text('My firs Yattag page!')
#             doc.stag('link', rel='stylesheet', href='')
#         with tag('body'):
#             with tag('header'):
#                 with tag('nav', klass="navbar navbar-light", style='background-color: lightskyblue'):
#                     with tag('div', id='container'):
#                         with tag('a', id='navbar-brand'):
#                             with tag('span', id='font-style: italic; color: red; font-size: 40px; blockquote'):
#                                 text('Текст')
# # сгенерировать html код с отступами
# result = indent(
#     doc.getvalue(),
#     indentation='    ',
#     newline='\r\n',
#     indent_text=True
# )


# class CmsPageBody:
#     def __init__(self):
#         self.Content = []
#
#     def Add(self, cms_object) -> None:
#         self.Content.append(cms_object)
#
#     def render(self) -> str:
#         render_output = ""
#         for o in self.Content:
#             render_output += o.render()
#
#         return f"<body>{render_output}</body>"
#
#
# class CmsText:
#     def __init__(self, text: str):
#         self.text = text
#
#     def render(self) -> str:
#         return self.text
#
#
# cms_page = CmsPage()
#
# cms_page.cms_body.Add(CmsText("hello world!"))
#
# print(cms_page.render())
