# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import re
class Ui_MainWindow(object):

    def __init__(self) -> None:
        super().__init__()
        

    def populateDataTable(self):
        try:
            item_list = self.importData()
            item_list = item_list[1:]
            size = len(item_list)
            self.tableWidget.setRowCount(size)
            for rows in range(0,len(item_list)):
                item = item_list[rows]
                for col in range(0,7):
                    item_child = item[col]
                    self.tableWidget.setItem(rows,col,QtWidgets.QTableWidgetItem(item_child))
        except:
            print("Error while importing the file")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1191, 594)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SortComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.SortComboBox.setGeometry(QtCore.QRect(10, 50, 171, 22))
        
        self.SortComboBox.setObjectName("SortComboBox")
        self.SortComboBox.addItems(["Insertion Sort","Merge Sort","BubbleSort","HeapSort","Binary Insertion Sort","QuickSort","Selection Sort","Intro Sort","Burst Sort","Tree Sort","Tim Sort","Counting Sort","Radix Sort"])
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 55, 16))
        self.label.setObjectName("label")
        self.SelectComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.SelectComboBox.setGeometry(QtCore.QRect(10, 110, 171, 22))
        self.SelectComboBox.setObjectName("SelectComboBox")
        self.SelectComboBox.addItems(['Manufacturer','Model','Description','Price','Rating','no. of reviews','url'])
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
       # self.SearchButton.clicked.connect(self.populateDataTable)
        self.ImportButton.clicked.connect(self.populateDataTable)
        self.ExportButton.clicked.connect(self.exportData)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, G51Project):
        _translate = QtCore.QCoreApplication.translate
        G51Project.setWindowTitle(_translate("G51Project", "MainWindow"))
        self.label.setText(_translate("G51Project", "Sort by"))
        self.label_2.setText(_translate("G51Project", "Select Attribute"))
        self.SearchButton.setText(_translate("G51Project", "Search"))
        self.ImportButton.setText(_translate("G51Project", "Import"))
        self.ExportButton.setText(_translate("G51Project", "Export"))
        self.pauseButton.setText(_translate("G51Project", "Pause"))
        self.StopButton.setText(_translate("G51Project", "Stop"))
        self.ResumeButton.setText(_translate("G51Project", "Resume"))
        item = self.dataTable.horizontalHeaderItem(0)
        item.setText(_translate("G51Project", "Manufacturer"))
        item = self.dataTable.horizontalHeaderItem(1)
        item.setText(_translate("G51Project", "Model"))
        item = self.dataTable.horizontalHeaderItem(2)
        item.setText(_translate("G51Project", "Description"))
        item = self.dataTable.horizontalHeaderItem(3)
        item.setText(_translate("G51Project", "Price"))
        item = self.dataTable.horizontalHeaderItem(4)
        item.setText(_translate("G51Project", "Rating"))
        item = self.dataTable.horizontalHeaderItem(5)
        item.setText(_translate("G51Project", "Reviews"))
        item = self.dataTable.horizontalHeaderItem(6)
        item.setText(_translate("G51Project", "URL"))
        self.increasingRadioButton.setText(_translate("G51Project", "Increasing"))
        self.decreasingRadioButton.setText(_translate("G51Project", "Decreasing"))
        self.FilterButton.setText(_translate("G51Project", "Filter"))
        self.menuMenu.setTitle(_translate("G51Project", "Menu"))
        self.actionExit.setText(_translate("G51Project", "Exit"))
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
        path = self.ImportField.text()
        path = path.replace('\\','\\\\')
        try:
            with open(path,'r',encoding = 'utf-8') as file:
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
        except FileNotFoundError:

            print("File was not found!")
            return 
    def exportData(self):
        data = self.importData()
        path = self.ExportField.text()
        path = path.replace('\\','\\\\')
        print(path)
        try:
            with open(path,'w',newline="",encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            file.close()
        except:
            print("error while exporting the file")
    #######################################          Count Sort          ##########################################
    def findRange(self,array):
        maximum = array[0]
        for i in range(0,len(array)):
            if maximum < array[i]:
                maximum = array[i]
        minimum = array[0]
        for i in range(0,len(array)):
            if minimum > array[i]:
                minimum = array[i]
        rangeOfArray = maximum - minimum
        newArray = []
        for i in range(0,rangeOfArray+1):
            newArray.append(0)
        return newArray,minimum
    def countSort(self,array):
        count , minimum= self.findRange(array)
        output = []
        for i in range(0,len(array)):
            count[array[i] + abs(minimum)] = count[array[i] + abs(minimum)] + 1
        i = 0
        print(count)
        while(i < len(count)):
            if count[i] > 0:
                count[i] = count[i] - 1
                output.append(i - abs(minimum))
            else:
                i = i + 1
        return output
    #################################################################################################################
    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

