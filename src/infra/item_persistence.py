from abc import ABC, abstractmethod
from business.model import Item


class IItemPersistence(ABC):

    @abstractmethod
    def save(self, item: Item) -> Item:
        ...

    @abstractmethod
    def getAll(self) -> dict:
        ...

    @abstractmethod
    def delete(self, item_id: int) -> Item:
        ...

    @abstractmethod
    def update(self, item_id: int, name: str, stock: int, price: float) -> Item:
        ...
