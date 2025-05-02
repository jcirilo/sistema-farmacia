from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')
ID = TypeVar('ID')

class Persistence(ABC, Generic[T, ID]):

    @abstractmethod
    def save(self, entity: T) -> T:
        """Cria ou atualiza a entidade."""
        pass

    @abstractmethod
    def get_by_id(self, entity_id: ID) -> Optional[T]:
        """Retorna a entidade pelo ID (ou código)."""
        pass

    @abstractmethod
    def list_all(self) -> List[T]:
        """Retorna todas as entidades."""
        pass

    @abstractmethod
    def delete(self, entity_id: ID) -> None:
        """Remove a entidade."""
        pass
