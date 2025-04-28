from abc import ABC, abstractmethod

class PurchaseState(ABC):
    @abstractmethod
    def proceed(self, purchase):
        pass

    @abstractmethod
    def cancel(self, purchase):
        pass

    @abstractmethod
    def __str__(self):
        pass
