from src.deleteWin import Ui_MainWindow
from PyQt6 import QtWidgets
from settings import Base
import sqlite3


class DeleteForm(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.tableWidget.hide()
        self.listWidget.show()
        self.OK.hide()
        self.Cancel.hide()

        self.printData()

        self.OK.clicked.connect(self.add)
        self.Cancel.clicked.connect(self.cancel)

    def printData(self):
        con = sqlite3.connect(Base)
        cur = con.cursor()

        query = "SELECT name FROM sqlite_master WHERE type =='table'"
        for row in cur.execute(query):
            self.listWidget.addItems(row)
            self.listWidget.itemClicked.connect(self.selectedTable)

        return con, cur

    def selectedTable(self, item):
        self.listWidget.hide()
        self.tableWidget.show()
        self.OK.show()
        self.Cancel.show()
        con, cur = self.printData()
        if (item.text() == "Users"):
            self.label_4.setText("Users")
            self.lineEdit.show()
            self.label.show()
            self.label.setText("Id")
            self.lineEdit_2.hide()
            self.label_2.hide()
            self.label_2.setText("Password")
            self.lineEdit_3.hide()
            self.label_3.hide()
            self.tableName = self.label_4.text()
            query = "SELECT * FROM Users"
            self.tableWidget.setRowCount(50)
            tablerow = 0
            for row in cur.execute(query):
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                tablerow += 1
        if (item.text() == "Workers"):
            self.label_4.setText("Workers")
            self.lineEdit.show()
            self.label.show()
            self.label.setText("Id")
            self.lineEdit_2.hide()
            self.label_2.hide()
            self.lineEdit_3.hide()
            self.label_3.hide()
            query = "SELECT * FROM Workers"
            self.tableWidget.setRowCount(50)
            tablerow = 0
            for row in cur.execute(query):
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                tablerow += 1
        if (item.text() == "Post"):
            self.label_4.setText("Post")
            self.lineEdit.show()
            self.lineEdit_2.hide()
            self.lineEdit_3.hide()
            self.label.show()
            self.label.setText("Id")
            self.label_2.hide()
            self.label_3.hide()
            query = "SELECT * FROM Post"
            self.tableWidget.setRowCount(50)
            tablerow = 0
            for row in cur.execute(query):
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                tablerow += 1
        if (item.text() == "Orders"):
            self.label_4.setText("Orders")
            self.lineEdit.show()
            self.label.show()
            self.label.setText("Id")
            self.lineEdit_2.hide()
            self.label_2.hide()
            self.lineEdit_3.hide()
            self.label_3.hide()
            query = "SELECT * FROM Orders"
            self.tableWidget.setRowCount(50)
            tablerow = 0
            for row in cur.execute(query):
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                tablerow += 1
        if (item.text() == "Menu"):
            self.label_4.setText("Menu")
            self.lineEdit.show()
            self.label.show()
            self.label.setText("Id")
            self.lineEdit_2.hide()
            self.label_2.hide()
            self.lineEdit_3.hide()
            self.label_3.hide()
            query = "SELECT * FROM Menu"
            self.tableWidget.setRowCount(50)
            tablerow = 0
            for row in cur.execute(query):
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                tablerow += 1
        if (item.text() == "Cafe"):
            self.label_4.setText("Cafe")
            self.lineEdit.show()
            self.label.show()
            self.label.setText("Id")
            self.lineEdit_2.hide()
            self.label_2.hide()
            self.lineEdit_3.hide()
            self.label_3.hide()
            query = "SELECT * FROM Cafe"
            self.tableWidget.setRowCount(50)
            tablerow = 0
            for row in cur.execute(query):
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                tablerow += 1

    def add(self):
        con, cur = self.printData()
        self.tableName = self.label_4.text()
        ids = self.lineEdit.text()
        if (self.tableName == "Users"):
            try:
                cur.execute("SELECT * FROM Users WHERE id = ?", (ids))
                for row in cur.fetchone():
                    cur.execute("DELETE FROM Users WHERE id = ?", (ids))
                    QtWidgets.QMessageBox.information(None, "Информация", "Пользователь был удален")
                    con.commit()
                    self.cancel()
                    break
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Пользователь не найден, проверьте данные и попробуйте снова")
        if (self.tableName == "Workers"):
            try:
                cur.execute("SELECT * FROM Workers WHERE id = ?", (ids))
                for row in cur.fetchone():
                    cur.execute("DELETE FROM Workers WHERE id = ?", (ids))
                    QtWidgets.QMessageBox.information(None, "Информация", "Работник был удален")
                    con.commit()
                    self.cancel()
                    break
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Работник не найден, проверьте данные и попробуйте снова")
        if (self.tableName == "Menu"):
            try:
                cur.execute("SELECT * FROM Menu WHERE id = ?", (ids))
                for row in cur.fetchone():
                    cur.execute("DELETE FROM Menu WHERE id = ?", (ids))
                    QtWidgets.QMessageBox.information(None, "Информация", "Элемент меню был удален")
                    con.commit()
                    self.cancel()
                    break
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Элемент меню не найден, проверьте данные и попробуйте снова")
        if (self.tableName == "Post"):
            try:
                cur.execute("SELECT * FROM Post WHERE id = ?", (ids))
                for row in cur.fetchone():
                    cur.execute("DELETE FROM Post WHERE id = ?", (ids))
                    QtWidgets.QMessageBox.information(None, "Информация", "Должность была удален")
                    con.commit()
                    self.cancel()
                    break
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Должность не найдена, проверьте данные и попробуйте снова")
        if (self.tableName == "Orders"):
            try:
                cur.execute("SELECT * FROM Orders WHERE id = ?", (ids))
                for row in cur.fetchone():
                    cur.execute("DELETE FROM Orders WHERE id = ?", (ids))
                    QtWidgets.QMessageBox.information(None, "Информация", "Заказ был удален")
                    con.commit()
                    self.cancel()
                    break
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Заказ не найден, проверьте данные и попробуйте снова")
        if (self.tableName == "Cafe"):
            try:
                cur.execute("SELECT * FROM Cafe WHERE id = ?", (ids))
                for row in cur.fetchone():
                    cur.execute("DELETE FROM Cafe WHERE id = ?", (ids))
                    QtWidgets.QMessageBox.information(None, "Информация", "Кафе было удален")
                    con.commit()
                    self.cancel()
                    break
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Кафе не найдено, проверьте данные и попробуйте снова")

    def cancel(self):
        QtWidgets.QMessageBox.information(None, "Информация", "Поля были очищены")
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.tableWidget.clear()
        self.listWidget.clear()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.tableWidget.hide()
        self.listWidget.show()
        self.printData()