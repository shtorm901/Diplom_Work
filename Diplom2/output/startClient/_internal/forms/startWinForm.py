from src.startWin import Ui_MainWindow
from .regWinForm import RegForm
from .logWinForm import LogForm
from PyQt6 import QtWidgets


class StartForm(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.registration)
        self.pushButton_2.clicked.connect(self.login)

    def registration(self):
        self.regWin = RegForm()
        self.regWin.show()
        self.close()

    def login(self):
        self.logWin = LogForm()
        self.logWin.show()
        self.close()