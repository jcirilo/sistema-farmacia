from typing import Dict, Optional
from ..persistence.persistence import Persistence
from ...business.model.user import User

class UserMemoryDAO(Persistence[User, int]):
    def __init__(self):
        # chave = user.id, valor = objeto User
        self._storage: Dict[int, User] = {}

    def save(self, entity: User) -> User:
        self._storage[entity.get_id()] = entity
        return entity

    def get_by_id(self, entity_id: int) -> Optional[User]:
        return self._storage.get(entity_id)

    def list_all(self) -> list[User]:
        return list(self._storage.values())

    def delete(self, entity_id: int) -> None:
        if entity_id in self._storage:
            del self._storage[entity_id]
