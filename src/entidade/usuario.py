class Usuario:
    def __init__(self, id: int, nome: str, email: str, cpf: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.cpf = cpf

    def __repr__(self):
        return f"Usuário (id={self.id}, nome='{self.nome}', email='{self.email}', cpf='{self.cpf}')"
    
usuarios = []

def adicionar_usuario(id: int, nome: str, email: str, cpf: str):
    novo_usuario = Usuario(id, nome, email, cpf)
    usuarios.append(novo_usuario)
    print(f"Usuário adicionado: {novo_usuario}")