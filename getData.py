# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import csv
class Ui_MainWindow(object):
    def populateDataTable(self):
        item_list = self.importData()
        size = len(item_list)
        self.tableWidget.setRowCount(size)
        for rows in range(1,len(item_list)):
            item = item_list[rows]
            for col in range(0,7):
                item_child = item[col]
                self.tableWidget.setItem(rows,col,QtWidgets.QTableWidgetItem(item_child))
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1191, 594)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SortComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.SortComboBox.setGeometry(QtCore.QRect(10, 50, 171, 22))
        self.SortComboBox.setObjectName("SortComboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 55, 16))
        self.label.setObjectName("label")
        self.SelectComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.SelectComboBox.setGeometry(QtCore.QRect(10, 110, 171, 22))
        self.SelectComboBox.setObjectName("SelectComboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 91, 16))
        self.label_2.setObjectName("label_2")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(190, 210, 81, 31))
        self.SearchButton.setObjectName("SearchButton")
        self.SearchField = QtWidgets.QLineEdit(self.centralwidget)
        self.SearchField.setGeometry(QtCore.QRect(10, 210, 171, 31))
        self.SearchField.setObjectName("SearchField")
        self.ImportField = QtWidgets.QLineEdit(self.centralwidget)
        self.ImportField.setGeometry(QtCore.QRect(10, 260, 171, 31))
        self.ImportField.setObjectName("ImportField")
        self.ImportButton = QtWidgets.QPushButton(self.centralwidget)
        self.ImportButton.setGeometry(QtCore.QRect(190, 260, 81, 31))
        self.ImportButton.setObjectName("ImportButton")
        self.ExportField = QtWidgets.QLineEdit(self.centralwidget)
        self.ExportField.setGeometry(QtCore.QRect(10, 310, 171, 31))
        self.ExportField.setObjectName("ExportField")
        self.ExportButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExportButton.setGeometry(QtCore.QRect(190, 310, 81, 31))
        self.ExportButton.setObjectName("ExportButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(320, 10, 571, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(890, 10, 81, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(980, 10, 81, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1070, 10, 81, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(320, 60, 841, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1191, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.SearchButton.clicked.connect(self.populateDataTable)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sort by"))
        self.label_2.setText(_translate("MainWindow", "Select Column"))
        self.SearchButton.setText(_translate("MainWindow", "Search"))
        self.ImportButton.setText(_translate("MainWindow", "Import"))
        self.ExportButton.setText(_translate("MainWindow", "Export"))
        self.pushButton_4.setText(_translate("MainWindow", "Pause"))
        self.pushButton_5.setText(_translate("MainWindow", "Stop"))
        self.pushButton_6.setText(_translate("MainWindow", "Resume"))
     # """  item = self.tableWidget.horizontalHeaderItem(0)
      #  item.setText(_translate("MainWindow", "No."))"""
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Manufacturer"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Model"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Rating"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Reviews"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "URL"))
    def importData(self):
        item_list = []
        with open('data.csv','r',encoding = 'utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                Manufacturer = row[0]
                Model = row[1]
                Description = row[2]
                Price = row[3]
                Rating = row[4]
                review_count = row[5]
                url = row[6]
                arr = (Manufacturer, Model, Description, Price, Rating,review_count,url)
                item_list.append(arr)
        return item_list
       
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

