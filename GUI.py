# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from bs4 import BeautifulSoup
import time
import sys
from bs4.element import Tag
from selenium import webdriver
from types import coroutine
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import re
import math
import threading


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None


class BST(Node):
    def __init__(self):
        self.root = None
        self.array = []
    # this function take a value, convert it into node and then insert it in the binary tree

    def insertNode(self, value):
        item = Node(value)
        if self.root == None:
            self.root = Node(item.value)
        else:
            current = self.root
            while True:
                if item.value[1] >= current.value[1]:
                    if current.right == None:
                        current.right = Node(item.value)
                        current.right.parent = current
                        break
                    else:
                        current = current.right
                elif item.value[1] < current.value[1]:
                    if current.left == None:
                        current.left = Node(item.value)
                        current.left.parent = current
                        break
                    else:
                        current = current.left
    # this function finds the minimum value of the tree

    def visit(self, node):
        try:
            if node.value != None:
                #print("Node: " + str(node.value))
                self.array.append(node.value)
        except:
            print("Node: None")
    # this is a recursive function for inorder traversal

    def inorder(self, root):
        try:
            if root.left != None:
                self.inorder(root.left)
            self.visit(root)
            if root.right != None:
                self.inorder(root.right)
        except:
            return

    def getSorted(self, array):
        tree = BST()
        for i in range(len(array)):
            tree.insertNode(array[i])
        tree.inorder(tree.root)
        return self.array

    def fill_array(self, Node):
        if Node != None:
            if (Node.left != None):
                pos = self.fill_array(Node.left)

            global BST_array
            BST_array.append(Node.value)

            if (Node.right != None):
                pos = self.fill_array(Node.right)

    def To_Array(self, Node):
        global BST_array
        BST_array = []
        self.fill_array(Node)
        return BST_array


class Ui_G51Project(object):
    itemList = []
    pause = False
    cancel = False
    printTable = []

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
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setRange(0, 101)
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

        #self.increasingRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        #self.increasingRadioButton.setGeometry(QtCore.QRect(110, 140, 95, 20))
        # self.increasingRadioButton.setObjectName("increasingRadioButton")
        #self.decreasingRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        #self.decreasingRadioButton.setGeometry(QtCore.QRect(10, 140, 95, 20))
        # self.decreasingRadioButton.setObjectName("decreasingRadioButton")
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
       # self.increasingRadioButton.raise_()
        # self.decreasingRadioButton.raise_()
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
        self.SortComboBox.addItems(['Insertion Sort', "Merge Sort", "Bubble Sort", "Heap Sort",
                                   "Quick Sort", "Selection Sort", 'Cocktail Sort', 'Shell Sort', 'Tree Sort'])
        self.SelectComboBox.addItems(
            ['Manufacturer', 'Model', 'Description', 'Price', 'Rating', 'No. of reviews'])
        self.ImportButton.clicked.connect(self.populateDataTable)
        self.ExportButton.clicked.connect(self.exportData)
        self.FilterButton.clicked.connect(self.checkFilter)
        self.pauseButton.clicked.connect(self.pauseFeature)
        self.ResumeButton.clicked.connect(self.resumeFeature)
        self.retranslateUi(G51Project)
        # self.SortComboBox.setCurrentIndex(-1)
        # self.increasingRadioButton.setChecked(True)
        self.SpecifyAttributeField.setVisible(False)
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
        # self.increasingRadioButton.setText(
        #   _translate("G51Project", "Increasing"))
        # self.decreasingRadioButton.setText(
        #   _translate("G51Project", "Decreasing"))
        self.FilterButton.setText(_translate("G51Project", "Filter"))
        self.menuMenu.setTitle(_translate("G51Project", "Menu"))
        self.actionExit.setText(_translate("G51Project", "Exit"))
        # self.SortComboBox.activated.connect(self.comboFix)
        self.SearchButton.clicked.connect(self.searchFunction)
        self.StopButton.clicked.connect(self.stopFeature)
        # self.increasingRadioButton.clicked.connect(self.inc_dec_table)
        # self.decreasingRadioButton.clicked.connect(self.inc_dec_table)
        ############################################################################

    def stopFeature(self):
        self.cancel = True

    def pauseFeature(self):
        self.pause = True

    def resumeFeature(self):
        self.pause = False

    def searchFunction(self):
        self.cancel = False
        self.pause = False
        text = self.SearchField.text()
        #print('before :  ' + str(text))
        t = text.split(' ')[0]
        #print("after :   " + str(t))
        t = t.casefold()
        if t == 'scrap':
            self.SearchButton.setText('Search')
            #print("in if sattement")
            self.ProgressBarControl()
        else:
            self.findFilter(text)
            pass

    def findFilter(self, text):
        table = []
        #print('before loop')
        myTable = []
        if self.SearchButton.text() == 'Search':
            for i in range(0, self.dataTable.rowCount()):
                table.append(self.dataTable.item(
                    i, 2).text() + self.dataTable.item(i, 3).text() + self.dataTable.item(i, 4).text() + self.dataTable.item(i, 5).text())
            #print('after loop')
            count = 0
            # "".__contains__()
            select_row = []
            for s in table:
                if s.__contains__(text):
                    select_row.append(count)
                count = count + 1
            #print("select row: " + str(select_row))
            size = self.dataTable.rowCount()
            for i in range(size):
                tuple = (self.dataTable.item(i, 0).text(), self.dataTable.item(i, 1).text(), self.dataTable.item(i, 2).text(), self.dataTable.item(
                    i, 3).text(), self.dataTable.item(i, 4).text(), self.dataTable.item(i, 5).text(), self.dataTable.item(i, 6).text())
                myTable.append(tuple)
            self.printTable = myTable
            myTable = []
            for i in select_row:
                tuple = (self.dataTable.item(i, 0).text(), self.dataTable.item(i, 1).text(), self.dataTable.item(i, 2).text(), self.dataTable.item(
                    i, 3).text(), self.dataTable.item(i, 4).text(), self.dataTable.item(i, 5).text(), self.dataTable.item(i, 6).text())
                myTable.append(tuple)
            # self.dataTable.setSelectionMode(QtGui.QAbstractTextDocumentLayout)
            # table.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
            self.dataTable.clearContents()
            for i in range(len(select_row)):
                try:
                    item = myTable[i]
                    for col in range(7):
                        item_child = item[col]
                        self.dataTable.setItem(
                            i, col, QtWidgets.QTableWidgetItem(item_child))
                except:
                    print("error while filterign the file")
            self.SearchButton.setText('Back')
        else:
            myTable = self.printTable
            #print("lenght of array: " + str(len(myTable)))
            for i in range(len(myTable)):
                try:
                    item = myTable[i]
                    for col in range(7):
                        item_child = item[col]
                        self.dataTable.setItem(
                            i, col, QtWidgets.QTableWidgetItem(item_child))
                except:
                    print("error while filterign the file")
            self.SearchButton.setText("Search")

    def AScrapper(self):
        try:
            driver = webdriver.Chrome(
                executable_path='C:\\Program Files\\Google\\Chrome\\chromedriver.exe')
        # listofitems = ['dell laptops', 'hp laptops', 'lenovo laptops',
            #               'gaming phones', 'smart watches', 'mechanical keyboards', 'adapters', 'gaming mouse', 'gaming chairs', 'xbox accessories', 'playstation accessories', 'moniters', 'asus phones', 'rbg accessories']
            # ['gaming mouse','gaming chairs','xbox accessories','playstation accessories','moniters','asus phones','rbg accessories']
            # ['dell laptops','hp laptops','lenovo laptops','gaming phones','smart watches','mechanical keyboards','adapters']
            items = self.SearchField.text()
            items = items.replace('scrap', '')
            print(items)
            url = self.getUrl(items)
            item_list = []
            for page in range(1, 21):
                while self.pause == True:
                    if self.cancel == True:
                        break
                if self.cancel == True:
                    v = 0
                    # self.progressBar.setValue(v)
                    break
                self.progressBar.setValue(page*5)

                pg = url.format(page)
                driver.get(pg)
                # print(pg)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                results = soup.find_all(
                    'div', {'data-component-type': 's-search-result'})
                for item in results:
                    extracted_data = self.extract_data(item)
                    if extracted_data:
                        item_list.append(extracted_data)
                    # Thread1 = threading.Thread(target=self.saveToCSV,args=(item_list,))
            self.itemList = item_list
            self.saveToCSV(item_list)
            itemList = self.readFromCSV()
            self.populateSearchTable(itemList)

            # Thread2 = threading.Thread(target=self.readFromCSV,args=())
            # Thread3 = threading.Thread(target=self.populateSearchTable,args=(lst))
            # lst = self.readFromCSV()
            # self.populateSearchTable(lst)
            #print("before saving")
            # self.printTable = item_list
            driver.close()

            #print('after reading')
            # self.progressBar.setValue(0)
        except:
            lst = self.readFromCSV()
            #print('after reading')
            self.populateSearchTable(lst)
            # self.progressBar.setValue(0)
            pass

    # save data to a csv file

    def saveToCSV(self, item_list):
        try:
            with open('Mydata.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Manufacturer', 'Model', 'Description',
                                'Price', 'Rating', 'no. of reviews', 'url'])
                writer.writerows(item_list)
                file.close()
        except:
            print("permission denied")

    def readFromCSV(self):
        item_list = []
        try:
            with open('Mydata.csv', 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    Manufacturer = row[0]
                    # Manufacturer = re.sub(r'[^A-Za-z0-9 ]+', '', Manufacturer)
                    Model = row[1]
                    # Model = re.sub(r'[^A-Za-z0-9 ]+', '', Model)
                    Description = row[2]
                    # Description = re.sub(r'[^A-Za-z0-9 ]+', '', Description)
                    Price = row[3]
                    Rating = row[4]
                    review_count = row[5]
                    url = row[6]
                    arr = (Manufacturer, Model, Description,
                           Price, Rating, review_count, url)
                    item_list.append(arr)
            file.close()
            return item_list

        except:

            print("File was not found!")
            return

    def populateSearchTable(self, item_list):
        try:
            # self.itemList = item_list
            size = len(item_list)
            self.dataTable.setRowCount(size)
            # rowCount = self.dataTable.rowCount()
            # right = len(item_list) + rowCount
            for rows in range(0, size):
                item = item_list[rows]
                for col in range(7):
                    item_child = item[col]
                    self.dataTable.setItem(
                        rows, col, QtWidgets.QTableWidgetItem(item_child))
        except:
            print("Error while printing the file")

    def getUrl(self, item):
        template = 'https://www.amazon.com/s?k={}'
        link = item.replace(' ', '+')
        url = template.format(link)
        url += '&page={}'
        return url

    def extract_data(self, item):
        description = item.h2.a.text
        description = re.sub(r'[^A-Za-z0-9 ]+', '', description)
        atag = item.h2.a
        href = atag.get('href')
        link = 'https://www.amazon.com' + href
        company = description.split(' ')[0]
        company = "".join(company)
        model = description.split(' ')[1:]
        model = " ".join(model)
        try:
            price_parent = item.find('span', 'a-price')
            price = price_parent.find('span', 'a-offscreen').text
        except AttributeError:
            return
        try:
            rating = item.i.text
            reviews = item.find('span', 'a-size-base').text
        except AttributeError:
            return

        result = (company, model, description,
                  price, rating, reviews, link)
        # print(result)
        return result

    def ProgressBarControl(self):
        self.cancel = False
        thread = threading.Thread(target=self.AScrapper, args=())
        thread.start()

    """def comboFix(self):
        s = self.SortComboBox.currentText()
        if s == 'Tree Sort' or 'Radix Sort' or 'Count Sort':
            self.SelectComboBox.clear()
            self.SelectComboBox.addItems(['Price', 'Rating', 'No. of reviews'])
        else:
            self.SelectComboBox.clear()
            self.SelectComboBox.addItems(
                ['Manufacturer', 'Model', 'Description', 'Price', 'Rating', 'No. of reviews', 'url'])"""

    def importData(self):
        item_list = []
        path = self.ImportField.text()
        if path == None:
            path = 'ScrappedData.csv'
        path = path.replace('\\', '\\\\')
        try:
            with open(path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    Manufacturer = row[0]
                    # Manufacturer = re.sub(r'[^ \w+]', '', Manufacturer)
                    Model = row[1]
                    # Model = re.sub(r'[^ \w+]', '', Model)
                    Description = row[2]
                    Description = re.sub(r'[^ \w+]', '', Description)
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

    def getTableData(self):
        size = self.dataTable.rowCount()
        myTable = []
        for i in range(size):
            try:
                tuple = (self.dataTable.item(i, 0).text(), self.dataTable.item(i, 1).text(), self.dataTable.item(i, 2).text(), self.dataTable.item(
                    i, 3).text(), self.dataTable.item(i, 4).text(), self.dataTable.item(i, 5).text(), self.dataTable.item(i, 6).text())
                myTable.append(tuple)

            except:
                i = i + 1
        return myTable

    def exportData(self):
        data = self.getTableData()
        path = self.ExportField.text()
        path = path.replace('\\', '\\\\')
        # print(path)
        try:
            with open(path, 'w', newline="", encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            file.close()
        except:
            print("error while exporting the file")
    """  # Count Sort          ##########################################

    def countSort(self, array):
        for i in range(len(array)):
            array[i][1] = array[i][1] * 100
        count, minimum = self.findRange(array)
        output = []
        for i in range(0, len(array)):
            count[array[i][1]] = count[array[i][1]] + 1
        i = 0
        print(count)
        while(i < len(count)):
            if count[i] > 0:
                count[i] = count[i] - 1
                output.append(i - abs(minimum))
            else:
                i = i + 1
        return output

    def findRange(self, array):
        maximum = array[0][1]
        for i in range(0, len(array)):
            if maximum < array[i][1]:
                maximum = array[i][1]
        for i in range(0, maximum+1):
            newArray.append(0)
        return newArray, minimum"""
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
#################################           Shell Sort          ##################################

    def Shell_sort(self, array):

        gap = len(array) // 2

        while gap > 0:
            i = 0
            j = gap

            while (j < len(array)):

                if (array[i][1] > array[j][1]):
                    array[i], array[j] = array[j], array[i]

                i = i + 1
                j = j + 1

                k = i
                while (k - gap > -1):

                    if array[k - gap][1] > array[k][1]:
                        array[k-gap], array[k] = array[k], array[k-gap]

                    k = k - 1

            gap = gap // 2

        return array

##########################          CockTail Sort           #################################
    def cocktail_sort(self, array):
        swapped = True
        start = 0
        end = len(array) - 1
        while (swapped == True):

            swapped = False

            for i in range(start, end):
                if (array[i][1] > array[i + 1][1]):
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True

            if (swapped == False):
                break

            swapped = False

            end = end-1

            for i in range(end-1, start-1, -1):
                if (array[i][1] > array[i + 1][1]):
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True

            start = start + 1

        return array

    def BinaryTreeSort(self, array):
        bt = BST()
        for i in array:

            bt.insertNode(i)

        b = bt.To_Array(bt.root)

        return b

    ######################################################

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
            self.dataTable.clearFocus()
        except:
            print("Your csv file may contain some characters that utf-8 can't decode \n please use a valid csv file")

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

    def SelectionSort(self, Array):
        for i in range(0, len(Array)):
            min_index = i
            for j in range(i+1, len(Array)):
                if(Array[j][1] < Array[min_index][1]):
                    min_index = j
            Array[i], Array[min_index] = Array[min_index], Array[i]
        return Array
############################            Radix Sort              #########################################

    def getNumber(num, n):
        try:
            s = str(num)
            index = len(s) - n
            if(index < 0):
                return 0
            n = int(s[len(s)-n])
            return n
        except IndexError:
            return 0

    def checkBucket(bucket):
        for i in range(10):
            if bucket[i]:
                return True
        return False

    def combineBucket(bucket):
        arr = []
        for i in range(10):
            arr = arr + bucket[i]
        return arr

    def RadixSort(self, array):
        bucket = [[] for i in range(10)]
        greatest = array[0][1]
        for i in range(len(array)):
            if greatest < array[i][1]:
                greatest = array[i][1]
        size = len(str(greatest))
        for i in range(len(array)):
            a = array[i][1]
            a = a[0] % 10
            bucket[a].append(array[i])
        bucket1 = [[] for i in range(10)]
        for i in range(1, size+1):
            for j in range(10):
                if self.checkBucket(bucket):
                    while len(bucket[j]) > 0:
                        num = bucket[j].pop(0)
                        a = self.getNumber(num[1], i)
                        bucket1[a[0]].append(num)
            for j in range(10):
                if self.checkBucket(bucket1):
                    while len(bucket1[j]) > 0:
                        num = bucket1[j].pop(0)
                        a = self.getNumber(num[1], i)
                        bucket[a[0]].append(num)
        return self.combineBucket(bucket)
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
                if array[right] > array[index]:
                    array[right], array[index] = array[index], array[right]
                    index = right
                else:
                    break
            else:
                break

    def heapsort(self, array):
        for i in range((len(array)-2)//2, -1, -1):
            self.heapifyDown(array, i, len(array))
        for j in range(len(array)-1, 0, -1):
            array[j], array[0] = array[0], array[j]
            self.heapifyDown(array, 0, j)

    def bubbleSort(self, array):
        for i in range(0, len(array)):
            swapped = False

            for j in range(0, len(array)-i-1):
                if(array[j][1] > array[j+1][1]):
                    array[j], array[j+1] = array[j+1], array[j]
                    swapped = True

            if(not swapped):
                break

        return array

    def burstSort(self, array):
        pass
        #################################################################################################################

    def checkFilter(self):
        item_selected = self.SelectComboBox.currentText()
        # print(item_selected)
        wrong_indexes = []
        index = [[], []]
        indexRating = [[], []]
        ratingArray = []
        companyBucket = [[], []]
        companyArray = []
        descriptionBucket = [[], []]
        descriptionArray = []
        reviewBucket = [[], []]
        reviewArray = []
        urlBucket = [[], []]
        urlArray = []
        modelBucket = [[], []]
        modelArray = []
        count = 0
        # print(item_selected)
        array = []
        for item in self.itemList:
            # print(item_selected)
            try:
                ###########         Model           #####################
                md = item[1]
                md = md.upper()
                modelBucket[0].append(count)
                modelBucket[1].append(md)
                modelArray.append(modelBucket)
                modelBucket = [[], []]
                ############    URL         ############################
                url = item[6]
                urlBucket[0].append(count)
                urlBucket[1].append(url)
                urlArray.append(url)
                urlBucket = [[], []]
                ###############         No of reviews       ########################
                rw = item[5]
                rw = rw.replace(',', "")
                rw = int(rw)
                reviewBucket[0].append(count)
                reviewBucket[1].append(rw)
                reviewArray.append(reviewBucket)
                reviewBucket = [[], []]
                ####################        Description         ##########################
                ds = item[2]
                descriptionBucket[0].append(count)
                ds = ds.upper()
                descriptionBucket[1].append(ds)
                descriptionArray.append(descriptionBucket)
                descriptionBucket = [[], []]
                #######     for rating     ###############
                rt = item[4]
                # print("rating " + str(rt))
                rt = str(rt)
                rt = rt.split(' ')
                rt = rt[0]
                rt = float(rt)
                # print("rt  = " + str(rt))
                indexRating[0].append(count)
                indexRating[1].append(rt)
                ratingArray.append(indexRating)
                indexRating = [[], []]
                ###################     company     ######################
                cp = item[0]
                cp = cp.upper()
                companyBucket[0].append(count)
                companyBucket[1].append(cp)
                companyArray.append(companyBucket)
                companyBucket = [[], []]
                ###############        for Price    ####################
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
                ########################################################
                count = count + 1
            except:
                wrong_indexes.append(count)
        attribute = self.SelectComboBox.currentText()
        if attribute == 'Price':
            thread = threading.Thread(
                target=self.SortAttribute, args=(array, wrong_indexes,))
            # self.SortAttribute(array, wrong_indexes)
            thread.start()
        elif attribute == 'Manufacturer':
            thread = threading.Thread(
                target=self.SortAttribute, args=(companyArray, wrong_indexes,))
            thread.start()
            # self.SortAttribute(companyArray, wrong_indexes)
        elif attribute == 'Description':
            thread = threading.Thread(target=self.SortAttribute, args=(
                descriptionArray, wrong_indexes,))
            thread.start()
            # self.SortAttribute(descriptionArray, wrong_indexes)
        elif attribute == 'Rating':
            thread = threading.Thread(
                target=self.SortAttribute, args=(ratingArray, wrong_indexes,))
            thread.start()
            # self.SortAttribute(ratingArray, wrong_indexes)
        elif attribute == 'URL':
            # self.SortAttribute(urlArray, wrong_indexes)
            thread = threading.Thread(
                target=self.SortAttribute, args=(urlArray, wrong_indexes,))
            thread.start()

        elif attribute == 'No. of reviews':
            # self.SortAttribute(reviewArray, wrong_indexes)
            thread = threading.Thread(
                target=self.SortAttribute, args=(reviewArray, wrong_indexes,))
            thread.start()

        elif attribute == 'Model':
            thread = threading.Thread(
                target=self.SortAttribute, args=(modelArray, wrong_indexes,))
            thread.start()

    def SortAttribute(self, array, wrong_indexes):
        sortBy = self.SortComboBox.currentText()
        if sortBy == 'Merge Sort':
            array = self.mergeSort(array)
        elif sortBy == 'Insertion Sort':
            array = self.insertionSort(array)
        elif sortBy == 'Heap Sort':
            self.heapsort(array)
        elif sortBy == 'Quick Sort':
            array = self.quickSort(array, 0, len(array)-1)
        elif sortBy == 'Selection Sort':
            array = self.SelectionSort(array)
        elif sortBy == 'Radix Sort':
            array = self.RadixSort(array)
        elif sortBy == 'Bubble Sort':
            array = self.bubbleSort(array)
        elif sortBy == 'Shell Sort':
            array = self.Shell_sort(array)
        elif sortBy == 'Cocktail Sort':
            array = self.cocktail_sort(array)
        elif sortBy == 'Tree Sort':
            array = self.BinaryTreeSort(array)
            # print(array)
        self.dataTable.clearContents()
        item_list = self.importData()
        if item_list == None:
            item_list = self.readFromCSV()
        item_list = item_list[1:]
        self.itemList = item_list
        size = len(item_list)
        self.dataTable.setRowCount(size)
        self.dataTable.clearContents()
        # print("lenghts: " + str(len(array)) + "   " +
        #     str(size) + "          " + str(len(wrong_indexes)))
        for i in wrong_indexes:
            item_list.pop(i)
        #print("After poping")
        # print("lenghts: " + str(len(array)) + "   " +
            # str(size) + "          " + str(len(wrong_indexes)))
        for rows in range(0, len(array)):
            index = array[rows][0][0]
            item = item_list[index]
            for col in range(7):
                item_child = item[col]
                self.dataTable.setItem(
                    rows, col, QtWidgets.QTableWidgetItem(item_child))
        self.dataTable.clearFocus()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    G51Project = QtWidgets.QMainWindow()
    ui = Ui_G51Project()
    ui.setupUi(G51Project)
    G51Project.show()
    sys.exit(app.exec_())
