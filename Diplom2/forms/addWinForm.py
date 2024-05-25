from src.addWin import Ui_MainWindow
from PyQt6 import QtWidgets
from settings import Base
import sqlite3


class AddForm(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.OK.hide()
        self.Cancel.hide()
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.tableWidget.hide()
        self.listWidget.show()

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
        if(item.text() == "Users"):
            self.label_4.setText("Users")
            self.lineEdit.show()
            self.label.show()
            self.label.setText("Login")
            self.lineEdit_2.show()
            self.label_2.show()
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
        if(item.text() == "Workers"):
            self.label_4.setText("Workers")
            self.lineEdit.show()
            self.label.show()
            self.label.setText("Name")
            self.lineEdit_2.show()
            self.label_2.show()
            self.label_2.setText("Surname")
            self.lineEdit_3.show()
            self.label_3.show()
            self.label_3.setText("Post_id")
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
            self.lineEdit_2.show()
            self.lineEdit_3.hide()
            self.label.show()
            self.label.setText("Name")
            self.label_2.show()
            self.label_2.setText("Salary")
            self.label_3.hide()
            query = "SELECT * FROM Post"
            self.tableWidget.setRowCount(50)
            tablerow = 0
            for row in cur.execute(query):
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                tablerow += 1
        if(item.text() == "Orders"):
            self.label_4.setText("Orders")
            self.lineEdit.show()
            self.label.show()
            self.label.setText("Menu_id")
            self.lineEdit_2.show()
            self.label_2.show()
            self.label_2.setText("user_id")
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
        if(item.text() == "Menu"):
            self.label_4.setText("Menu")
            self.lineEdit.show()
            self.label.show()
            self.label.setText("Product Name")
            self.lineEdit_2.show()
            self.label_2.show()
            self.label_2.setText("Product Price")
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
        if(item.text() == "Cafe"):
            self.label_4.setText("Cafe")
            self.lineEdit.show()
            self.label.show()
            self.label.setText("Cafe Name")
            self.lineEdit_2.show()
            self.label_2.show()
            self.label_2.setText("Cafe Address")
            self.lineEdit_3.show()
            self.label_3.show()
            self.label_3.setText("Cafe Telephone_Number")
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
        if(self.tableName == "Users"):
            try:
                login = self.lineEdit.text()
                password = self.lineEdit_2.text()
                cur.execute("INSERT INTO Users (name, password) VALUES (?, ?)", (login, password))
                QtWidgets.QMessageBox.information(None, "Информация", "Был добавлен новый пользователь")
                con.commit()
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
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Ошибка в данных")
        if(self.tableName == "Workers"):
            try:
                name = self.lineEdit.text()
                surname = self.lineEdit_2.text()
                post_id = self.lineEdit_3.text()
                cur.execute("INSERT INTO Workers (name, surname, post_id) VALUES (?, ?, ?)", (name, surname, post_id))
                QtWidgets.QMessageBox.information(None, "Информация", "Был добавлен новый работник")
                con.commit()
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
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Ошибка в данных")
        if(self.tableName == "Post"):
            try:
                name = self.lineEdit.text()
                salary = self.lineEdit_2.text()
                cur.execute("INSERT INTO Post (name, salary) VALUES (?, ?)", (name, salary))
                QtWidgets.QMessageBox.information(None, "Информация", "Была добавлена новая должность")
                con.commit()
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
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Ошибка в данных")
        if(self.tableName == "Orders"):
            try:
                menu_id = self.lineEdit.text()
                user_id = self.lineEdit_2.text()
                cur.execute("INSERT INTO Orders (menu_id, user_id) VALUES (?, ?)", (menu_id, user_id))
                QtWidgets.QMessageBox.information(None, "Информация", "Был добавлен новый заказ")
                con.commit()
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
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Ошибка в данных")
        if(self.tableName == "Menu"):
            try:
                name = self.lineEdit.text()
                price = self.lineEdit_2.text()
                cur.execute("INSERT INTO Menu (name, price) VALUES (?, ?)", (name, price))
                QtWidgets.QMessageBox.information(None, "Информация", "Был добавлен новый продукт")
                con.commit()
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
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Ошибка в данных")
        if(self.tableName == "Cafe"):
            try:
                name = self.lineEdit.text()
                address = self.lineEdit_2.text()
                telephone_number = self.lineEdit_3.text()
                cur.execute("INSERT INTO Cafe (name, address, telephone_number) VALUES (?, ?, ?)", (name, address, telephone_number))
                QtWidgets.QMessageBox.information(None, "Информация", "Было добавлено новое кафе")
                con.commit()
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
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Ошибка в данных")

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