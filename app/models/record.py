from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class Record:
    id: str
    model_name: str
    title: str
    json_data: dict[str, Any] | None
    markdown_data: str | None
    created: datetime
    updated: datetime