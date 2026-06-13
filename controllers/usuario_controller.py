from models.usuario_model import UsuarioModel

class UsuarioController:
    def __init__(self):
        self.model = UsuarioModel()

    def cadastrar(self, nome, email, telefone):
        if nome == "" or email == "" or telefone == "":
            return False, "Preencha todos os campos!"
        self.model.inserir(nome, email, telefone)
        return True, "Usuário cadastrado!"

    def listar_todos(self):
        return self.model.listar()
