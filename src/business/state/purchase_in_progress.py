from state.purchase_state import PurchaseState
from state.purchase_completed import PurchaseCompleted
from state.purchase_canceled import PurchaseCanceled

class PurchaseInProgress(PurchaseState):
    def proceed(self, purchase):
        purchase.state = PurchaseCompleted()
    
    def cancel(self, purchase):
        purchase.state = PurchaseCanceled()

    def __str__(self):
        return "Em andamento"
