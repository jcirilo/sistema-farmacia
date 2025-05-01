from .purchase import Purchase
from .item import Item


class Cart:
    def __init__(self, purchase: Purchase):
        self.__purchase = purchase
        self.__items = {}

    def get_purchase(self) -> Purchase:
        return self.__purchase

    def add_item(self, item: Item, quantity: int):
        if item in self.__items:
            self.__items[item] += quantity
        else:
            self.__items[item] = quantity

    def remove_item(self, item: Item):
        if item in self.__items:
            del self.__items[item]

    def get_items(self) -> dict:
        return self.__items

    def calculate_total(self) -> float:
        return sum(item.get_price() * qty for item, qty in self.__items.items())

    def clear_cart(self):
        self.__items.clear()
