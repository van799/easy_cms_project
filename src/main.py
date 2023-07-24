import asyncio

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

# from api.v1.api import router
from config.app_settings import app_settings

from typing import Any
from fastapi import Request, Query, FastAPI
from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
# from main import app
from core.cms_server import CmsServer
# from core.user_authenticator import UserAuthenticator
from db.db import Database
# from main import app
from schemas.entity import CmsUserRegistration, RequestMessage


# app = FastAPI(
#     title=app_settings.project_name,
#     default_response_class=ORJSONResponse,
# )
#
# router = APIRouter()
#
#
# @router.get("/",
#             status_code=status.HTTP_201_CREATED,
#             description='Тестовый endpoint')
# async def index(*,
#                 request: Request,
#                 param=None) -> Any:
#     cms_server = CmsServer()
#     result_server = await cms_server.get_page(request.url.path, param)
#     return FileResponse(result_server.content)


async def app(scope, receive, send):
    """
    Echo the method and path back in an HTTP response.
    """
    assert scope['type'] == 'http'

    body = f'Received {scope["method"]} request to {scope["path"]}'
    param = 'test'
    cms_server = CmsServer()
    result_server = await cms_server.get_page(scope["path"], param)

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



# app.include_router(router, prefix='/api/v1')

"""Запуск сервера"""


async def main():
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
