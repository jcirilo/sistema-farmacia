from business.control import UserControl
from business.model import Customer
from infra import UserPersistenceRam

user_control = UserControl(UserPersistenceRam())


def cadastrar_cliente():
    print("\n--- Cadastro de Cliente ---")
    try:
        id = int(input("ID: "))
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        cpf = input("CPF: ")

        cliente = Customer(id, nome, email, senha, cpf)
        user_control.add(cliente)
        print("Cliente cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar cliente: {str(e)}")


def listar_clientes():
    print("\n--- Lista de Clientes ---")
    clientes = user_control.listAll()
    for cliente in clientes.values():
        print(f"ID: {cliente.id} | Nome: {cliente.name} | Email: {cliente.email}")
