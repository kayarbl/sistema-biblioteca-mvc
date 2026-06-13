from PySide6.QtWidgets import QApplication
from views.main_window import MainView
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainView()
    janela.show()
    sys.exit(app.exec())
