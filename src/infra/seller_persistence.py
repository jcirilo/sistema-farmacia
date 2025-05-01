from abc import ABC, abstractmethod
from business.model import Seller


class ISellerPersistence(ABC):
    @abstractmethod
    def save(self, seller: Seller) -> Seller:
        ...

    @abstractmethod
    def get_by_id(self, seller_id: int) -> Seller:
        ...

    @abstractmethod
    def get_all(self) -> dict:
        ...

    @abstractmethod
    def delete(self, seller_id: int) -> Seller:
        ...

    @abstractmethod
    def update(self, seller_id: int, name: str, email: str) -> Seller:
        ...
