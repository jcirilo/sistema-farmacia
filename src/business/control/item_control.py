from src.infra.dao.item_dao_memory import ItemMemoryDAO
from src.business.model.item import Item

class ItemControl:
    def __init__(self, item_repo=None):
        self.__dao = item_repo if item_repo else ItemMemoryDAO()

    def add_item(self, item: Item):
        return self.__dao.save(item)

    def get_item_by_code(self, code: str):
        return self.__dao.get_by_id(code)

    def list_all(self):
        return self.__dao.list_all()

    def update_item(self, item: Item):
        return self.__dao.save(item)

    def delete_item(self, code: str):
        self.__dao.delete(code)
