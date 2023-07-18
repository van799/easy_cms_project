from pydantic import BaseModel


class RequestMessage(BaseModel):
    massage: str


class CmsUserRegistration(BaseModel):
    username: str
    password: str
