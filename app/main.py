from fastapi import FastAPI

from app.controllers.record_controller import build_router
from app.repositories.record_repository import RecordRepository
from app.services.record_service import RecordService
from app.core.settings import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name)

    repository = RecordRepository()
    service = RecordService(repository)

    app.include_router(build_router(service))

    return app


app = create_app()