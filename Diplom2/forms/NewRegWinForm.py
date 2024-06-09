from src.NRegWin import Ui_MainWindow
from PyQt6 import QtWidgets
import sqlite3
from settings import Base


class NewReg(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label.setText("Login")
        self.label_2.setText("Password")
        self.pushButton.setText("Зарегистрироваться")
        self.actionLoginWindow.triggered.connect(self.LogIN)

        self.pushButton.clicked.connect(self.Create)

    def LogIN(self):
        from .NewLogWinForm import NLog
        self.LogWindow = NLog()
        self.LogWindow.show()
        self.close()

    def Create(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        con = sqlite3.connect(Base)
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO Users (name, password) VALUES (?, ?)", (login, password))
            con.commit()
            QtWidgets.QMessageBox.information(None, "Информация", "Пользователь был добавлен")
            from .NewLogWinForm import NLog
            self.LogWindow = NLog()
            self.LogWindow.show()
            self.close()
        except Exception:
            QtWidgets.QMessageBox.warning(None, "Ошибка", "Ошибка в данных")