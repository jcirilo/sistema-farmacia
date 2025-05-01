from abc import ABC, abstractmethod
from business.model import Vendedor

class IVendedorPersistence(ABC):
    @abstractmethod
    def save(self, vendedor: Vendedor) -> Vendedor:
        ...
    
    @abstractmethod
    def get_by_id(self, vendedor_id: int) -> Vendedor:
        ...
    
    @abstractmethod
    def get_all(self) -> dict:
        ...
    
    @abstractmethod
    def delete(self, vendedor_id: int) -> Vendedor:
        ...
    
    @abstractmethod
    def update(self, vendedor_id: int, nome: str, email: str) -> Vendedor:
        ...