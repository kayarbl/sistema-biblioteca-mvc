from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QMessageBox
)

from controllers.livro_controller import LivroController


class LivrosView(QWidget):
    def __init__(self):
        super().__init__()

        self.controller = LivroController()

        self.setWindowTitle("Cadastro de Livros")
        self.setMinimumWidth(700)

        layout = QVBoxLayout()

        # Inputs
        self.input_titulo = QLineEdit()
        self.input_autor = QLineEdit()
        self.input_ano = QLineEdit()
        self.input_qtd_total = QLineEdit()
        self.input_qtd_disp = QLineEdit()

        layout.addWidget(QLabel("Título:"))
        layout.addWidget(self.input_titulo)

        layout.addWidget(QLabel("Autor:"))
        layout.addWidget(self.input_autor)

        layout.addWidget(QLabel("Ano de Publicação:"))
        layout.addWidget(self.input_ano)

        layout.addWidget(QLabel("Quantidade Total:"))
        layout.addWidget(self.input_qtd_total)

        layout.addWidget(QLabel("Quantidade Disponível:"))
        layout.addWidget(self.input_qtd_disp)

        # Botão cadastrar
        btn_cadastrar = QPushButton("Cadastrar Livro")
        btn_cadastrar.clicked.connect(self.cadastrar)
        layout.addWidget(btn_cadastrar)

        # Tabela
        self.tabela = QTableWidget()
        layout.addWidget(self.tabela)

        # Botão atualizar lista
        btn_atualizar = QPushButton("Atualizar Lista")
        btn_atualizar.clicked.connect(self.carregar)
        layout.addWidget(btn_atualizar)

        self.setLayout(layout)
        self.carregar()

    def cadastrar(self):
        titulo = self.input_titulo.text()
        autor = self.input_autor.text()
        ano = self.input_ano.text()
        qtd_total = self.input_qtd_total.text()
        qtd_disp = self.input_qtd_disp.text()

        ok, msg = self.controller.cadastrar(
            titulo, autor, ano, qtd_total, qtd_disp
        )

        if ok:
            QMessageBox.information(self, "Sucesso", msg)

            self.input_titulo.clear()
            self.input_autor.clear()
            self.input_ano.clear()
            self.input_qtd_total.clear()
            self.input_qtd_disp.clear()

            self.carregar()
        else:
            QMessageBox.warning(self, "Erro", msg)

    def carregar(self):
        dados = self.controller.listar_todos()

        self.tabela.setRowCount(len(dados))
        self.tabela.setColumnCount(6)

        self.tabela.setHorizontalHeaderLabels([
            "ID", "Título", "Autor", "Ano", "Total", "Disponível"
        ])

        for linha, registro in enumerate(dados):
            for col, valor in enumerate(registro):
                self.tabela.setItem(
                    linha, col, QTableWidgetItem(str(valor))
                )

    # -----------------------------
    # CORRETO (SEM SQL NA VIEW)
    # -----------------------------
    def atualizar_quantidade_disponivel(self, livro_id):
        ok, msg = self.controller.reduzir_disponivel(livro_id)

        if ok:
            QMessageBox.information(self, "Sucesso", msg)
            self.carregar()
        else:
            QMessageBox.warning(self, "Erro", msg)