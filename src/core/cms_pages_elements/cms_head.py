from core.cms_page_base import CmsPageBase


class CmsHead(CmsPageBase):
    def __init__(self, title: str, id: str, page_name: str, content: str):
        super().__init__(id, page_name, content)
        self.title = title


