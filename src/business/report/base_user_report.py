from abc import ABC, abstractmethod
from typing import List
from business.model.customer import Customer

class BaseUserReport(ABC):

    def generate(self, customers: List[Customer], access_log: dict) -> str:
        self._start_report()
        self._add_title()
        self._add_summary(customers, access_log)
        self._add_details(customers, access_log)
        return self._finalize()

    def _start_report(self):
        self.report = ""

    @abstractmethod
    def _add_title(self):
        pass

    @abstractmethod
    def _add_summary(self, customers: List[Customer], access_log: dict):
        pass

    @abstractmethod
    def _add_details(self, customers: List[Customer], access_log: dict):
        pass

    @abstractmethod
    def _finalize(self) -> str:
        pass
