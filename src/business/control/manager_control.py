from business.model import Manager
from infra import IManagerPersistence


class ManagerController:
    def __init__(self, persistence: IManagerPersistence):
        self.persistence = persistence

    def register(self, manager: Manager) -> Manager:
        return self.persistence.save(manager)

    def authenticate(self, email: str, password: str) -> Manager:
        return self.persistence.authenticate(email, password)

    def list_all(self) -> dict:
        return self.persistence.get_all()

    def update(self, manager_id: int, data: dict) -> Manager:
        return self.persistence.update(manager_id, data)

    def deactivate(self, manager_id: int) -> bool:
        return self.persistence.deactivate(manager_id)
