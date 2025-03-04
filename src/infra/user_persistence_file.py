from business.model import User
from .user_persistence import IUserPersistence

class UserPersistenceFile(IUserPersistence):
    def __init__(self):
        super().__init__()
        self.__data = {}

    def save(self, user: User) -> User:
        self.__data[user.get_id()] = user
        return self.__data.get(user.get_id())
    
    def getAll(self) -> dict:
        return self.__data.values()
    