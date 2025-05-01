from abc import ABC, abstractmethod
from business.model.item import Item
from infra.item_persistence import IItemPersistence

class ItemCommand(ABC):
    def __init__(self, persistence: IItemPersistence):
        self.persistence = persistence

    @abstractmethod
    def execute(self):
        pass

class CreateItemCommand(ItemCommand):
    def __init__(self, persistence: IItemPersistence, item: Item):
        super().__init__(persistence)
        self.item = item

    def execute(self) -> Item:
        return self.persistence.save(self.item)

class UpdateItemCommand(ItemCommand):
    def __init__(self, persistence: IItemPersistence, 
                 item_id: int, name: str, stock: int, price: float):
        super().__init__(persistence)
        self.item_id = item_id
        self.name = name
        self.stock = stock
        self.price = price

    def execute(self) -> Item:
        return self.persistence.update(
            self.item_id,
            self.name,
            self.stock,
            self.price
        )

