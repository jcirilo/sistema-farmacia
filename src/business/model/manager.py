from .user import User
from .seller import Seller


class Manager(User):
    def __init__(self, id: int, manager_name: str):
        super().__init__()
        self.__id = id
        self.__manager_name = manager_name

    def get_id(self) -> int:
        return self.__id

    def get_manager_name(self) -> str:
        return self.__manager_name

    def set_manager_name(self, manager_name: str):
        self.__manager_name = manager_name

    def register_manager(self, new_manager: 'Manager'):
        pass

    def register_vendor(self, new_vendor: Seller):
        pass

    def generate_sales_report_per_vendor(self, vendor: Seller):
        pass
