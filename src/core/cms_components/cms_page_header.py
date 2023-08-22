from yattag import Doc, indent


class CmsPageHeader:
    def __init__(self, text: str, size: int):
        self.text = text
        self.size = size

    def render(self):
        doc, tag, text, line = Doc().ttl()

        if self.size == 1:
            line('h1', self.text)
        elif self.size == 2:
            line('h2', self.text)
        elif self.size == 3:
            line('h3', self.text)
        elif self.size == 4:
            line('h4', self.text)
        elif self.size == 5:
            line('h5', self.text)
        elif self.size == 6:
            line('h6', self.text)
        else:
            raise Exception('The wrong text size is indicated')
        return doc.getvalue()