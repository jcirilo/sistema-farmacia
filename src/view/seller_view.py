from business.control import SellerControl
from business.model import Seller
from infra import SellerPersistenceRam

seller_control = SellerControl(SellerPersistenceRam())


def cadastrar_vendedor():
    id = int(input("ID: "))
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    vendedor = Seller(id, nome, email, senha)
    seller_control.register(vendedor)
    print("Vendedor cadastrado com sucesso.")


def listar_vendedores():
    vendedores = seller_control.get_all()
    for v in vendedores.values():
        print(f"ID: {v.id} | Nome: {v.name}")
