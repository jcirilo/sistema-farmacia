from business.model import Item
from infra import IItemPersistence


class ItemControl:
    def __init__(self, persistence: IItemPersistence):
        self.persistence = persistence

    def add(self, item: Item) -> Item:
        return self.persistence.save(item)

    def listAll(self) -> dict:
        return self.persistence.getAll()

    def delete(self, item_id: int) -> Item:
        return self.persistence.delete(item_id)

    def update(self, item_id: int, name: str, stock: int, price: float):
        return self.persistence.update(item_id, name, stock, price)
