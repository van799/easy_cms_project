import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1.api import router
from config.app_settings import app_settings


app = FastAPI(
    title=app_settings.project_name,
    default_response_class=ORJSONResponse,
)

app.include_router(router, prefix='/api/v1')

"""Запуск сервера"""
if __name__ == "__main__":
    uvicorn.run(app,
                host=app_settings.project_host,
                port=app_settings.project_port,
                )

# сделать 1 эндпоинт, который вызывает cms сервер и выдает нужную страницу