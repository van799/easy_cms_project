from yattag import Doc

from core.cms_components.cms_hyperlink import CmsHyperlink


class CmsPageUnorderedList:
    def __init__(self, id, css_class):
        self.css_class = css_class
        self.id = id
        self.elements = []

    def add(self, element):
        self.elements.append(element)
        return self

    def render(self):
        doc, tag, text, line = Doc().ttl()

        with tag('ul', id=self.id, klass=self.css_class):
            for element in self.elements:
                with tag('li', id=self.id, klass=self.css_class):
                    doc.asis(element.render())
        return doc.getvalue()

    @staticmethod
    def create(id, css_class):
        cms_page_unordered_list = CmsPageUnorderedList(id, css_class)
        return cms_page_unordered_list


# cms_page_unordered_list = CmsPageUnorderedList('id_1', 'cool_ul_li') \
#     .add(CmsHyperlink('url_hyperlink1', 'hyperlink_class', 'One_link')) \
#     .add(CmsHyperlink('url_hyperlink2', 'hyperlink_class', 'Second_link'))
#
# print(cms_page_unordered_list.render())
