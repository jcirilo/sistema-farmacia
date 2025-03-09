from abc import ABC, abstractmethod
from business.model import User

class IUserPersistence(ABC):
 
  @abstractmethod
  def save(self, user: User) -> User:
    ...

  @abstractmethod
  def getAll(self) -> dict:
    ...

  @abstractmethod
  def delete(self, user_id: int) -> User:
    ...
  
  @abstractmethod
  def update(self, user_id: int, name: str, email: str, password: str, cpf: str) -> User:
    ...