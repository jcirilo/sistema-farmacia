from abc import ABC, abstractmethod
from business.model import ShoppingCart


class IShoppingCartPersistence(ABC):
    @abstractmethod
    def save(self, cart: ShoppingCart) -> ShoppingCart:
        ...

    @abstractmethod
    def get_by_id(self, cart_id: int) -> ShoppingCart:
        ...

    @abstractmethod
    def get_all(self) -> dict:
        ...

    @abstractmethod
    def delete(self, cart_id: int) -> ShoppingCart:
        ...

    @abstractmethod
    def update(self, cart_id: int, items: list) -> ShoppingCart:
        ...
