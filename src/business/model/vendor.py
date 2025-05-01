from .user import User

class Vendor(User):
    def __init__(self, id: int, vendor_name: str):
        super().__init__()
        self.__id = id
        self.__vendor_name = vendor_name

    def get_id(self) -> int:
        return self.__id

    def get_vendor_name(self) -> str:
        return self.__vendor_name

    def set_vendor_name(self, vendor_name: str):
        self.__vendor_name = vendor_name

    def control_stock(self):
        # controlar estoque
        pass

    def control_purchase(self):
        # controlar compras
        pass

    def generate_sales_report(self):
        # gerar relatório de vendas
        pass