import uuid
from datetime import datetime, timezone
from typing import List

from app.models.record import Record
from app.repositories.record_repository import RecordRepository
from app.schemas.record import RecordCreate


class RecordService:
    def __init__(self, repository: RecordRepository) -> None:
        self._repository = repository

    def create_record(self, data: RecordCreate) -> Record:
        if not data.model_name.strip() or not data.title.strip():
            raise ValueError("model and title are required")

        now = datetime.now(timezone.utc)

        record = Record(
            id=str(uuid.uuid4()),
            model_name=data.model_name,
            title=data.title,
            json_data=data.json_data,
            markdown_data=data.markdown_data,
            created=now,
            updated=now,
        )

        return self._repository.create_record(record)

    def get_record(self, record_id: str) -> Record | None:
        return self._repository.get_record_by_id(record_id)

    def list_records(self) -> List[Record]:
        return self._repository.list_records()