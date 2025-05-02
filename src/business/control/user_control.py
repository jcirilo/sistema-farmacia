from src.infra.dao.user_dao_memory import UserMemoryDAO
from src.business.model.user import User

class UserControl:
    def __init__(self, user_repo=None):
        self.__dao = UserMemoryDAO()

    def add_user(self, user: User):
        return self.__dao.save(user)

    def get_user_by_id(self, user_id: int):
        return self.__dao.get_by_id(user_id)

    def list_all(self):
        return self.__dao.list_all()

    def update_user(self, user: User):
        return self.__dao.save(user)

    def delete_user(self, user_id: int):
        self.__dao.delete(user_id)
