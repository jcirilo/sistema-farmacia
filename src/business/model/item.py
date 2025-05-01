class Item:
    def __init__(self, id: int, name: str, stock: int, price: float):
        self.id = id
        self.name = name
        self.stock = stock
        self.price = price

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_stock(self) -> int:
        return self.__stock

    def get_price(self) -> float:
        return self.__price

    def set_name(self, name: str):
        self.__name = name

    def set_stock(self, stock: int):
        self.__stock = stock

    def set_price(self, price: float):
        self.__price = price
