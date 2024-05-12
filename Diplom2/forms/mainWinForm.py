from src.mainWin import Ui_MainWindow
from .addWinForm import AddForm
from .editWinForm import EditForm
from .deleteWinForm import DeleteForm
from PyQt6 import QtWidgets


class MainForm(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.add)
        self.pushButton.clicked.connect(self.edit)
        self.pushButton_3.clicked.connect(self.delete)

    def add(self):
        self.addForm = AddForm()
        self.addForm.show()

    def delete(self):
        self.deleteForm = DeleteForm()
        self.deleteForm.show()

    def edit(self):
        self.editForm = EditForm()
        self.editForm.show()