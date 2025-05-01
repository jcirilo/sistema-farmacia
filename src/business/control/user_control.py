import sys
from pathlib import Path
from business.model import Customer
from infra import IUserPersistence
from adapter.email_validator_adapter import EmailValidatorAdapter
from business.command.add_user_command import AddUserCommand

# Adiciona o diretório 'business' ao sys.path
BUSINESS_DIR = Path(__file__).resolve().parent
sys.path.append(str(BUSINESS_DIR))

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
