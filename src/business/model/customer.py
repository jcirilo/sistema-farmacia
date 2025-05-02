from .user import User

class Customer(User):
    def __init__(self, id: int, name: str, email: str, password:str, cpf: str, phone_number: str):
        super().__init__(id, name, email, password, cpf, phone_number)

    def __repr__(self):
        return super().__repr__()