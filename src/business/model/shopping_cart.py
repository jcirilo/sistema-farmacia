from .item import Item

class ShoppingCart():

    # Glossario
    # Código do Carrinho: 10 posições - alfanumérico
    # Itens: Lista de medicamentos adicionados ao carrinho
    # Quantidade por Item: 5 posições - numérico
    # Subtotal: 10 posições - numérico (formato decimal)
    def __init__(self, code: str, items: list[Item]):
        self.__code = code
        self.__items= items
        self.__total= self.__calculate_total()

    def __calculate_total(self) -> float:
        return sum(item.get_price() for item in self.__items)

    def get_code(self) -> str:
        return self.__code

    def get_item(self, index: int):
        return self.__items[index]
        
    def get_items(self) -> list[Item]:
        return self.__items.copy()

    def get_total(self) -> float:
        return self.__total

    def set_code(self, code: str) -> str:
        self.__code = code
        return self.get_code()

    def set_item(self, index: int, item: Item):
        self.__items[index] = item
        self.set_total(self.__calculate_total())
        return self.get_item(index)
    
    def set_items(self, items: list[Item]) -> list:
        self.__items = items
        self.set_total(self.__calculate_total())
        return self.get_items()

    def set_total(self, total: float) -> float:
        self.__total = total
        return self.get_total()
    
    def __repr__(self):
        return (f"ShoppingCart(code={self.__code!r}, "
                f"items={self.__items!r}, "
                f"total={self.__total})")