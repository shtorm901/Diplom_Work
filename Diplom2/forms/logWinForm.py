from src.logWin import Ui_MainWindow
from PyQt6 import QtWidgets
from settings import Base
import sqlite3

class LogForm(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.OKButton.clicked.connect(self.login)
        self.CancelButton.clicked.connect(self.cancel)

    def login(self):
        login = self.Login.text()
        password = self.Password.text()
        con = sqlite3.connect(Base)
        cur = con.cursor()

        try:
            cur.execute("SELECT * FROM Users WHERE (name, password) == (?, ?)", (login, password))
            for row in cur.fetchone():
                from .mainWinForm import MainForm
                self.mainWin = MainForm()
                self.mainWin.show()
                self.close()
                QtWidgets.QMessageBox.information(None, "Информация", "Успешный вход")
                break
        except TypeError:
            QtWidgets.QMessageBox.warning(None, "Ошибка", "Проверьте данные и попробуйте снова")

    def cancel(self):
        self.Login.clear()
        self.Password.clear()
        QtWidgets.QMessageBox.information(None, "Информация", "Поля были очищены")