from .user import User


class Seller(User):
    def __init__(self, id: int, seller_name: str):
        super().__init__()
        self.__id = id
        self.__seller_name = seller_name

    def get_id(self) -> int:
        return self.__id

    def get_seller_name(self) -> str:
        return self.__seller_name

    def set_seller_name(self, seller_name: str):
        self.__seller_name = seller_name

    def control_stock(self):
        pass

    def control_purchase(self):
        pass

    def generate_sales_report(self):
        pass
