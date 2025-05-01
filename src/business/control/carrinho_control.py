from business.model import Carrinho, ItemCarrinho
from infra import ICarrinhoPersistence

class CarrinhoControl:
    def __init__(self, persistence: ICarrinhoPersistence):
        self.persistence = persistence

    # cria um novo carrinho para um cliente
    def criar_carrinho(self, cliente_id: int) -> Carrinho:
        return self.persistence.criar(cliente_id)
    
    # adiciona um item ao carrinho
    def adicionar_item(self, carrinho_id: int, item: ItemCarrinho) -> Carrinho:
        return self.persistence.adicionar_item(carrinho_id, item)
    
    # remove um item do carrinho
    def remover_item(self, carrinho_id: int, item_id: int) -> Carrinho:
        return self.persistence.remover_item(carrinho_id, item_id)
    
    # lista todos os itens de um carrinho
    def listar_itens(self, carrinho_id: int) -> dict:
        return self.persistence.listar_itens(carrinho_id)
    
    # finaliza o carrinho (checkout)
    def finalizar(self, carrinho_id: int) -> dict:
        return self.persistence.finalizar(carrinho_id)