from src.NewMainWin import Ui_MainWindow
from PyQt6 import QtWidgets
from .NewRegWinForm import NewReg
from .NewLogWinForm import NLog
from settings import Base
import sqlite3


class MainWin(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.printData()

        self.logWin = NLog()
        self.regWin = NewReg()


        self.tableWidget.hide()
        self.DeleteButon.hide()
        self.EditButton.hide()
        self.AddButton.hide()
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.label_8.hide()
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.lineEdit_4.hide()
        self.lineEdit_5.hide()
        self.lineEdit_6.hide()
        self.lineEdit_7.hide()
        self.lineEdit_8.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.actionLogin.triggered.connect(self.Aut)
        self.actionRegistration.triggered.connect(self.Reg)
        self.actionMainWindow.triggered.connect(self.Main)

        self.pushButton.clicked.connect(self.Add)
        self.pushButton_2.clicked.connect(self.Edit)
        self.pushButton_3.clicked.connect(self.Delete)

        self.AddButton.clicked.connect(self.AddRow)
        self.DeleteButon.clicked.connect(self.DeleteRow)
        self.EditButton.clicked.connect(self.EditRow)

    def Aut(self):
        self.logWin.show()

    def Reg(self):
        self.regWin.show()

    def Main(self):
        self.DeleteButon.hide()
        self.AddButton.hide()
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.label_8.hide()
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.lineEdit_4.hide()
        self.lineEdit_5.hide()
        self.lineEdit_6.hide()
        self.lineEdit_7.hide()
        self.lineEdit_8.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.listWidget.clear()
        self.tableWidget.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.listWidget.show()
        self.printData()

    def printData(self):
        con = sqlite3.connect(Base)
        cur = con.cursor()

        query = "Select name from sqlite_master WHERE type == 'table'"
        for row in cur.execute(query):
            self.listWidget.addItems(row)
            self.listWidget.itemClicked.connect(self.selectTable)
            self.tableWidget.clear()

        return con, cur

    def Add(self):
        self.EditButton.hide()
        self.DeleteButon.hide()
        self.AddButton.setText("Add")
        self.AddButton.show()
        self.label.show()
        self.label_2.show()
        self.label_3.show()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.label_8.hide()
        self.lineEdit.show()
        self.lineEdit_2.show()
        self.lineEdit_3.show()
        self.lineEdit_4.hide()
        self.lineEdit_5.hide()
        self.lineEdit_6.hide()
        self.lineEdit_7.hide()
        self.lineEdit_8.hide()
        if(self.table_name == "Users"):
            self.label.setText("Login")
            self.label_2.setText("Password")
            self.label_3.hide()
            self.lineEdit_3.hide()
        if(self.table_name == "Workers"):
            self.label_2.show()
            self.label_3.show()
            self.lineEdit_2.show()
            self.lineEdit_3.show()
            self.label.setText("Name")
            self.label_2.setText("Surname")
            self.label_3.setText("Post_Id")
        if(self.table_name == "Post"):
            self.label_2.show()
            self.label_3.hide()
            self.lineEdit_2.show()
            self.lineEdit_3.hide()
            self.label.setText("Name")
            self.label_2.setText("Salary")
        if (self.table_name == "Menu"):
            self.label_2.show()
            self.label_3.hide()
            self.lineEdit_2.show()
            self.lineEdit_3.hide()
            self.label.setText("Name")
            self.label_2.setText("Price")
        if (self.table_name == "Cafe"):
            self.label_2.show()
            self.label_3.show()
            self.lineEdit_2.show()
            self.lineEdit_3.show()
            self.label.setText("Name")
            self.label_2.setText("Adress")
            self.label_3.setText("Telephone_Number")
        if (self.table_name == "Orders"):
            self.label_2.show()
            self.label_3.hide()
            self.lineEdit_2.show()
            self.lineEdit_3.hide()
            self.label.setText("Menu_Id")
            self.label_2.setText("User_Id")
    def AddRow(self):
        con, cur = self.printData()
        if (self.table_name == "Users"):
            login = self.lineEdit.text()
            password = self.lineEdit_2.text()
            try:
                cur.execute("INSERT INTO Users (name, password) VALUES (?, ?)", (login, password))
                QtWidgets.QMessageBox.information(None, "Информация", "Пользователь был добавлен")
                con.commit()
                query = "SELECT * FROM Users"
                self.tableWidget.setRowCount(50)
                tablerow = 0
                for row in cur.execute(query):
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                    tablerow += 1
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Ошибка в данных")
        if (self.table_name == "Workers"):
            Name = self.lineEdit.text()
            Surname = self.lineEdit_2.text()
            Post_Id = self.lineEdit_3.text()
            try:
                cur.execute("INSERT INTO Workers (name, surname, post_id) VALUES (?, ?, ?)", (Name, Surname, Post_Id))
                QtWidgets.QMessageBox.information(None, "Информация", "Работник добавлен")
                con.commit()
                query = "SELECT * FROM Workers"
                self.tableWidget.setRowCount(50)
                tablerow = 0
                for row in cur.execute(query):
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    tablerow += 1
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Ошибка в данных")

        if(self.table_name == "Post"):
            Name = self.lineEdit.text()
            Salary = self.lineEdit_2.text()
            try:
                cur.execute("INSERT INTO Post (name, salary) VALUES (?, ?)", (Name, Salary))
                QtWidgets.QMessageBox.information(None, "Информация", "Должность была добавлена")
                con.commit()
                query = "SELECT * FROM Post"
                self.tableWidget.setRowCount(50)
                tablerow = 0
                for row in cur.execute(query):
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    tablerow += 1
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Ошибка в данных")

        if (self.table_name == "Menu"):
            Name = self.lineEdit.text()
            Price = self.lineEdit_2.text()
            try:
                cur.execute("INSERT INTO Menu (name, price) VALUES (?, ?)", (Name, Price))
                QtWidgets.QMessageBox.information(None, "Информация", "Предмет был добавлен")
                con.commit()
                query = "SELECT * FROM Menu"
                self.tableWidget.setRowCount(50)
                tablerow = 0
                for row in cur.execute(query):
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    tablerow += 1
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Ошибка в данных")

        if (self.table_name == "Cafe"):
            Name = self.lineEdit.text()
            Address = self.lineEdit_2.text()
            Phone = self.lineEdit_3.text()
            try:
                cur.execute("INSERT INTO Cafe (name, address, telephone_number) VALUES (?, ?, ?)", (Name, Address, Phone))
                QtWidgets.QMessageBox.information(None, "Информация", "Кафе было добавлено")
                con.commit()
                query = "SELECT * FROM Cafe"
                self.tableWidget.setRowCount(50)
                tablerow = 0
                for row in cur.execute(query):
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                    tablerow += 1
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Ошибка в данных")

        if (self.table_name == "Orders"):
            Menu_Id = self.lineEdit.text()
            User_Id = self.lineEdit_2.text()
            try:
                cur.execute("INSERT INTO Orders (menu_id, user_id) VALUES (?, ?)", (Menu_Id, User_Id))
                QtWidgets.QMessageBox.information(None, "Информация", "Заказ был добавлен")
                con.commit()
                query = "SELECT * FROM Orders"
                self.tableWidget.setRowCount(50)
                tablerow = 0
                for row in cur.execute(query):
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                    tablerow += 1
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Ошибка в данных")

    def Delete(self):
        self.EditButton.hide()
        self.AddButton.hide()
        self.DeleteButon.setText("Delete")
        self.DeleteButon.show()
        self.label.show()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.label_8.hide()
        self.lineEdit.show()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.lineEdit_4.hide()
        self.lineEdit_5.hide()
        self.lineEdit_6.hide()
        self.lineEdit_7.hide()
        self.lineEdit_8.hide()
        self.label.setText("Id")

    def DeleteRow(self):
        con, cur = self.printData()
        Id = self.lineEdit.text()
        if(self.table_name == "Users"):
            try:
                cur.execute("SELECT * FROM Users WHERE id = ?", (Id))
                for row in cur.fetchone():
                    cur.execute("DELETE FROM Users WHERE id = ?", (Id))
                    QtWidgets.QMessageBox.information(None, "Информация", "Пользователь удален")
                    con.commit()
                    query = "SELECT * FROM Users"
                    self.tableWidget.setRowCount(50)
                    tablerow = 0
                    for row in cur.execute(query):
                        self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                        self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                        tablerow += 1
                    self.lineEdit.clear()
                    break
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Пользователь не найден")

        if (self.table_name == "Workers"):
            try:
                cur.execute("SELECT * FROM Workers WHERE id = ?", (Id))
                for row in cur.fetchone():
                    cur.execute("DELETE FROM Workers WHERE id = ?", (Id))
                    QtWidgets.QMessageBox.information(None, "Информация", "Работник удален")
                    con.commit()
                    query = "SELECT * FROM Workers"
                    self.tableWidget.setRowCount(50)
                    tablerow = 0
                    for row in cur.execute(query):
                        self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                        self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                        self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                        tablerow += 1
                    self.lineEdit.clear()
                    break
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Работник не найден")

        if (self.table_name == "Post"):
            try:
                cur.execute("SELECT * FROM Post WHERE id = ?", (Id))
                for row in cur.fetchone():
                    cur.execute("DELETE FROM Post WHERE id = ?", (Id))
                    QtWidgets.QMessageBox.information(None, "Информация", "Должность удалена")
                    con.commit()
                    query = "SELECT * FROM Post"
                    self.tableWidget.setRowCount(50)
                    tablerow = 0
                    for row in cur.execute(query):
                        self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                        self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                        tablerow += 1
                    self.lineEdit.clear()
                    break
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Должность не найдена")

        if (self.table_name == "Cafe"):
            try:
                cur.execute("SELECT * FROM Cafe WHERE id = ?", (Id))
                for row in cur.fetchone():
                    cur.execute("DELETE FROM Cafe WHERE id = ?", (Id))
                    QtWidgets.QMessageBox.information(None, "Информация", "Кафе удалено")
                    con.commit()
                    query = "SELECT * FROM Cafe"
                    self.tableWidget.setRowCount(50)
                    tablerow = 0
                    for row in cur.execute(query):
                        self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                        self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                        self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                        tablerow += 1
                    self.lineEdit.clear()
                    break
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Кафе не найдено")

        if (self.table_name == "Orders"):
            try:
                cur.execute("SELECT * FROM Orders WHERE id = ?", (Id))
                for row in cur.fetchone():
                    cur.execute("DELETE FROM Orders WHERE id = ?", (Id))
                    QtWidgets.QMessageBox.information(None, "Информация", "Заказ удален")
                    con.commit()
                    query = "SELECT * FROM Orders"
                    self.tableWidget.setRowCount(50)
                    tablerow = 0
                    for row in cur.execute(query):
                        self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                        self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                        self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                        tablerow += 1
                    self.lineEdit.clear()
                    break
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Заказ не найден")

        if (self.table_name == "Menu"):
            try:
                cur.execute("SELECT * FROM Menu WHERE id = ?", (Id))
                for row in cur.fetchone():
                    cur.execute("DELETE FROM Menu WHERE id = ?", (Id))
                    QtWidgets.QMessageBox.information(None, "Информация", "Предмет удален")
                    con.commit()
                    query = "SELECT * FROM Menu"
                    self.tableWidget.setRowCount(50)
                    tablerow = 0
                    for row in cur.execute(query):
                        self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                        self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                        tablerow += 1
                    self.lineEdit.clear()
                    break
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Предмет не найден")

    def Edit(self):
        self.AddButton.hide()
        self.DeleteButon.hide()
        self.EditButton.setText("Edit")
        self.EditButton.show()
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_8.show()
        self.label_5.show()
        self.label_6.show()
        self.label_7.show()
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.lineEdit_4.hide()
        self.lineEdit_8.show()
        self.lineEdit_7.show()
        self.lineEdit_6.show()
        self.lineEdit_5.show()
        if(self.table_name == "Users"):
            self.label_8.setText("Id")
            self.label_5.setText("name")
            self.label_6.setText("Password")
            self.label_7.hide()
            self.lineEdit_7.hide()
        if(self.table_name == "Workers"):
            self.label_8.setText("Id")
            self.label_5.setText("Name")
            self.label_6.setText("Surname")
            self.label_7.show()
            self.lineEdit_7.show()
            self.label_7.setText("Post_Id")
        if(self.table_name == "Post"):
            self.label_8.setText("Id")
            self.label_5.setText("Name")
            self.label_6.setText("Salary")
            self.label_7.hide()
            self.lineEdit_7.hide()
        if (self.table_name == "Menu"):
            self.label_8.setText("Id")
            self.label_5.setText("Name")
            self.label_6.setText("Price")
            self.label_7.hide()
            self.lineEdit_7.hide()
        if (self.table_name == "Orders"):
            self.label_8.setText("Id")
            self.label_5.setText("User_Id")
            self.label_6.setText("Menu_Id")
            self.label_7.hide()
            self.lineEdit_7.hide()
        if (self.table_name == "Cafe"):
            self.label_8.setText("Id")
            self.label_5.setText("Name")
            self.label_6.setText("Address")
            self.label_7.show()
            self.lineEdit_7.show()
            self.label_7.setText("Telephone_Number")

    def EditRow(self):
        con, cur = self.printData()
        Id = self.lineEdit_8.text()
        if(self.table_name == "Users"):
            Login = self.lineEdit_5.text()
            Password = self.lineEdit_6.text()
            try:
                cur.execute("SELECT * FROM Users WHERE id = ?", (Id))
                for row in cur.fetchone():
                    cur.execute("UPDATE Users Set (name, password) = (?, ?) WHERE id == (?)", (Login, Password, Id))
                    con.commit()
                    QtWidgets.QMessageBox.information(None, "Информация", "Пользователь был изменен")
                    query = "SELECT * FROM Users"
                    self.tableWidget.setRowCount(50)
                    tablerow = 0
                    for row in cur.execute(query):
                        self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                        self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                        tablerow += 1
                    self.lineEdit_5.clear()
                    self.lineEdit_6.clear()
                    self.lineEdit_7.clear()
                    self.lineEdit_8.clear()
                    break
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Пользователь не найден")

        if (self.table_name == "Workers"):
            Name = self.lineEdit_5.text()
            Surname = self.lineEdit_6.text()
            Post_Id = self.lineEdit_7.text()
            try:
                cur.execute("SELECT * FROM Workers WHERE id = ?", (Id))
                for row in cur.fetchone():
                    cur.execute("UPDATE Workers Set (name, surname, post_id) = (?, ?, ?) WHERE id == (?)", (Name, Surname, Post_Id, Id))
                    con.commit()
                    QtWidgets.QMessageBox.information(None, "Информация", "Работник был изменен")
                    query = "SELECT * FROM Workers"
                    self.tableWidget.setRowCount(50)
                    tablerow = 0
                    for row in cur.execute(query):
                        self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                        self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                        self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                        tablerow += 1
                    self.lineEdit_5.clear()
                    self.lineEdit_6.clear()
                    self.lineEdit_7.clear()
                    self.lineEdit_8.clear()
                    break
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Работник не найден")

        if (self.table_name == "Post"):
            Name = self.lineEdit_5.text()
            Salary = self.lineEdit_6.text()
            try:
                cur.execute("SELECT * FROM Post WHERE id = ?", (Id))
                for row in cur.fetchone():
                    cur.execute("UPDATE Post Set (name, salary) = (?, ?) WHERE id == (?)", (Name, Salary, Id))
                    con.commit()
                    QtWidgets.QMessageBox.information(None, "Информация", "Должность была изменена")
                    query = "SELECT * FROM Post"
                    self.tableWidget.setRowCount(50)
                    tablerow = 0
                    for row in cur.execute(query):
                        self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                        self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                        tablerow += 1
                    self.lineEdit_5.clear()
                    self.lineEdit_6.clear()
                    self.lineEdit_7.clear()
                    self.lineEdit_8.clear()
                    break
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Должность не найдена")


        if (self.table_name == "Orders"):
            User_Id = self.lineEdit_5.text()
            Menu_Id = self.lineEdit_6.text()
            try:
                cur.execute("SELECT * FROM Orders WHERE id = ?", (Id))
                for row in cur.fetchone():
                    cur.execute("UPDATE Orders Set (menu_id, user_id) = (?, ?) WHERE id == (?)", (User_Id, Menu_Id, Id))
                    con.commit()
                    QtWidgets.QMessageBox.information(None, "Информация", "Заказ был изменен")
                    query = "SELECT * FROM Orders"
                    self.tableWidget.setRowCount(50)
                    tablerow = 0
                    for row in cur.execute(query):
                        self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                        self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                        self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                        tablerow += 1
                    self.lineEdit_5.clear()
                    self.lineEdit_6.clear()
                    self.lineEdit_7.clear()
                    self.lineEdit_8.clear()
                    break
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Заказ не найден")

        if (self.table_name == "Menu"):
            Name = self.lineEdit_5.text()
            Price = self.lineEdit_6.text()
            try:
                cur.execute("SELECT * FROM Menu WHERE id = ?", (Id))
                for row in cur.fetchone():
                    cur.execute("UPDATE Menu Set (name, price) = (?, ?) WHERE id == (?)", (Name, Price, Id))
                    con.commit()
                    QtWidgets.QMessageBox.information(None, "Информация", "Предмет был изменен")
                    query = "SELECT * FROM Menu"
                    self.tableWidget.setRowCount(50)
                    tablerow = 0
                    for row in cur.execute(query):
                        self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                        self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                        tablerow += 1
                    self.lineEdit_5.clear()
                    self.lineEdit_6.clear()
                    self.lineEdit_7.clear()
                    self.lineEdit_8.clear()
                    break
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Предмет не найден")

        if (self.table_name == "Cafe"):
            Name = self.lineEdit_5.text()
            Address = self.lineEdit_6.text()
            Phone_Number = self.lineEdit_7.text()
            try:
                cur.execute("SELECT * FROM Cafe WHERE id = ?", (Id))
                for row in cur.fetchone():
                    cur.execute("UPDATE Cafe Set (name, address, telephone_number) = (?, ?, ?) WHERE id == (?)", (Name, Address, Phone_Number, Id))
                    con.commit()
                    QtWidgets.QMessageBox.information(None, "Информация", "Кафе было изменено")
                    query = "SELECT * FROM Cafe"
                    self.tableWidget.setRowCount(50)
                    tablerow = 0
                    for row in cur.execute(query):
                        self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                        self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                        self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                        tablerow += 1
                    self.lineEdit_5.clear()
                    self.lineEdit_6.clear()
                    self.lineEdit_7.clear()
                    self.lineEdit_8.clear()
                    break
            except Exception:
                QtWidgets.QMessageBox.warning(None, "Ошибка", "Кафе не найдено")

    def selectTable(self, item):
        con, cur = self.printData()
        self.listWidget.hide()
        self.tableWidget.show()
        self.pushButton.show()
        self.pushButton_2.show()
        self.pushButton_3.show()
        self.table_name = item.text()
        if(item.text() == "Users"):
            query = "SELECT * FROM Users"
            self.tableWidget.setRowCount(50)
            tablerow = 0
            for row in cur.execute(query):
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                tablerow += 1
        if(item.text() == "Workers"):
            query = "SELECT * FROM Workers"
            self.tableWidget.setRowCount(50)
            tablerow = 0
            for row in cur.execute(query):
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                tablerow += 1
        if(item.text() == "Post"):
            query = "SELECT * FROM Post"
            self.tableWidget.setRowCount(50)
            tablerow = 0
            for row in cur.execute(query):
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                tablerow += 1
        if(item.text() == "Orders"):
            query = "SELECT * FROM Orders"
            self.tableWidget.setRowCount(50)
            tablerow = 0
            for row in cur.execute(query):
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                tablerow += 1
        if(item.text() == "Menu"):
            query = "SELECT * FROM Menu"
            self.tableWidget.setRowCount(50)
            tablerow = 0
            for row in cur.execute(query):
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                tablerow += 1
        if(item.text() == "Cafe"):
            query = "SELECT * FROM Cafe"
            self.tableWidget.setRowCount(50)
            tablerow = 0
            for row in cur.execute(query):
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                tablerow += 1

        return self.table_name
