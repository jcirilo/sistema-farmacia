from .item import Item

class Purchase:
    def __init__(self, code:str, date: str, product: Item, amount: int, total: float, payment: str, status: str):
        self.__code = code
        self.__date = date
        self.__product = product
        self.__amount = amount
        self.__total = total
        self.__payment = payment
        self.__status = status

    def get_code(self) -> str:
        return self.__code

    def get_date(self) -> str:
        return self.__date

    def get_product(self) -> Item:
        return self.__product

    def get_amount(self) -> int:
        return self.__amount

    def get_total(self) -> float:
        return self.__total

    def get_payment(self) -> str:
        return self.__payment

    def get_status(self) -> str:
        return self.__status

    def set_code(self, code: str) -> str:
        self.__code = code
        return self.get_code()

    def set_date(self, date: str) -> str:
        self.__date = date
        return self.get_date()

    def set_product(self, product: Item) -> Item:
        self.__product = product
        return self.get_product()

    def set_amount(self, amount: int) -> int:
        self.__amount = amount
        return self.get_amount()

    def set_total(self, total: float) -> float:
        self.__total = total
        return self.get_total()

    def set_payment(self, payment: str) -> str:
        self.__payment = payment
        return self.get_payment()

    def set_status(self, status: str) -> str:
        self.__status = status
        return self.get_status()
    
    def __repr__(self):
        return (f"Purchase(code={self.__code!r}, date={self.__date!r}, "
                f"product={self.__product!r}, amount={self.__amount}, "
                f"total={self.__total}, payment={self.__payment!r}, "
                f"status={self.__status!r})")
