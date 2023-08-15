from core.cms_page_base import CmsPageBase


class CmsPage(CmsPageBase):
    def __init__(self,
                 title: str,
                 body: str,
                 footer: str,
                 header: str,
                 id: str,
                 page_name: str,
                 content: str):
        super().__init__(id, page_name, content)
        self.title = title
        self.header = header
        self.body = body
        self.footer = footer
