from business.command.command import Command
from business.model import Customer
from infra import IUserPersistence

# Exceções personalizadas para tratamento de erros
class InvalidLoginError(Exception):
    pass

class InvalidPasswordError(Exception):
    pass

class AddUserCommand:
    def __init__(self, persistence: IUserPersistence, customer: Customer):
        self.persistence = persistence
        self.customer = customer

    def execute(self) -> Customer:
        return self.persistence.save(self.customer)

    def validate_login(self, name):
        if not name:
            raise InvalidLoginError("O login não pode ser vazio")
        
        if len(name) > 12:
            raise InvalidLoginError("O login deve ter no máximo 12 caracteres")
        
        if any(char.isdigit() for char in name):
            raise InvalidLoginError("O login não pode conter números")

    def validate_password(self, password):
        if not password:
            raise InvalidPasswordError("A senha não pode ser vazia")
        
        if len(password) < 8:
            raise InvalidPasswordError("A senha deve ter no mínimo 8 caracteres")
        
        if not any(char.isdigit() for char in password):
            raise InvalidPasswordError("A senha deve conter pelo menos um número")
        
        if not any(char.isupper() for char in password):
            raise InvalidPasswordError("A senha deve conter pelo menos uma letra maiúscula")
        
        special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>/?`~"
        if not any(char in special_characters for char in password):
            raise InvalidPasswordError("A senha deve conter pelo menos um caractere especial")
