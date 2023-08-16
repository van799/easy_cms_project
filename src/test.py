from yattag import Doc, indent

doc, tag, text = Doc().tagtext()

# рекомендуется в начале задавать тип документа
# doc.asis('<!DOCTYPE html>')
#
# with tag('html'):
#     with tag('head'):
#         doc.stag('link', rel='stylesheet', href='bootstrap.css')
#         # принцип создания тегов
#         with tag('body'):
#             with tag('title'):
#                 text('My firs Yattag page!')
#             doc.stag('link', rel='stylesheet', href='')
#         with tag('body'):
#             with tag('h1'):
#                 text('Hello world!')


doc.asis('<!DOCTYPE html>')
doc.stag('meta', charset='utf-8')

with tag('html'):
    with tag('head'):
        doc.stag('link', rel='stylesheet', href='bootstrap.min.css')
        # принцип создания тегов
        with tag('title'):
            text('My firs Yattag page!')
            doc.stag('link', rel='stylesheet', href='')
        with tag('body'):
            with tag('header'):
                with tag('nav', klass="navbar navbar-light", style='background-color: lightskyblue'):
                    with tag('div', id='container'):
                        with tag('a', id='navbar-brand'):
                            with tag('span', id='font-style: italic; color: red; font-size: 40px; blockquote'):
                                text('Текст')
# сгенерировать html код с отступами
result = indent(
    doc.getvalue(),
    indentation='    ',
    newline='\r\n',
    indent_text=True
)
print(result)

import asyncio
import uvicorn


async def app(scope, receive, send):
    """
    Echo the method and path back in an HTTP response.
    """
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/html'],
        ]
    })
    await send({
        'type': 'http.response.body',
        'body': doc.getvalue().encode('utf-8'),
    })


"""Запуск сервера"""


async def main():
    config = uvicorn.Config("test:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
