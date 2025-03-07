from abc import ABC
from business.model import User
from infra import UserPersistenceFile


class UserControl(ABC):
    def add(self, user: User, persistence: UserPersistenceFile) -> User:
        return persistence.save(user)

    def list(self, name: str, persistence: UserPersistenceFile) -> User: 
        ...

    def listAll(self, persistence: UserPersistenceFile) -> dict:
        return persistence.getAll()

    def delete(self, user_id: int, persistence: UserPersistenceFile) -> User:
        return persistence.delete(user_id)
