from abc import ABC, abstractmethod
from typing import Tuple

class ILoginValidator(ABC):
    @abstractmethod
    def validate(self, login: str) -> Tuple[bool, str]:
        pass

class IPasswordValidator(ABC):
    @abstractmethod
    def validate(self, password: str) -> Tuple[bool, str]:
        pass