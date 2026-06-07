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