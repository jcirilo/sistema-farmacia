from business.model import Compra, ItemCompra
from infra import ICompraPersistence

class CompraControl:
    def __init__(self, persistence: ICompraPersistence):
        self.persistence = persistence

    # finaliza uma compra (checkout do carrinho)
    def finalizar_compra(self, carrinho_id: int, cliente_id: int, metodo_pagamento: str) -> Compra:
        return self.persistence.finalizar(carrinho_id, cliente_id, metodo_pagamento)
    
    # busca uma compra por ID
    def buscar_por_id(self, compra_id: int) -> Compra:
        return self.persistence.buscar_por_id(compra_id)
    
    # lista todas as compras de um cliente
    def listar_por_cliente(self, cliente_id: int) -> list[Compra]:
        return self.persistence.listar_por_cliente(cliente_id)
    
    # lista todas as compras (para administradores)
    def listar_todas(self) -> list[Compra]:
        return self.persistence.listar_todas()
    
    # cancela uma compra (se ainda não processada)
    def cancelar_compra(self, compra_id: int) -> bool:
        return self.persistence.cancelar(compra_id)
    
    # gera nota fiscal de uma compra
    def gerar_nota_fiscal(self, compra_id: int) -> dict:
        return self.persistence.gerar_nota_fiscal(compra_id)