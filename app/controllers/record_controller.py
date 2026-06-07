# pyright: reportUnusedFunction=false
from fastapi import APIRouter, HTTPException

from app.models.record import Record
from app.schemas.record import RecordCreate, RecordResponse
from app.services.record_service import RecordService


def build_router(service: RecordService) -> APIRouter:
    router = APIRouter(prefix="/model", tags=["model"])

    def to_response(record: Record) -> RecordResponse:
        return RecordResponse(
            id=record.id,
            model_name=record.model_name,
            title=record.title,
            json_data=record.json_data,
            markdown_data=record.markdown_data,
            created=record.created,
            updated=record.updated,
        )

    @router.post("", response_model=RecordResponse)
    def create_record(payload: RecordCreate) -> RecordResponse:
        try:
            record = service.create_record(payload)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        return to_response(record)

    @router.get("/{record_id}", response_model=RecordResponse)
    def get_record(record_id: str) -> RecordResponse:
        record = service.get_record(record_id)
        if record is None:
            raise HTTPException(status_code=404, detail="Record not found")
        return to_response(record)

    @router.get("", response_model=list[RecordResponse])
    def list_records() -> list[RecordResponse]:
        return [to_response(r) for r in service.list_records()]

    return router