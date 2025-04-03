from business.model import Item
from .item_persistence import IItemPersistence

class ItemPersistenceFile(IItemPersistence):
    def __init__(self):
        super().__init__()
        self.__data = {}

    def save(self, item: Item) -> Item:
        self.__data[item.get_id()] = item
        return self.__data.get(item.get_id())

    def getAll(self) -> dict:
        return self.__data.values()

    def delete(self, item_id: int) -> Item:
        if item_id in self.__data:
            return self.__data.pop(item_id)
        return None

    def update(self, item_id, name, stock, price):
        pass
