from business.model import ShoppingCart, ShoppingCartItem
from infra import IShoppingCartPersistence


class ShoppingCartController:
    def __init__(self, persistence: IShoppingCartPersistence):
        self.persistence = persistence

    def create_cart(self, customer_id: int) -> ShoppingCart:
        return self.persistence.create(customer_id)

    def add_item(self, cart_id: int, item: ShoppingCartItem) -> ShoppingCart:
        return self.persistence.add_item(cart_id, item)

    def remove_item(self, cart_id: int, item_id: int) -> ShoppingCart:
        return self.persistence.remove_item(cart_id, item_id)

    def list_items(self, cart_id: int) -> dict:
        return self.persistence.list_items(cart_id)

    def finalize(self, cart_id: int) -> dict:
        return self.persistence.finalize(cart_id)
