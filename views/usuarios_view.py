from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QMessageBox
)
from controllers.usuario_controller import UsuarioController


class UsuariosView(QWidget):
    def __init__(self):
        super().__init__()

        self.controller = UsuarioController()

        self.setWindowTitle("Cadastro de Usuários")
        self.setMinimumWidth(600)

        layout = QVBoxLayout()

        
        self.input_nome = QLineEdit()
        self.input_email = QLineEdit()
        self.input_tel = QLineEdit()

        layout.addWidget(QLabel("Nome:"))
        layout.addWidget(self.input_nome)

        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.input_email)

        layout.addWidget(QLabel("Telefone:"))
        layout.addWidget(self.input_tel)

        btn_cadastrar = QPushButton("Cadastrar Usuário")
        btn_cadastrar.clicked.connect(self.cadastrar)
        layout.addWidget(btn_cadastrar)

        
        self.tabela = QTableWidget()
        layout.addWidget(self.tabela)

        btn_atualizar = QPushButton("Atualizar")
        btn_atualizar.clicked.connect(self.carregar)
        layout.addWidget(btn_atualizar)

        self.setLayout(layout)
        self.carregar()

    def cadastrar(self):
        nome = self.input_nome.text()
        email = self.input_email.text()
        telefone = self.input_tel.text()

        ok, msg = self.controller.cadastrar(
            nome,
            email,
            telefone
        )

        if ok:
            QMessageBox.information(self, "Sucesso", msg)
            self.input_nome.clear()
            self.input_email.clear()
            self.input_tel.clear()
            self.carregar()
        else:
            QMessageBox.warning(self, "Erro", msg)

    def carregar(self):
        dados = self.controller.listar_todos()

        self.tabela.setRowCount(len(dados))
        self.tabela.setColumnCount(5)
        self.tabela.setHorizontalHeaderLabels(
            ["ID", "Nome", "Email", "Telefone", "Data Cadastro"]
        )

        for linha, registro in enumerate(dados):
            for col, valor in enumerate(registro):
                self.tabela.setItem(linha, col, QTableWidgetItem(str(valor)))
