from .user import User

class Customer(User):
  def __init__(self, id: int, name: str, email:str, password:str, cpf:str):
    super().__init__(id, name, email, password, cpf)