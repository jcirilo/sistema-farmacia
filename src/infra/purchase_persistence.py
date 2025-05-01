from abc import ABC, abstractmethod
from business.model import Purchase


class IPurchasePersistence(ABC):
    @abstractmethod
    def finalize(self, cart_id: int, customer_id: int, payment_method: str) -> Purchase:
        pass

    @abstractmethod
    def get_by_id(self, purchase_id: int) -> Purchase:
        pass

    @abstractmethod
    def list_by_customer(self, customer_id: int) -> list[Purchase]:
        pass

    @abstractmethod
    def list_all(self) -> list[Purchase]:
        pass

    @abstractmethod
    def cancel(self, purchase_id: int) -> bool:
        pass

    @abstractmethod
    def generate_invoice(self, purchase_id: int) -> dict:
        pass
