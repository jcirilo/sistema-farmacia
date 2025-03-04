from abc import ABC, abstractmethod
from business.model import User

class IUserPersistence(ABC):
 
  @abstractmethod
  def save(self, user: User) -> User:
    ...

  @abstractmethod
  def getAll(self) -> dict:
    ...