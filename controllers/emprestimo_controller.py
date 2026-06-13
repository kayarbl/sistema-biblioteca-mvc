from models.emprestimo_model import EmprestimoModel
from controllers.livro_controller import LivroController
from controllers.usuario_controller import UsuarioController
from datetime import date

class EmprestimoController:
    def __init__(self):
        self.model = EmprestimoModel()
        self.livro_controller = LivroController()
        self.usuario_controller = UsuarioController()

    def emprestar(self, usuario_id, livro_id, data_emp, data_prev):
        sucesso, msg = self.livro_controller.reduzir_disponivel(livro_id)

        if not sucesso:
            return False, msg

        self.model.inserir(usuario_id, livro_id, data_emp, data_prev)

        return True, "Empréstimo registrado!"

    def listar_todos(self):
        return self.model.listar()
    
    def devolver(self, emprestimo_id):
        emprestimo = self.model.buscar_por_id(
            emprestimo_id
        )

        if not emprestimo:
            return False, "Empréstimo não encontrado!"

        if emprestimo[6] == "DEVOLVIDO":
            return False, "Este empréstimo já foi devolvido."

        livro_id = emprestimo[2]

        sucesso, msg = self.livro_controller.aumentar_disponivel(
            livro_id
        )

        if not sucesso:
            return False, msg

        self.model.devolver(
            emprestimo_id,
            date.today()
        )

        return True, "Livro devolvido!"