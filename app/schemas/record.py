from datetime import datetime
from typing import Any
from pydantic import BaseModel


class RecordBase(BaseModel):
    model_name: str
    title: str
    json_data: dict[str, Any] | None = None
    markdown_data: str | None = None


class RecordCreate(RecordBase):
    pass


class RecordResponse(RecordBase):
    id: str
    created: datetime
    updated: datetime