from business.control import ShoppingCartControl
from business.model import ShoppingCartItem
from infra import ShoppingCartPersistenceRam

cart_control = ShoppingCartControl(ShoppingCartPersistenceRam())


def criar_carrinho():
    cliente_id = int(input("ID do cliente: "))
    carrinho = cart_control.create_cart(cliente_id)
    print(f"Carrinho criado com ID: {carrinho.id}")


def adicionar_item():
    carrinho_id = int(input("ID do carrinho: "))
    produto_id = int(input("ID do produto: "))
    quantidade = int(input("Quantidade: "))
    item = ShoppingCartItem(produto_id, quantidade)
    cart_control.add_item(carrinho_id, item)
    print("Item adicionado com sucesso.")


def remover_item():
    carrinho_id = int(input("ID do carrinho: "))
    item_id = int(input("ID do item: "))
    cart_control.remove_item(carrinho_id, item_id)
    print("Item removido com sucesso.")
