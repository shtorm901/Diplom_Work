from src.editWin import Ui_MainWindow
from PyQt6 import QtWidgets
from settings import Base
import sqlite3


class EditForm(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tableWidget.hide()
        self.listWidget.show()
        self.label_4.hide()
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_8.hide()
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.lineEdit_5.hide()

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
        con, cur = self.printData()
        if (item.text() == "Users"):
            self.label_4.setText("Users")
            self.label.show()
            self.label.setText("Login")
            self.label_2.show()
            self.label_2.setText("Password")
            self.label_3.hide()
            self.label_5.show()
            self.label_5.setText("New")
            self.label_6.show()
            self.label_6.setText("Old")
            self.label_8.show()
            self.label_8.setText("Id")
            self.lineEdit.show()
            self.lineEdit_2.show()
            self.lineEdit_3.hide()
            self.lineEdit_5.show()
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
            self.label.show()
            self.label.setText("Name")
            self.label_2.show()
            self.label_2.setText("Surname")
            self.label_3.show()
            self.label_3.setText("Post_id")
            self.label_5.show()
            self.label_5.setText("New")
            self.label_6.show()
            self.label_6.setText("Old")
            self.label_8.show()
            self.label_8.setText("Id")
            self.lineEdit.show()
            self.lineEdit_2.show()
            self.lineEdit_3.show()
            self.lineEdit_5.show()
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
            self.label.show()
            self.label.setText("Name")
            self.label_2.show()
            self.label_2.setText("Salary")
            self.label_3.hide()
            self.label_5.show()
            self.label_5.setText("New")
            self.label_6.show()
            self.label_6.setText("Old")
            self.label_8.show()
            self.label_8.setText("Id")
            self.lineEdit.show()
            self.lineEdit_2.show()
            self.lineEdit_3.hide()
            self.lineEdit_5.show()
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
            self.label.show()
            self.label.setText("Menu_id")
            self.label_2.show()
            self.label_2.setText("User_id")
            self.label_3.hide()
            self.label_5.show()
            self.label_5.setText("New")
            self.label_6.show()
            self.label_6.setText("Old")
            self.label_8.show()
            self.label_8.setText("Id")
            self.lineEdit.show()
            self.lineEdit_2.show()
            self.lineEdit_3.hide()
            self.lineEdit_5.show()
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
            self.label.show()
            self.label.setText("Product Name")
            self.label_2.show()
            self.label_2.setText("Product Price")
            self.label_3.hide()
            self.label_5.show()
            self.label_5.setText("New")
            self.label_6.show()
            self.label_6.setText("Old")
            self.label_8.show()
            self.label_8.setText("Id")
            self.lineEdit.show()
            self.lineEdit_2.show()
            self.lineEdit_3.hide()
            self.lineEdit_5.show()
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
            self.label.show()
            self.label.setText("Cafe Name")
            self.label_2.show()
            self.label_2.setText("Cafe Address")
            self.label_3.show()
            self.label_3.setText("Cafe Telephone_Number")
            self.label_5.show()
            self.label_5.setText("New")
            self.label_6.show()
            self.label_6.setText("Old")
            self.label_8.show()
            self.lineEdit.show()
            self.lineEdit_2.show()
            self.lineEdit_3.show()
            self.lineEdit_5.show()
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
        ids = self.lineEdit_5.text()
        if self.tableName == "Users":
            login = self.lineEdit.text()
            password = self.lineEdit_2.text()
            try:
                cur.execute("UPDATE Users SET (name, password) = (?, ?) WHERE id == (?)", (login, password, ids))
                QtWidgets.QMessageBox.information(None, "Информация", "Пользователь был обновлен")
                con.commit()
                self.cancel()
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Пользователь не найден, проверьте данные и попробуйте снова")

        if self.tableName == "Workers":
            name = self.lineEdit.text()
            surname = self.lineEdit_2.text()
            post_id = self.lineEdit_3.text()
            try:
                cur.execute("UPDATE Workers SET (name, surname, post_id) = (?, ?, ?) WHERE id == (?)", (name, surname, post_id, ids))
                QtWidgets.QMessageBox.information(None, "Информация", "Работник был обновлен")
                con.commit()
                self.cancel()
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Работник не найден, проверьте данные и попробуйте снова")

        if self.tableName == "Post":
            name = self.lineEdit.text()
            salary = self.lineEdit_2.text()
            try:
                cur.execute("UPDATE Post SET (name, salary) = (?, ?) WHERE id == (?)", (name, salary, ids))
                QtWidgets.QMessageBox.information(None, "Информация", "Должность была обновлена")
                con.commit()
                self.cancel()
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Должность не найдена, проверьте данные и попробуйте снова")

        if self.tableName == "Orders":
            menu_id = self.lineEdit.text()
            user_id = self.lineEdit_2.text()
            try:
                cur.execute("UPDATE Orders SET (menu_id, user_id) = (?, ?) WHERE id == (?)", (menu_id, user_id, ids))
                QtWidgets.QMessageBox.information(None, "Информация", "Заказ был обновлен")
                con.commit()
                self.cancel()
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Заказ не найден, проверьте данные и попробуйте снова")

        if self.tableName == "Menu":
            name = self.lineEdit.text()
            price = self.lineEdit_2.text()
            try:
                cur.execute("UPDATE Menu SET (name, price) = (?, ?) WHERE id == (?)", (name, price, ids))
                QtWidgets.QMessageBox.information(None, "Информация", "Продукт был обновлен")
                con.commit()
                self.cancel()
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Продукт не найден, проверьте данные и попробуйте снова")

        if self.tableName == "Cafe":
            name = self.lineEdit.text()
            address = self.lineEdit_2.text()
            phone_number = self.lineEdit_5.text()
            try:
                cur.execute("UPDATE Cafe SET (name, address, telephone_number) = (?, ?, ?) WHERE id == (?)", (name, address, phone_number, ids))
                QtWidgets.QMessageBox.information(None, "Информация", "Заказ был обновлен")
                con.commit()
                self.cancel()
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Заказ не найден, проверьте данные и попробуйте снова")

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
        self.tableWidget.hide()
        self.listWidget.show()
        self.label_4.hide()
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_8.hide()
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.lineEdit_5.hide()
        self.listWidget.show()
        self.printData()