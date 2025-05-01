from business.model import Vendedor
from infra import IVendedorPersistence

class VendedorControl:
    def __init__(self, persistence: IVendedorPersistence):
        self.persistence = persistence

    # cadastra um vendedor
    def cadastrar(self, vendedor: Vendedor) -> Vendedor:
        return self.persistence.salvar(vendedor)
    
    # lista todos os vendedores
    def listar_todos(self) -> dict:
        return self.persistence.obter_todos()
    
    # busca vendedor por ID
    def buscar_por_id(self, vendedor_id: int) -> Vendedor:
        return self.persistence.obter_por_id(vendedor_id)
    
    # atualiza dados do vendedor
    def atualizar(self, vendedor_id: int, dados: dict) -> Vendedor:
        return self.persistence.atualizar(vendedor_id, dados)
    
    # remove um vendedor
    def remover(self, vendedor_id: int) -> bool:
        return self.persistence.remover(vendedor_id)