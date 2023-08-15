class CmsPageBody:
    def __init__(self):
        self.content = []

    def add(self, cms_object) -> None:
        self.content.append(cms_object)

    def render(self) -> str:
        render_output = ""
        for o in self.content:
            render_output += o.render()

        return f"<body>{render_output}</body>"
