from typing import Dict, Optional
from ..persistence.persistence import Persistence
from ...business.model.purchase import Purchase

class PurchaseMemoryDAO(Persistence[Purchase, str]):
    def __init__(self):
        self._storage: Dict[str, Purchase] = {}

    def save(self, entity: Purchase) -> Purchase:
        self._storage[entity.get_code()] = entity
        return entity

    def get_by_id(self, entity_id: str) -> Optional[Purchase]:
        return self._storage.get(entity_id)

    def list_all(self) -> list[Purchase]:
        return list(self._storage.values())

    def delete(self, entity_id: str) -> None:
        self._storage.pop(entity_id, None)
