from .user import User


class Customer(User):
    def __init__(self, id: int, name: str, email: str, password: str, cpf: str):
        super().__init__(id, name, email, password, cpf)
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.cpf = cpf

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
