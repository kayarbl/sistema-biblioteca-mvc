from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from views.livros_view import LivrosView
from views.usuarios_view import UsuariosView
from views.emprestimo_view import EmprestimoView


class MainView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema Biblioteca - MVC")
        self.setMinimumWidth(400)

        layout = QVBoxLayout()

        
        btn_livros = QPushButton("Gerenciar Livros")
        btn_livros.clicked.connect(self.abrir_livros)
        layout.addWidget(btn_livros)

        
        btn_usuarios = QPushButton("Gerenciar Usuários")
        btn_usuarios.clicked.connect(self.abrir_usuarios)
        layout.addWidget(btn_usuarios)

       
        btn_emprestimos = QPushButton("Gerenciar Empréstimos")
        btn_emprestimos.clicked.connect(self.abrir_emprestimos)
        layout.addWidget(btn_emprestimos)

        self.setLayout(layout)

    
    def abrir_livros(self):
        self.janela_livros = LivrosView()
        self.janela_livros.show()

    def abrir_usuarios(self):
        self.janela_usuarios = UsuariosView()
        self.janela_usuarios.show()

    def abrir_emprestimos(self):
        self.janela_emprestimos = EmprestimoView()
        self.janela_emprestimos.show()
