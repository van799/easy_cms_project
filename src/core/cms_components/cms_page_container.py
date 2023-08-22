from yattag import Doc


class CmsPageContainer:
    def __init__(self, id, css_class):
        self.css_class = css_class
        self.id = id
        self.elements = []

    def add(self, element):
        self.elements.append(element)
        return self

    def render(self):
        doc, tag, text, line = Doc().ttl()

        with tag('div', id=self.id, klass=self.css_class):
            for element in self.elements:
                doc.asis(element.render())
        return doc.getvalue()

    @staticmethod
    def create(id, css_class):
        cms_page_container = CmsPageContainer(id, css_class)
        return cms_page_container
