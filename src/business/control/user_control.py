from business.model import Customer
from infra import IUserPersistence
from adapter.email_validator_adapter import EmailValidatorAdapter

class UserControl():
    def __init__(self, persistence: IUserPersistence):
        super().__init__()
        self.persistence = persistence
        self.email_validator = EmailValidatorAdapter()

    def add(self, customer: Customer) -> Customer:
        if not self.email_validator.is_valid(customer.email):
            raise ValueError("E-mail inválido.")
            
        return self.persistence.save(customer)

    def listAll(self) -> list[Customer]:
        return list(self.persistence.getAll())

    def delete(self, user_id: int) -> Customer:
        return self.persistence.delete(user_id)
