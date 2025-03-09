from business.model import User
from .user_persistence import IUserPersistence


class UserPersistenceRam(IUserPersistence):
    def __init__(self):
        super().__init__()
        self.__data = {}

    def save(self, user: User) -> User:
        self.__data[user.get_id()] = user
        return self.__data.get(user.get_id())

    def getAll(self) -> dict:
        return self.__data.values()

    def delete(self, user_id: int) -> User:
        if user_id in self.__data:
            return self.__data.pop(user_id)
        return None

    def update(self, user_id, name, email, password, cpf):
        return super().update(user_id, name, email, password, cpf)