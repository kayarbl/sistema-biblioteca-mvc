from models.livro_model import LivroModel

class LivroController:
    def __init__(self):
        self.model = LivroModel()

    def cadastrar(self, titulo, autor, ano, qtd_total, qtd_disp):
        if not titulo or not autor or not ano or qtd_total == "" or qtd_disp == "":
            return False, "Preencha todos os campos!"

        try:
            ano = int(ano)
            qtd_total = int(qtd_total)
            qtd_disp = int(qtd_disp)
        except:
            return False, "Ano e quantidades devem ser números!"

        self.model.inserir(titulo, autor, ano, qtd_total, qtd_disp)
        return True, "Livro cadastrado!"

    def listar_todos(self):
        return self.model.listar()

    def buscar_por_id(self, livro_id):
        return self.model.buscar_por_id(livro_id)

    def atualizar(self, livro_id, titulo, autor, ano, qtd_total, qtd_disp):
        if not titulo or not autor or not ano or qtd_total == "" or qtd_disp == "":
            return False, "Preencha todos os campos!"

        try:
            ano = int(ano)
            qtd_total = int(qtd_total)
            qtd_disp = int(qtd_disp)
        except:
            return False, "Ano e quantidades devem ser números!"

        self.model.atualizar(livro_id, titulo, autor, ano, qtd_total, qtd_disp)
        return True, "Livro atualizado!"

    def excluir(self, livro_id):
        self.model.excluir(livro_id)
        return True, "Livro excluído!"

    def reduzir_disponivel(self, livro_id):
        print("Livro recebido:", livro_id)

        livro = self.model.buscar_por_id(livro_id)

        print("Resultado da busca:", livro)

        if not livro:
            return False, "Livro não encontrado!"

        qtd_disp = livro[5]  # quantidade_disponivel

        print("Quantidade disponível:", qtd_disp)

        if qtd_disp <= 0:
            return False, "Nenhum exemplar disponível!"

        nova_qtd = qtd_disp - 1

        print("Nova quantidade:", nova_qtd)

        self.model.alterar_disponivel(livro_id, nova_qtd)

        return True, "Livro emprestado!"
    
    def aumentar_disponivel(self, livro_id):
        livro = self.model.buscar_por_id(livro_id)

        if not livro:
            return False, "Livro não encontrado!"

        qtd_disp = livro[5]

        nova_qtd = qtd_disp + 1

        self.model.alterar_disponivel(livro_id, nova_qtd)

        return True, "Livro devolvido!"