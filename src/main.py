import asyncio

import uvicorn

from core.cms_server import CmsServer


async def app(scope, receive, send):
    assert scope['type'] == 'http'

    cms_server = CmsServer()
    result_server = await cms_server.get_page(scope["path"])

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/html'],
        ]
    })
    await send({
        'type': 'http.response.body',
        'body': result_server.content.encode('utf-8'),
    })


"""Запуск сервера"""
async def main():
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
