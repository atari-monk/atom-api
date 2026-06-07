## Record CRUD API Implementation

### File Structure

```
app/
  main.py
  controllers/
    record_controller.py
  services/
    record_service.py
  repositories/
    record_repository.py
  models/
    record.py
  schemas/
    record.py
  core/
    settings.py
.env
```

---

### Dependencies

See [Commands](../../commands.md) to install

requirements.txt:

```
fastapi
uvicorn[standard]
pydantic
pydantic-settings
python-dotenv
```

---

### app/core/settings.py

```python
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "record-api"
    env: str = "dev"

    model_config = {"env_file": ".env"}


settings = Settings()
```

---

### app/models/record.py

```python
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
```

---

### app/schemas/record.py

```python
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
```

---

### app/repositories/record_repository.py

```python
from typing import Dict, List, Optional
from app.models.record import Record


class RecordRepository:
    def __init__(self) -> None:
        self._store: Dict[str, Record] = {}

    def create_record(self, record: Record) -> Record:
        self._store[record.id] = record
        return record

    def get_record_by_id(self, record_id: str) -> Optional[Record]:
        return self._store.get(record_id)

    def list_records(self) -> List[Record]:
        return list(self._store.values())
```

---

### app/services/record_service.py

```python
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
```

---

### app/controllers/record_controller.py

```python
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
```

---

### app/main.py

```python
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
```

---

### .env

```
APP_NAME=record-api
ENV=dev
```

---