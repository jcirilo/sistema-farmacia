from business.model.item import Item
from infra import IItemPersistence

class ItemControl:
    def __init__(self, persistence: IItemPersistence):
        self.persistence = persistence

    # adiciona um novo item ao sistema
    def add(self, item: Item) -> Item:
        return self.persistence.save(item)
    
    # lista todos os itens cadastrados no sistema
    def listAll(self) -> dict:
        return self.persistence.getAll()

    # remove um item do sistema pelo ID
    def delete(self, item_id: int) -> Item:
        return self.persistence.delete(item_id)
    
    # atualiza um item existente no sistema
    def update(self, item_id: int, name: str, stock: int, price: float):
        return self.persistence.update(item_id, name, stock, price)
