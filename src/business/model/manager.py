from .user import User
from .vendor import Vendor


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
        # registrar um novo gerente
        pass

    def register_vendor(self, new_vendor: Vendor):
        #  registrar um novo vendedor
        pass

    def generate_sales_report_per_vendor(self, vendor: Vendor):
        # gerar relatório de vendas por vendedor
        pass