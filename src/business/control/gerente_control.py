from business.model import Gerente
from infra import IGerentePersistence

class GerenteControl:
    def __init__(self, persistence: IGerentePersistence):
        self.persistence = persistence

    # cadastra um novo gerente
    def cadastrar(self, gerente: Gerente) -> Gerente:
        return self.persistence.salvar(gerente)
    
    # autentica um gerente
    def autenticar(self, email: str, senha: str) -> Gerente:
        return self.persistence.autenticar(email, senha)
    
    # lista todos os gerentes
    def listar_todos(self) -> dict:
        return self.persistence.obter_todos()
    
    # atualiza dados do gerente
    def atualizar(self, gerente_id: int, dados: dict) -> Gerente:
        return self.persistence.atualizar(gerente_id, dados)
    
    # desativa um gerente
    def desativar(self, gerente_id: int) -> bool:
        return self.persistence.desativar(gerente_id)