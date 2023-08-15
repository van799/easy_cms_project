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
from main import app
from schemas.entity import CmsUserRegistration, RequestMessage

database = Database()
# router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/",
         status_code=status.HTTP_201_CREATED,
         description='Тестовый endpoint')
async def index(*,
                request: Request,
                param=None) -> Any:
    cms_server = CmsServer()
    result_server = await cms_server.get_page(request.url.path, param)
    return FileResponse(result_server.content)


@app.get("/error",
         status_code=status.HTTP_201_CREATED,
         description='Тестовый endpoint')
async def error(*,
                request: Request,
                param='Error') -> Any:
    cms_server = CmsServer()
    result_server = await cms_server.get_page(request.url.path, param)
    return FileResponse(result_server.content)

# @router.post("/register",
#              response_model=RequestMessage,
#              status_code=status.HTTP_201_CREATED,
#              description='Регистрация пользователя')
# async def register(*,
#                    session: AsyncSession = Depends(database.get_session),
#                    request: CmsUserRegistration
#                    ) -> Any:
#
#     user_authenticate = UserAuthenticator(session)
#
#     if await user_authenticate.register_user(request.username, request.password):
#         return RequestMessage(message='Пользователь успешно зарегистрировался')
#     return RequestMessage(message='Такой пользователь уже существует')
