from state.purchase_in_progress import PurchaseInProgress

class Purchase:
    def __init__(self, id, customer):
        self.id = id
        self.customer = customer
        self.state = PurchaseInProgress()

    def proceed(self):
        self.state.proceed(self)

    def cancel(self):
        self.state.cancel(self)

    def __str__(self):
        return f"Compra {self.id} está {self.state}"
