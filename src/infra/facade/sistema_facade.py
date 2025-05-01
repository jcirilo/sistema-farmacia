import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))  

from business.model.item import Item 
from business.command.item_command import CreateItemCommand, UpdateItemCommand
from infra.item_persistence_ram import ItemPersistenceRam

class SistemaFacade:
    def __init__(self):
        self.__item_persistence = ItemPersistenceRam()

    # métodos para produto/item:
    def cadastrar_produto(self, nome: str, estoque: int, preco: float):
        item = Item(name=nome, stock=estoque, price=preco)
        command = CreateItemCommand(self.persistence, item)
        return command.execute()

    def atualizar_produto(self, produto_id: int, nome: str = None, 
                         estoque: int = None, preco: float = None) -> bool:
        try:
            # Obtém item atual para manter valores não informados
            itens = self.__item_persistence.getAll()
            item_atual = itens.get(produto_id)
            
            if not item_atual:
                return False
                
            # Aplica apenas as atualizações fornecidas
            nome = nome if nome is not None else item_atual.name
            estoque = estoque if estoque is not None else item_atual.stock
            preco = preco if preco is not None else item_atual.price
            
            resultado = self.__item_control.update(
                item_id=produto_id,
                name=nome,
                stock=estoque,
                price=preco
            )
            return resultado is not None
        except:
            return False

    def listar_produtos(self) -> list:
        try:
            itens = self.__item_control.listAll()
            return [{
                'id': item.id,
                'nome': item.name,
                'estoque': item.stock,
                'preco': item.price
            } for item in itens.values()]
        except:
            return []

    def remover_produto(self, produto_id: int) -> dict:
        try:
            sucesso = self.__item_control.delete(produto_id) is not None
            return {
                'status': sucesso,
                'mensagem': 'Produto removido' if sucesso else 'ID não encontrado'
            }
        except Exception as e:
            return {
                'status': False,
                'mensagem': f'Erro na remoção: {str(e)}'
            }

    # métodos para Carrinho
    def adicionar_ao_carrinho(self, usuario_id: int, item_id: int, quantidade: int):
        return self.carrinho.adicionar_item(
            usuario_id=usuario_id,
            item_id=item_id,
            quantidade=quantidade
        )


    # métodos para Usuário
    def registrar_usuario(self, nome: str, email: str):
        return self.usuario.criar_usuario(
            nome=nome,
            email=email
        )
    
    def atualizar_estoque(self, produto_id: int, novo_estoque: int) -> bool:
        updated_item = self.__item_control.update(
            item_id=produto_id,
            name=None,  # Mantém o nome atual
            stock=novo_estoque,
            price=None  # Mantém o preço atual
        )
        return updated_item is not None