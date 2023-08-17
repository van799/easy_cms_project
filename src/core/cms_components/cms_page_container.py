from yattag import Doc, indent



class CmsPageContainer:
    def __init__(self, div_id, div_class, tags):
        self.css_class = div_class
        self.div_id = div_id
        self.tags = tags

    def render(self):
        doc, tag, text, line = Doc().ttl()

        with tag('div', id=self.div_id):
            doc.asis(self.tags)
        return doc.getvalue()


# cms_page = CmsPage('0', 'Главная страница', '0')
#
# cms_page.add(CmsPageHeader('Заголовок сайта', 1))

cms_page_container = CmsPageContainer(1,
                                   'Красивый заголовок',
                                   'ada')


print(cms_page_container.render())


#
# cms_page = CmsPage('0', 'Главная страница', '0')
#
# cms_page.add(CmsPageHeader('Заголовок сайта', 1))
# cms_page.add(CmsPageHeader('Заголовок сайта', 2))
# cms_page.add(CmsPageHeader('Заголовок сайта', 3))
# cms_page.add(CmsPageHeader('Заголовок сайта', 4))


# print(cms_page.render())
