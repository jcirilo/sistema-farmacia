
# APP PARA TESTAR A PERSISTÊNCIA

# Para rodar abra o terminal na pasta ./src e digite:
# python -m view.app

# lembre-se que o terminal precisa está aberto na pasta ./src
# como no exemplo:

# C:/User/sistema-farmacia/src >

from infra import UserPersistenceFile
from business.control import UserControl
from business.model import Customer

customer_db: UserPersistenceFile = UserPersistenceFile()
customer_control: UserControl   = UserControl()

cliente1: Customer = Customer(1, "Joao", "joao@email.com", "seNh4a1234", "012.345.678-90")
cliente2: Customer = Customer(2, "Barbara", "barbara@email.com", "seNh4a1234", "012.345.678-90")
cliente3: Customer = Customer(3, "Thais", "thais@email.com", "seNh4a1234", "012.345.678-90")
cliente4: Customer = Customer(4, "Pedro", "pedro@email.com", "seNh4a1234", "012.345.678-90")
cliente5: Customer = Customer(5, "Victor", "victor@email.com", "seNh4a1234", "012.345.678-90")

customer_control.add(cliente1, customer_db)
customer_control.add(cliente2, customer_db)
customer_control.add(cliente3, customer_db)
customer_control.add(cliente4, customer_db)
customer_control.add(cliente5, customer_db)

print(customer_control.listAll(customer_db))