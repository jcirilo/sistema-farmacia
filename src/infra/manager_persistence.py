from abc import ABC, abstractmethod
from business.model import Manager


class IManagerPersistence(ABC):
    @abstractmethod
    def save(self, manager: Manager) -> Manager:
        ...

    @abstractmethod
    def get_by_id(self, manager_id: int) -> Manager:
        ...

    @abstractmethod
    def get_all(self) -> dict:
        ...

    @abstractmethod
    def delete(self, manager_id: int) -> Manager:
        ...

    @abstractmethod
    def update(self, manager_id: int, name: str, email: str) -> Manager:
        ...
