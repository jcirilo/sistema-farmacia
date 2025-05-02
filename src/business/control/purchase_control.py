from src.infra.dao.purchase_dao_memory import PurchaseMemoryDAO
from src.business.model.purchase import Purchase

class PurchaseControl:
    def __init__(self, purchase_repo=None):
        self.__dao = purchase_repo if purchase_repo else PurchaseMemoryDAO()

    def add_purchase(self, purchase: Purchase):
        return self.__dao.save(purchase)

    def get_purchase_by_code(self, code: str):
        return self.__dao.get_by_id(code)

    def list_all(self):
        return self.__dao.list_all()

    def update_purchase(self, purchase: Purchase):
        return self.__dao.save(purchase)

    def delete_purchase(self, code: str):
        self.__dao.delete(code)
