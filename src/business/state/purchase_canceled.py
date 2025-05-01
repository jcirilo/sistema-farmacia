from state.purchase_state import PurchaseState

class PurchaseCanceled(PurchaseState):
    def proceed(self, purchase):
        raise Exception("Compra cancelada não pode prosseguir!")

    def cancel(self, purchase):
        raise Exception("Compra já foi cancelada!")

    def __str__(self):
        return "Cancelada"
