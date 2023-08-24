from yattag import Doc


class CmsHyperlink:
    def __init__(self, url_hyperlink: str, hyperlink_class: str, description_hyperlink: str, target='_parent'):
        self.url_image = url_hyperlink
        self.hyperlink_class = hyperlink_class
        self.description_hyperlink = description_hyperlink
        self.target = target

    def render(self):
        doc, tag, text, line = Doc().ttl()
        with tag('a'):
            doc.attr(klass=self.hyperlink_class, target=self.target, href=self.url_image)
            text(self.description_hyperlink)
        return doc.getvalue()
