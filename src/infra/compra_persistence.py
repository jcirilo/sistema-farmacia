from abc import ABC, abstractmethod
from business.model import Compra

class ICompraPersistence(ABC):
    @abstractmethod
    def finalizar(self, carrinho_id: int, cliente_id: int, metodo_pagamento: str) -> Compra:
        pass
    
    @abstractmethod
    def buscar_por_id(self, compra_id: int) -> Compra:
        pass
    
    @abstractmethod
    def listar_por_cliente(self, cliente_id: int) -> list[Compra]:
        pass
    
    @abstractmethod
    def listar_todas(self) -> list[Compra]:
        pass
    
    @abstractmethod
    def cancelar(self, compra_id: int) -> bool:
        pass
    
    @abstractmethod
    def gerar_nota_fiscal(self, compra_id: int) -> dict:
        pass