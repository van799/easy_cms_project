class CmsPage:
    def __init__(self, id: str, page_name: str, content: str):
        self._id = id
        self._page_name = page_name
        self._content = content

    @property
    def id(self) -> str:
        return self._id

    @property
    def page_name(self) -> str:
        return self._page_name

    @property
    def content(self) -> str:
        return self._content
