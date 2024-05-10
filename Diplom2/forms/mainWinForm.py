from src.mainWin import Ui_MainWindow
from PyQt6 import QtWidgets
from settings import Base
import sqlite3


class MainForm(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.add)
        self.pushButton.clicked.connect(self.edit)
        self.pushButton_3.clicked.connect(self.delete)

        self.printTable()

    def printTable(self):
        con = sqlite3.connect(Base)
        cur = con.cursor()

        query = "SELECT name FROM sqlite_master WHERE type == 'table'"
        for row in cur.execute(query):
            self.listWidget.addItems(row)

        return con, cur

    def add(self):
        from .addWinForm import AddForm
        self.addWin = AddForm()
        self.addWin.show()
        self.close()

    def edit(self):
        from .editWinForm import EditForm
        self.editWin = EditForm()
        self.editWin.show()
        self.close()

    def delete(self):
        from .deleteWinForm import DeleteForm
        self.deleteWin = DeleteForm()
        self.deleteWin.show()
        self.close()