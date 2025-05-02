from src.infra.dao.shopping_cart_dao_memory import ShoppingCartMemoryDAO
from src.business.model.shopping_cart import ShoppingCart

class ShoppingCartControl:
    def __init__(self, shopping_cart_repo=None):
        self.__dao = shopping_cart_repo if  shopping_cart_repo else ShoppingCartMemoryDAO()

    def add_cart(self, cart: ShoppingCart):
        return self.__dao.save(cart)

    def get_cart_by_code(self, code: str):
        return self.__dao.get_by_id(code)

    def list_all(self):
        return self.__dao.list_all()

    def update_cart(self, cart: ShoppingCart):
        return self.__dao.save(cart)

    def delete_cart(self, code: str):
        self.__dao.delete(code)
