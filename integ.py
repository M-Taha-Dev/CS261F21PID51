# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from types import coroutine
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import re
import math


class Ui_G51Project(object):
    itemList = []

    def setupUi(self, G51Project):
        G51Project.setObjectName("G51Project")
        G51Project.setEnabled(True)
        G51Project.resize(1320, 676)
        self.centralwidget = QtWidgets.QWidget(G51Project)
        self.centralwidget.setObjectName("centralwidget")
        self.SortComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.SortComboBox.setEnabled(True)
        self.SortComboBox.setGeometry(QtCore.QRect(10, 50, 271, 22))
        self.SortComboBox.setEditable(False)
        self.SortComboBox.setCurrentText("")
        self.SortComboBox.setObjectName("SortComboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 55, 16))
        self.label.setObjectName("label")
        self.SelectComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.SelectComboBox.setGeometry(QtCore.QRect(10, 110, 271, 22))
        self.SelectComboBox.setObjectName("SelectComboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 91, 16))
        self.label_2.setObjectName("label_2")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(290, 220, 81, 31))
        self.SearchButton.setObjectName("SearchButton")
        self.SearchField = QtWidgets.QLineEdit(self.centralwidget)
        self.SearchField.setGeometry(QtCore.QRect(10, 220, 271, 31))
        self.SearchField.setObjectName("SearchField")
        self.ImportField = QtWidgets.QLineEdit(self.centralwidget)
        self.ImportField.setGeometry(QtCore.QRect(10, 510, 271, 31))
        self.ImportField.setObjectName("ImportField")
        self.ImportButton = QtWidgets.QPushButton(self.centralwidget)
        self.ImportButton.setGeometry(QtCore.QRect(290, 510, 81, 31))
        self.ImportButton.setObjectName("ImportButton")
        self.ExportField = QtWidgets.QLineEdit(self.centralwidget)
        self.ExportField.setGeometry(QtCore.QRect(10, 560, 271, 31))
        self.ExportField.setObjectName("ExportField")
        self.ExportButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExportButton.setGeometry(QtCore.QRect(290, 560, 81, 31))
        self.ExportButton.setObjectName("ExportButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(430, 10, 571, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(1000, 10, 81, 31))
        self.pauseButton.setObjectName("pauseButton")
        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setGeometry(QtCore.QRect(1090, 10, 81, 31))
        self.StopButton.setObjectName("StopButton")
        self.ResumeButton = QtWidgets.QPushButton(self.centralwidget)
        self.ResumeButton.setGeometry(QtCore.QRect(1180, 10, 81, 31))
        self.ResumeButton.setObjectName("ResumeButton")
        self.dataTable = QtWidgets.QTableWidget(self.centralwidget)
        self.dataTable.setGeometry(QtCore.QRect(430, 50, 881, 581))
        self.dataTable.setObjectName("dataTable")
        self.dataTable.setColumnCount(7)
        self.dataTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(6, item)
        self.increasingRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.increasingRadioButton.setGeometry(QtCore.QRect(110, 140, 95, 20))
        self.increasingRadioButton.setObjectName("increasingRadioButton")
        self.decreasingRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.decreasingRadioButton.setGeometry(QtCore.QRect(10, 140, 95, 20))
        self.decreasingRadioButton.setObjectName("decreasingRadioButton")
        self.SpecifyAttributeField = QtWidgets.QLineEdit(self.centralwidget)
        self.SpecifyAttributeField.setGeometry(QtCore.QRect(10, 170, 271, 31))
        self.SpecifyAttributeField.setObjectName("SpecifyAttributeField")
        self.FilterButton = QtWidgets.QPushButton(self.centralwidget)
        self.FilterButton.setGeometry(QtCore.QRect(290, 170, 81, 31))
        self.FilterButton.setObjectName("FilterButton")
        self.FilterButton.raise_()
        self.SortComboBox.raise_()
        self.label.raise_()

        self.SelectComboBox.raise_()
        self.label_2.raise_()
        self.SearchButton.raise_()
        self.SearchField.raise_()
        self.ImportField.raise_()
        self.ImportButton.raise_()
        self.ExportField.raise_()
        self.ExportButton.raise_()
        self.progressBar.raise_()
        self.pauseButton.raise_()
        self.StopButton.raise_()
        self.ResumeButton.raise_()
        self.dataTable.raise_()
        self.increasingRadioButton.raise_()
        self.decreasingRadioButton.raise_()
        self.SpecifyAttributeField.raise_()
        G51Project.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(G51Project)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1320, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        G51Project.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(G51Project)
        self.statusbar.setObjectName("statusbar")
        G51Project.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(G51Project)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())
        ######################################
        self.SortComboBox.addItems(['Insertion Sort', "Merge Sort", "Bubble Sort", "Heap Sort", "Binary Insertion Sort",
                                   "Quick Sort", "Selection Sort", "Intro Sort", "Burst Sort", "Tree Sort", "Tim Sort", "Counting Sort", "Radix Sort"])
        self.SelectComboBox.addItems(
            ['Manufacturer', 'Model', 'Description', 'Price', 'Rating', 'no. of reviews', 'url'])
        self.ImportButton.clicked.connect(self.populateDataTable)
        self.ExportButton.clicked.connect(self.exportData)
        self.FilterButton.clicked.connect(self.checkFilter)

        self.retranslateUi(G51Project)
        self.SortComboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(G51Project)

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
        self.increasingRadioButton.setText(
            _translate("G51Project", "Increasing"))
        self.decreasingRadioButton.setText(
            _translate("G51Project", "Decreasing"))
        self.FilterButton.setText(_translate("G51Project", "Filter"))
        self.menuMenu.setTitle(_translate("G51Project", "Menu"))
        self.actionExit.setText(_translate("G51Project", "Exit"))

        ############################################################################

    def importData(self):
        item_list = []
        path = self.ImportField.text()
        path = path.replace('\\', '\\\\')
        try:
            with open(path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    Manufacturer = row[0]
                    Model = row[1]
                    Description = row[2]
                    Price = row[3]
                    Rating = row[4]
                    review_count = row[5]
                    url = row[6]
                    arr = (Manufacturer, Model, Description,
                           Price, Rating, review_count, url)
                    item_list.append(arr)
            return item_list
        except FileNotFoundError:
            print("File was not found!")
            return None

    def exportData(self):
        data = self.importData()
        path = self.ExportField.text()
        path = path.replace('\\', '\\\\')
        print(path)
        try:
            with open(path, 'w', newline="", encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            file.close()
        except:
            print("error while exporting the file")
    #######################################          Count Sort          ##########################################

    def findRange(self, array):
        maximum = array[0]
        for i in range(0, len(array)):
            if maximum < array[i]:
                maximum = array[i]
        minimum = array[0]
        for i in range(0, len(array)):
            if minimum > array[i]:
                minimum = array[i]
        rangeOfArray = maximum - minimum
        newArray = []
        for i in range(0, rangeOfArray+1):
            newArray.append(0)
        return newArray, minimum
    ############################### Merge Sort ################################################

    def merge(self, array1, array2):
        l1 = len(array1)
        l2 = len(array2)
        i = 0
        j = 0
        array = []

        while i < l1 and j < l2:
            if array1[i][1] <= array2[j][1]:
                array.append(array1[i])
                i = i + 1
            else:
                array.append(array2[j])
                j = j + 1

        while i < l1:
            array.append(array1[i])
            i = i + 1

        while j < l2:
            array.append(array2[j])
            j = j + 1

        return array

    def mergeSort(self, array):
        if len(array) <= 1:
            return array

        mid = int(len(array)/2)

        right = array[:mid]
        left = array[mid:]

        right = self.mergeSort(right)
        left = self.mergeSort(left)

        arr = self.merge(left, right)
        return arr

    ######################################################

    def countSort(self, array):
        count, minimum = self.findRange(array)
        output = []
        for i in range(0, len(array)):
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

    def populateDataTable(self):
        try:

            item_list = self.importData()
            item_list = item_list[1:]
            self.itemList = item_list
            size = len(item_list)
            self.dataTable.setRowCount(size)
            for rows in range(0, len(item_list)):
                item = item_list[rows]
                for col in range(7):
                    item_child = item[col]
                    self.dataTable.setItem(
                        rows, col, QtWidgets.QTableWidgetItem(item_child))
        except:
            print("Error while importing the file")

    def insertionSort(self, array):

        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and array[j][1] > key[1]:
                array[j+1] = array[j]
                j = j-1
            array[j + 1] = key
        return array

    def quickSort(self, arr, low, high):
        if (low < high):
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)
            return arr

    def partition(self, arr, low, high):
        pivot = arr[high][1]
        i = low - 1
        for j in range(low, high):
            if (arr[j][1] < pivot):
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i+1]
        return (i + 1)

    def TimSort(self, array):
        pass

    def SelectionSort(self, array):
        pass

    def RadixSort(self, array):
        pass

    def BucketSort(self, array):
        pass

    def heapifyDown(self, array, index, upper):
        while True:
            left = index*2+1
            right = index*2+2
            if max(left, right) < upper:
                if array[index][1] >= max(array[left][1], array[right][1]):
                    break
                elif array[left][1] > array[right][1]:
                    array[index], array[left] = array[left], array[index]
                    index = left
                else:
                    array[index], array[right] = array[right], array[index]
                    index = right
            elif left < upper:
                if array[left][1] > array[index][1]:
                    array[left], array[index] = array[index], array[left]
                    index = left
                else:
                    break
            elif right < upper:
                if array[right][1] > array[index][1]:
                    array[right], array[index] = array[index], array[right]
                    index = right
                else:
                    break
            else:
                break

    def HeapSort(self, array):
        for i in range((len(array)-2)//2, -1, -1):
            self.heapifyDown(array, i, len(array))
        for j in range(len(array)-1, 0, -1):
            array[j], array[0] = array[0], array[j]
            self.heapifyDown(array, 0, j)
        self.HeapSort(array)
        return array

    def bubbleSort(self, array):
        pass

    def burstSort(self, array):
        pass
        #################################################################################################################

    def checkFilter(self):
        item_selected = self.SelectComboBox.currentText()
        print(item_selected)
        wrong_indexes = []
        if item_selected == 'Price':
            index = [[], []]
            count = 0
            print(item_selected)
            array = []

            for item in self.itemList:
                # print(item_selected)
                try:
                    pr = item[3]

                    # print(pr)
                    pr = pr.replace("$", "")
                    # print(pr)
                    pr = pr.replace(" ", "")
                    pr = pr.replace(",", "")
                   # print(pr)
                    p = math.ceil(float(pr))
                    # print(item_selected)
                    index[1].append(p)
                    array.append(index)
                    index[0].append(count)
                    index = [[], []]
                    tuple = (count, p)
                    count = count + 1
                except:
                    wrong_indexes.append(count)
                    pass
            self.sortPrice(array, wrong_indexes)

    def sortPrice(self, array, wrong_indexes):
        sortBy = self.SortComboBox.currentText()
        if sortBy == 'Merge Sort':
            arr = self.mergeSort(array)
        elif sortBy == 'Insertion Sort':
            arr = self.insertionSort(array)
        elif sortBy == 'Heap Sort':
            arr = self.HeapSort(array)
        elif sortBy == 'Quick Sort':
            arr = self.quickSort(array, 0, len(array)-1)

        self.dataTable.clearContents()

        item_list = self.importData()
        item_list = item_list[1:]
        self.itemList = item_list
        size = len(item_list)
        self.dataTable.setRowCount(size)
        print("lenghts: " + str(len(arr)) + "   " +
              str(size) + "          " + str(len(wrong_indexes)))
        for i in wrong_indexes:
            item_list.pop(i)
        print("After poping")
        print("lenghts: " + str(len(arr)) + "   " +
              str(size) + "          " + str(len(wrong_indexes)))
        for rows in range(0, len(arr)):
            index = arr[rows][0][0]

            item = item_list[index]
            for col in range(7):
                item_child = item[col]
                self.dataTable.setItem(
                    rows, col, QtWidgets.QTableWidgetItem(item_child))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    G51Project = QtWidgets.QMainWindow()
    ui = Ui_G51Project()
    ui.setupUi(G51Project)
    G51Project.show()
    sys.exit(app.exec_())
