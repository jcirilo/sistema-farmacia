from business.model import Customer
from infra import IUserPersistence
from adapter.email_validator_adapter import EmailValidatorAdapter
from command.add_user_command import AddUserCommand

class UserControl():
    def __init__(self, persistence: IUserPersistence):
        super().__init__()
        self.persistence = persistence
        self.email_validator = EmailValidatorAdapter()

    def add(self, customer: Customer) -> Customer:
        if not self.email_validator.is_valid(customer.email):
            raise ValueError("E-mail inválido.")

        command = AddUserCommand(self.persistence, customer)            
        return command.execute()

    def listAll(self) -> list[Customer]:
        return list(self.persistence.getAll())

    def delete(self, user_id: int) -> Customer:
        return self.persistence.delete(user_id)
