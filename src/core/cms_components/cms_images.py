from yattag import Doc


class CmsImages:
    def __init__(self, url_image: str, image_class: str):
        self.url_image = url_image
        self.image_class = image_class

    def render(self):
        doc, tag, text, line = Doc().ttl()
        doc.stag('img', src=self.url_image, klass=self.image_class)
        return doc.getvalue()


# image = CmsImages('pic.img', 'cool_pic')
# print(image.render())