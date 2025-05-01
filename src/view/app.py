
# APP PARA TESTAR A PERSISTÊNCIA

# Para rodar abra o terminal na pasta ./src e digite:
# python -m view.app

# lembre-se que o terminal precisa estar aberto na pasta ./src
# como no exemplo:

# C:/User/sistema-farmacia/src >

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from infra import UserPersistenceRam
from business.control import UserControl
from business.model import Customer
from business.command.add_user_command import AddUserCommand

def main():
    customer_db = UserPersistenceRam()
    customer_control = UserControl(customer_db)


    # Dados dos clientes
    clientes = [
        Customer(1, "Joao", "joao@email.com", "seNh4*a1234", "012.345.678-90"),
        Customer(2, "Barbara", "barbara@email.com", "seNh4a1234", "012.345.678-90"),
        Customer(3, "Thais", "thais@email.com", "seNh4a1234", "012.345.678-90"),
        Customer(4, "Pedro", "pedro@email.com", "seNh4a1234", "012.345.678-90"),
        Customer(5, "Victor", "victor@email.com", "seNh4a1234", "012.345.678-90")
    ]

    # Adiciona clientes usando o Command
    for cliente in clientes:
        try:
            add_command = AddUserCommand(customer_control, cliente)  # Passa o objeto diretamente
            add_command.execute()
            print(f"Cliente {cliente.name} adicionado com sucesso!")
        except Exception as e:
                print(f"Erro ao adicionar {cliente.name}: {str(e)}")
        # except InvalidLoginError as e:
        #     print(f"Erro no nome do cliente {cliente.name}: {e}")
        # except InvalidPasswordError as e:
        #     print(f"Erro na senha do cliente {cliente.name}: {e}")
        # except ValueError as e:  # Erro do email_validator
        #     print(f"Erro no e-mail do cliente {cliente.name}: {e}")
        # except Exception as e:
        #     print(f"Erro inesperado com o cliente {cliente.name}: {e}")

    # lista todos os clientes
    print("\nLista de clientes:")
    for cliente in customer_control.listAll():
        print(f"ID: {cliente.id}, Nome: {cliente.name}")

if __name__ == "__main__":
    main()