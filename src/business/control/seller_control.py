from business.model import Seller
from infra import ISellerPersistence


class SellerController:
    def __init__(self, persistence: ISellerPersistence):
        self.persistence = persistence

    def register(self, seller: Seller) -> Seller:
        return self.persistence.save(seller)

    def list_all(self) -> dict:
        return self.persistence.get_all()

    def get_by_id(self, seller_id: int) -> Seller:
        return self.persistence.get_by_id(seller_id)

    def update(self, seller_id: int, data: dict) -> Seller:
        return self.persistence.update(seller_id, data)

    def remove(self, seller_id: int) -> bool:
        return self.persistence.remove(seller_id)
