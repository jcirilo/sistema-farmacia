from typing import Dict, Optional
from ..persistence.persistence import Persistence
from ...business.model.item import Item

class ItemMemoryDAO(Persistence[Item, str]):
    def __init__(self):
        self._storage: Dict[str, Item] = {}

    def save(self, entity: Item) -> Item:
        self._storage[entity.get_code()] = entity
        return entity

    def get_by_id(self, entity_id: str) -> Optional[Item]:
        return self._storage.get(entity_id)

    def list_all(self) -> list[Item]:
        return list(self._storage.values())

    def delete(self, entity_id: str) -> None:
        self._storage.pop(entity_id, None)
