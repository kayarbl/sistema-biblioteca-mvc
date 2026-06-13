from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QComboBox, QMessageBox
)
from datetime import date, timedelta
from controllers.emprestimo_controller import EmprestimoController


class EmprestimoView(QWidget):
    def __init__(self):
        super().__init__()

        self.controller = EmprestimoController()

        self.setWindowTitle("Empréstimo de Livros")
        self.setMinimumWidth(600)

        layout = QVBoxLayout()

        # Usuários
        layout.addWidget(QLabel("Selecione o usuário:"))

        self.usuarios_disp = QComboBox()
        layout.addWidget(self.usuarios_disp)

        # Livros
        layout.addWidget(QLabel("Selecione o livro:"))

        self.livros_disp = QComboBox()
        layout.addWidget(self.livros_disp)

        # Carrega os dados dos comboboxes
        self.carregar_usuarios()
        self.carregar_livros()

        btn_emprestar = QPushButton("Emprestar")
        btn_emprestar.clicked.connect(self.emprestar)
        layout.addWidget(btn_emprestar)

        btn_devolver = QPushButton("Devolver")
        btn_devolver.clicked.connect(self.devolver)
        layout.addWidget(btn_devolver)

         # Tabela de empréstimos
        self.tabela = QTableWidget()
        layout.addWidget(self.tabela)

        # Botão atualizar
        btn_atualizar = QPushButton("Atualizar")
        btn_atualizar.clicked.connect(self.carregar)
        layout.addWidget(btn_atualizar)

        self.setLayout(layout)

        self.carregar()

    def carregar_usuarios(self):
        self.usuarios_disp.clear()

        usuarios = self.controller.usuario_controller.listar_todos()

        for usuario in usuarios:
            self.usuarios_disp.addItem(
                usuario[1],  # nome
                usuario[0]   # id
            )

    def carregar_livros(self):
        self.livros_disp.clear()

        livros = self.controller.livro_controller.listar_todos()

        for livro in livros:
            titulo = livro[1]
            disponivel = livro[5]

            texto = f"{titulo} ({disponivel} disponíveis)"

            self.livros_disp.addItem(
                texto,
                livro[0]
            )

    def carregar(self):
        dados = self.controller.listar_todos()

        self.tabela.setRowCount(len(dados))
        self.tabela.setColumnCount(7)

        self.tabela.setHorizontalHeaderLabels([
            "ID",
            "Usuário",
            "Livro",
            "Data Empréstimo",
            "Devolução Prevista",
            "Devolução Real",
            "Status"
        ])

        for linha, registro in enumerate(dados):
            for col, valor in enumerate(registro):
                self.tabela.setItem(
                    linha,
                    col,
                    QTableWidgetItem(str(valor))
                )
    def emprestar(self):
        usuario_id = self.usuarios_disp.currentData()
        livro_id = self.livros_disp.currentData()

        data_emp = date.today()
        data_prev = date.today() + timedelta(days=7)

        ok, msg = self.controller.emprestar(
            usuario_id,
            livro_id,
            data_emp,
            data_prev
        )

        if ok:
            QMessageBox.information(
                self,
                "Sucesso",
                msg
            )

            self.carregar()
            self.carregar_livros()

        else:
            QMessageBox.warning(
                self,
                "Empréstimo não realizado",
                msg
            )

    def devolver(self):
        linha = self.tabela.currentRow()

        if linha < 0:
            QMessageBox.warning(
                self,
                "Aviso",
                "Selecione um empréstimo."
            )
            return

        emprestimo_id = int(
            self.tabela.item(linha, 0).text()
        )

        ok, msg = self.controller.devolver(
            emprestimo_id
        )

        if ok:
            QMessageBox.information(
                self,
                "Sucesso",
                msg
            )

            self.carregar()
            self.carregar_livros()

        else:
            QMessageBox.warning(
                self,
                "Erro",
                msg
            )