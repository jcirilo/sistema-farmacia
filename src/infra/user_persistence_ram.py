from business.model import Customer
from .user_persistence import IUserPersistence


class UserPersistenceRam(IUserPersistence):
    def __init__(self):
        self.__data = {}
        self.__next_id = 1

    def save(self, customer: Customer) -> Customer:
        if not customer.id:
            customer.id = self.__next_id
            self.__next_id += 1
        self.__data[customer.id] = customer
        return customer

    def getAll(self) -> list:
        return list(self.__data.values())

    def delete(self, customer_id: int) -> Customer:
        return self.__data.pop(customer_id)

    def update(self, customer_id: int, **kwargs) -> Customer:
        customer = self.__data.get(customer_id)

        for key, value in kwargs.items():
            if hasattr(customer, key):
                setattr(customer, key, value)
        return customer
