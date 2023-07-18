from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from core.user_authenticator import UserAuthenticator
from db.db import Database
from schemas.entity import CmsUserRegistration, RequestMessage

database = Database()
router = APIRouter()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/register",
             response_model=RequestMessage,
             status_code=status.HTTP_201_CREATED,
             description='Регистрация пользователя')
async def register(*,
                   session: AsyncSession = Depends(database.get_session),
                   request: CmsUserRegistration
                   ) -> Any:

    user_authenticate = UserAuthenticator(session)

    if await user_authenticate.register_user(request.username, request.password):
        return RequestMessage(message='Пользователь успешно зарегистрировался')
    return RequestMessage(message='Такой пользователь уже существует')
