from state.purchase_state import PurchaseState

class PurchaseCompleted(PurchaseState):
    def proceed(self, purchase):
        raise Exception("Compra já concluída!")

    def cancel(self, purchase):
        raise Exception("Não pode cancelar uma compra concluída!")

    def __str__(self):
        return "Concluída"
