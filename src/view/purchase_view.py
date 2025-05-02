from business.control import PurchaseControl
from infra import PurchasePersistenceRam

purchase_control = PurchaseControl(PurchasePersistenceRam())


def finalizar_compra():
    carrinho_id = int(input("ID do carrinho: "))
    cliente_id = int(input("ID do cliente: "))
    metodo = input("Método de pagamento: ")
    compra = purchase_control.finalize_purchase(
        carrinho_id, cliente_id, metodo)
    print(f"Compra finalizada! ID: {compra.id}")


def cancelar_compra():
    compra_id = int(input("ID da compra: "))
    if purchase_control.cancel_purchase(compra_id):
        print("Compra cancelada com sucesso.")
