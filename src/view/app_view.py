import customer_view
import shopping_cart_view
import purchase_view
import seller_view
import manager_view


def menu():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Criar Carrinho")
        print("4. Adicionar Item")
        print("5. Finalizar Compra")
        print("6. Cadastrar Vendedor")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            customer_view.cadastrar_cliente()
        elif opcao == "2":
            customer_view.listar_clientes()
        elif opcao == "3":
            shopping_cart_view.criar_carrinho()
        elif opcao == "4":
            shopping_cart_view.adicionar_item()
        elif opcao == "5":
            purchase_view.finalizar_compra()
        elif opcao == "6":
            seller_view.cadastrar_vendedor()
        elif opcao == "7":
            break
        else:
            print("Opção inválida.")
