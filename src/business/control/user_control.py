from business.model import User
from infra import IUserPersistence
from adapter.email_validator_adapter import EmailValidatorAdapter

class UserControl():
    def __init__(self, persistence: IUserPersistence):
        super().__init__()
        self.persistence = persistence

    def add(self, user: User) -> User:
        if not self.email_validator.is_valid(user.get_email()):
            raise ValueError("E-mail inválido.")
            
        return self.persistence.save(user)

    #def list(self, name: str) -> User: 
    #    ...

    def listAll(self) -> dict:
        return self.persistence.getAll()

    def delete(self, user_id: int) -> User:
        return self.persistence.delete(user_id)
