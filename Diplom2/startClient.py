from src import base_worker
from forms.NewRegWinForm import NewReg
from PyQt6 import QtWidgets
from settings import Base
import sys

base_worker.set_base_path(Base)

if not base_worker.base_check():
    base_worker.create_base('base.sql')


if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   startWin = NewReg()
   startWin.show()
   app.exec()