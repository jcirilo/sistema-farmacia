from typing import Optional
from .item_control import ItemControl
from .purchase_control import PurchaseControl
from .shopping_cart_control import ShoppingCartControl
from .user_control import UserControl
from ..model.user import User
from ..model.item import Item
from ..model.purchase import Purchase
from ..model.shopping_cart import ShoppingCart

class FacadeSingletonControl:
    _instance: Optional["FacadeSingletonControl"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FacadeSingletonControl, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self) -> None:
        # Initialize controllers
        self._item_ctrl = ItemControl()
        self._purchase_ctrl = PurchaseControl()
        self._cart_ctrl = ShoppingCartControl()
        self._user_ctrl = UserControl()

    @property
    def item_control(self) -> ItemControl:
        return self._item_ctrl

    @property
    def purchase_control(self) -> PurchaseControl:
        return self._purchase_ctrl

    @property
    def shopping_cart_control(self) -> ShoppingCartControl:
        return self._cart_ctrl

    @property
    def user_control(self) -> UserControl:
        return self._user_ctrl

    # Item operations
    def add_item(self, item: Item) -> Item:
        return self._item_ctrl.add_item(item)

    def get_item(self, code: str) -> Optional[Item]:
        return self._item_ctrl.get_item_by_code(code)

    def list_items(self) -> list[Item]:
        return self._item_ctrl.list_all()

    def update_item(self, item: Item) -> Item:
        return self._item_ctrl.update_item(item)

    def delete_item(self, code: str) -> None:
        self._item_ctrl.delete_item(code)

    # Purchase operations
    def add_purchase(self, purchase: Purchase) -> Purchase:
        return self._purchase_ctrl.add_purchase(purchase)

    def get_purchase(self, code: str) -> Optional[Purchase]:
        return self._purchase_ctrl.get_purchase_by_code(code)

    def list_purchases(self) -> list[Purchase]:
        return self._purchase_ctrl.list_all()

    def update_purchase(self, purchase: Purchase) -> Purchase:
        return self._purchase_ctrl.update_purchase(purchase)

    def delete_purchase(self, code: str) -> None:
        self._purchase_ctrl.delete_purchase(code)

    # ShoppingCart operations
    def add_shopping_cart(self, cart: ShoppingCart) -> ShoppingCart:
        return self._cart_ctrl.add_cart(cart)

    def get_shopping_cart(self, code: str) -> Optional[ShoppingCart]:
        return self._cart_ctrl.get_cart_by_code(code)

    def list_shopping_carts(self) -> list[ShoppingCart]:
        return self._cart_ctrl.list_all()

    def update_shopping_cart(self, cart: ShoppingCart) -> ShoppingCart:
        return self._cart_ctrl.update_cart(cart)

    def delete_shopping_cart(self, code: str) -> None:
        self._cart_ctrl.delete_cart(code)

    # User operations
    def add_user(self, user: User) -> User:
        return self._user_ctrl.add_user(user)

    def get_user(self, user_id: int) -> Optional[User]:
        return self._user_ctrl.get_user_by_id(user_id)

    def list_users(self) -> list[User]:
        return self._user_ctrl.list_all()

    def update_user(self, user: User) -> User:
        return self._user_ctrl.update_user(user)

    def delete_user(self, user_id: int) -> None:
        self._user_ctrl.delete_user(user_id)
