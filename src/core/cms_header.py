from yattag import Doc, indent

from core.cms_components.cms_hyperlink import CmsHyperlink
from core.cms_components.cms_images import CmsImages
from core.cms_components.cms_page_header import CmsHeading
from core.cms_components.cms_page_unordered_list import CmsPageUnorderedList


class CmsPageHeader:
    def __init__(self, id: str, logo: str, description: str, navigations: dict, header_class: str, size=1):
        self.id = id
        self.logo = logo
        self.description = description
        self.size = size
        self.navigations = navigations
        self.header_class = header_class
        self._elements = []
        self.page_logo()
        self.page_text()
        self.navigation_bar()

    def page_logo(self):
        cms_images = CmsImages(self.logo, self.header_class)
        self.add(cms_images)

    def page_text(self):
        cms_heading = CmsHeading(self.description, self.size)
        self.add(cms_heading)

    def navigation_bar(self):
        for url_hyperlink, description_hyperlink in self.navigations.items():
            cms_page_unordered_list = CmsPageUnorderedList(self.id, self.header_class).add(
                CmsHyperlink(url_hyperlink, self.header_class, description_hyperlink))
            self.add(cms_page_unordered_list)

    def add(self, element):
        self._elements.append(element)

    def render(self) -> str:
        doc, tag, text = Doc().tagtext()

        with tag('header'):
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
        for element in self._elements:
            doc.asis(element.render())
        return doc.getvalue()


