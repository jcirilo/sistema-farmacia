from abc import ABC, abstractmethod
from business.model import Gerente

class IGerentePersistence(ABC):
    @abstractmethod
    def save(self, gerente: Gerente) -> Gerente:
        ...
    
    @abstractmethod
    def get_by_id(self, gerente_id: int) -> Gerente:
        ...
    
    @abstractmethod
    def get_all(self) -> dict:
        ...
    
    @abstractmethod
    def delete(self, gerente_id: int) -> Gerente:
        ...
    
    @abstractmethod
    def update(self, gerente_id: int, nome: str, email: str) -> Gerente:
        ...