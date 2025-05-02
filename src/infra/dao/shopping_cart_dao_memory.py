from typing import Dict, Optional
from ..persistence.persistence import Persistence
from ...business.model.shopping_cart import ShoppingCart

class ShoppingCartMemoryDAO(Persistence[ShoppingCart, str]):
    def __init__(self):
        self._storage: Dict[str, ShoppingCart] = {}

    def save(self, entity: ShoppingCart) -> ShoppingCart:
        self._storage[entity.get_code()] = entity
        return entity

    def get_by_id(self, entity_id: str) -> Optional[ShoppingCart]:
        return self._storage.get(entity_id)

    def list_all(self) -> list[ShoppingCart]:
        return list(self._storage.values())

    def delete(self, entity_id: str) -> None:
        self._storage.pop(entity_id, None)
