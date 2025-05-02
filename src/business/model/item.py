from abc import ABC

class Item(ABC):
    def __init__(self, name:str, manufacturer: str, price: float, amount: int, code: str):
        self.__name = name
        self.__manufacturer = manufacturer
        self.__price = price
        self.__amount = amount
        self.__code = code
    
    def get_name(self):
        return self.__name
    
    def get_manufacturer(self):
        return self.__manufacturer
    
    def get_price(self):
        return self.__price
    
    def get_amount(self):
        return self.__amount
    
    def get_code(self):
        return self.__code
    
    def set_name(self, name: str):
        self.__name = name
        return self.get_name()
    
    def set_manufacturer(self, manufacturer: str):
        self.__manufacturer = manufacturer
        return self.get_manufacturer
    
    def set_price(self, price: float):
        self.__price = price
        return self.get_price()
    
    def set_amount(self, amount: int):
        self.__amount = amount
        return self.get_amount()
    
    def set_code(self, code: str):
        self.__code = code
        return self.get_code()
    
    def __repr__(self):
        return f"code={self.get_code()}, name={self.get_name()}, manufacturer={self.get_manufacturer()}, price={self.get_price()}, ammount={self.get_amount()}"