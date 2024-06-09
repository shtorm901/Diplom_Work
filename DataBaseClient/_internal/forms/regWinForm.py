from src.regWin import Ui_MainWindow
from PyQt6 import QtWidgets
from settings import Base
import sqlite3


class RegForm(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.OKButton.clicked.connect(self.createUser)
        self.CancelButton.clicked.connect(self.cancel)

    def createUser(self):
        login = self.Login.text()
        password = self.Password.text()
        con = sqlite3.connect(Base)
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO Users(name, password) VALUES (?, ?)", (login, password))
            con.commit()
            QtWidgets.QMessageBox.information(None, "Информация", "Пользователь был добавлен")
            from .logWinForm import LogForm
            self.logWin = LogForm()
            self.logWin.show()
            self.close()
        except Exception:
            QtWidgets.QMessageBox.warning(None, "Ошибка", "Ошибка в данных")

    def cancel(self):
        self.Login.clear()
        self.Password.clear()
        QtWidgets.QMessageBox.information(None, "Информация", "Поля были очищены")