from business.control import ManagerControl
from business.model import Manager
from infra import ManagerPersistenceRam

manager_control = ManagerControl(ManagerPersistenceRam())


def cadastrar_gerente():
    id = int(input("ID: "))
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    gerente = Manager(id, nome, email, senha)
    manager_control.register(gerente)
    print("Gerente cadastrado com sucesso.")
