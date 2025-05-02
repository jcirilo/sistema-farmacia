from business.control import ProductControl
from business.model import Product
from infra import ProductPersistenceRam

product_control = ProductControl(ProductPersistenceRam())


def cadastrar_produto():
    id = int(input("ID do produto: "))
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    estoque = int(input("Estoque: "))
    produto = Product(id, nome, preco, estoque)
    product_control.register(produto)
    print("Produto cadastrado com sucesso.")
