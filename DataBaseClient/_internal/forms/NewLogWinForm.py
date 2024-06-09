from src.NLogWin import Ui_MainWindow
from .newMainWinForm import MainWin
from PyQt6 import QtWidgets
from settings import Base
import sqlite3


class NLog(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label.setText("Login")
        self.label_2.setText("Password")
        self.pushButton.setText("Войти")

        self.pushButton.clicked.connect(self.login)

    def login(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        con = sqlite3.connect(Base)
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM Users WHERE (name, password) == (?, ?)", (login, password))
            for row in cur.fetchone():
                QtWidgets.QMessageBox.information(None, "Информация", "Успешный вход")
                self.MainWindow = MainWin()
                self.MainWindow.show()
                self.close()
                break
        except Exception:
            QtWidgets.QMessageBox.warning(None, "Ошибка", "Проверьте данные и попробуйте снова")