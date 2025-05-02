from .user import User

class Seller(User):
    # Glossario
    # Nome: 40 posições - alfanumérico
    # CPF: 11 posições - numérico
    # Salário: 10 posições - numérico (formato decimal)
    # Status: 1 posição - caractere - domínio: A para Ativo ou I para Inativo
    
    def __init__(self, id: int, name: str, email: str, password:str, cpf: str, phone_number: str, status: str):
        super().__init__(id, name, email, password, cpf, phone_number)
        self.__status = status

    def get_status(self):
        return self.__status;

    def set_status(self, status: str):
        self.__status = status
        return self.get_status()
    
    def __repr__(self):
        return f"{super().__repr__()[:-1]}, status={self.__status!r})"
