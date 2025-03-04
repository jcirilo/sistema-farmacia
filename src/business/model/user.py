from abc import ABC

class User(ABC):
    
    def __init__(self, id: int, name: str, email: str, password:str, cpf: str):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__cpf = cpf
        self.__password = password

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> int:
        return self.__id

    def get_email(self) -> str:
        return self.__email
    
    def get_cpf(self) -> str:
        return self.__cpf

    def get_password(self) -> str:
        return self.__password

    def set_name(self, name:str) -> str:
        self.__name = name
        return self.get_name()

    def set_email(self, email:str) -> str:
        self.__email = email
        return self.get_email()

    def set_password(self, password:str) -> str:
        self.__password = password
        return self.get_password()

    def set_cpf(self, cpf:str) -> str:
        self.__cpf = cpf
        return self.get_cpf()
    
    def __repr__(self):
        return f"(id={self.__id}, nome='{self.__name}', email='{self.__email}', password='{self.__password}', cpf='{self.__cpf}')"