from abc import ABC, abstractmethod
from business.model import Carrinho

class ICarrinhoPersistence(ABC):
    @abstractmethod
    def save(self, carrinho: Carrinho) -> Carrinho:
        ...
    
    @abstractmethod
    def get_by_id(self, carrinho_id: int) -> Carrinho:
        ...
    
    @abstractmethod
    def get_all(self) -> dict:
        ...
    
    @abstractmethod
    def delete(self, carrinho_id: int) -> Carrinho:
        ...
    
    @abstractmethod
    def update(self, carrinho_id: int, itens: list) -> Carrinho:
        ...