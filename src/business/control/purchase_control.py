from business.model import Purchase, PurchaseItem
from infra import IPurchasePersistence


class PurchaseController:
    def __init__(self, persistence: IPurchasePersistence):
        self.persistence = persistence

    def finalize_purchase(self, cart_id: int, customer_id: int, payment_method: str) -> Purchase:
        return self.persistence.finalize(cart_id, customer_id, payment_method)

    def get_by_id(self, purchase_id: int) -> Purchase:
        return self.persistence.get_by_id(purchase_id)

    def list_by_customer(self, customer_id: int) -> list[Purchase]:
        return self.persistence.list_by_customer(customer_id)

    def list_all(self) -> list[Purchase]:
        return self.persistence.list_all()

    def cancel_purchase(self, purchase_id: int) -> bool:
        return self.persistence.cancel(purchase_id)

    def generate_invoice(self, purchase_id: int) -> dict:
        return self.persistence.generate_invoice(purchase_id)
