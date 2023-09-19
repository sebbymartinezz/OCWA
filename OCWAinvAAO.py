
import string
import os
import shutil


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication
from PyQt5.QtGui import QPixmap, QImageReader
from PyQt5.QtCore import Qt, QMimeData

import sqlite3

class ImageDropZone(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setAcceptDrops(True)
        self.setText("Drop an image here...")

    def dragEnterEvent(self, event):
        mime_data = event.mimeData()
        if mime_data.hasUrls() and len(mime_data.urls()) == 1:
            event.acceptProposedAction()

    def dropEvent(self, event):
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.current_image_path = file_path  # Store the path
            self.load_and_display_image(file_path)


    def load_and_display_image(self, file_path):
        pixmap = QPixmap(file_path)
        self.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def contextMenuEvent(self, event):
        menu = QtWidgets.QMenu(self)

        paste_action = menu.addAction("Paste Image")
        clear_action = menu.addAction("Clear Image")

        # Connect actions to functions
        paste_action.triggered.connect(self.paste_image_from_clipboard)
        clear_action.triggered.connect(self.clear_image)

        menu.exec_(event.globalPos())

    def paste_image_from_clipboard(self):
        clipboard = QtWidgets.QApplication.clipboard()
        mime_data = clipboard.mimeData()

        if mime_data.hasImage():
            image = clipboard.image()
            pixmap = QPixmap.fromImage(image)
            self.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def clear_image(self):
            self.setPixmap(QPixmap())  # Clears the image
            self.setText("Drop an image here...")
            if hasattr(self, 'current_image_path'):
                    delattr(self, 'current_image_path')  # Remove the stored path attribute


class Ui_Dialog(object):
    def setupUi(self, Dialog):


        self.image_drop_zone = ImageDropZone()





        Dialog.setObjectName("Dialog")
        Dialog.resize(1273, 876)
        Dialog.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1271, 881))
        self.stackedWidget.setObjectName("stackedWidget")
        self.WELCOME_PG = QtWidgets.QWidget()
        self.WELCOME_PG.setObjectName("WELCOME_PG")
        self.welcome = QtWidgets.QWidget(self.WELCOME_PG)
        self.welcome.setGeometry(QtCore.QRect(0, -10, 1271, 881))
        self.welcome.setStyleSheet("QWidget#welcome{\n"
"    background-color:qlineargradient(spread:pad, x1:0.517, y1:0.539727, x2:0.528, y2:1, stop:0 rgba(0, 116, 188, 255), stop:1 rgba(255, 255, 255, 255));}\n"
"\n"
"")
        self.welcome.setObjectName("welcome")
        self.label_2 = QtWidgets.QLabel(self.welcome)
        self.label_2.setGeometry(QtCore.QRect(530, 90, 251, 61))
        self.label_2.setStyleSheet("font: 8pt \"AIGDT\";\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.welcome)
        self.label.setGeometry(QtCore.QRect(590, 260, 111, 21))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.welcome)
        self.label_3.setGeometry(QtCore.QRect(580, 190, 171, 71))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 28pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.SEARCHALLPB = QtWidgets.QPushButton(self.welcome)
        self.SEARCHALLPB.setGeometry(QtCore.QRect(422, 360, 171, 51))
        self.SEARCHALLPB.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.SEARCHALLPB.setObjectName("SEARCHALLPB")
        self.VIEWSTOCKPB = QtWidgets.QPushButton(self.welcome)
        self.VIEWSTOCKPB.setGeometry(QtCore.QRect(710, 360, 171, 51))
        self.VIEWSTOCKPB.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.VIEWSTOCKPB.setObjectName("VIEWSTOCKPB")
        self.ADDPB = QtWidgets.QPushButton(self.welcome)
        self.ADDPB.setGeometry(QtCore.QRect(420, 460, 171, 51))
        self.ADDPB.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.ADDPB.setObjectName("ADDPB")
        self.SENDSTOCKPB_1 = QtWidgets.QPushButton(self.welcome)
        self.SENDSTOCKPB_1.setGeometry(QtCore.QRect(710, 460, 171, 51))
        self.SENDSTOCKPB_1.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.SENDSTOCKPB_1.setObjectName("SENDSTOCKPB_1")
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.VIEWSTOCKPB.raise_()
        self.ADDPB.raise_()
        self.SENDSTOCKPB_1.raise_()
        self.SEARCHALLPB.raise_()
        self.stackedWidget.addWidget(self.WELCOME_PG)
        self.SEARCH_PG = QtWidgets.QWidget()
        self.SEARCH_PG.setObjectName("SEARCH_PG")
        self.search_menu = QtWidgets.QWidget(self.SEARCH_PG)
        self.search_menu.setGeometry(QtCore.QRect(0, 0, 1271, 881))
        self.search_menu.setToolTipDuration(1)
        self.search_menu.setStyleSheet("QWidget#search_menu{\n"
"background-color: qlineargradient(spread:pad, x1:0.551975, y1:0.341, x2:0.553, y2:1, stop:0.810945 rgba(0, 122, 201, 255), stop:1 rgba(255, 255, 255, 255));}\n"
"\n"
"")
        self.search_menu.setObjectName("search_menu")
        self.SEARCHALLPB_7 = QtWidgets.QPushButton(self.search_menu)
        self.SEARCHALLPB_7.setGeometry(QtCore.QRect(770, 160, 131, 41))
        self.SEARCHALLPB_7.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.SEARCHALLPB_7.setObjectName("SEARCHALLPB_7")
        self.label_7 = QtWidgets.QLabel(self.search_menu)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 421, 61))
        self.label_7.setStyleSheet("font: 8pt \"AIGDT\";\n"
"font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.search_menu)
        self.lineEdit.setGeometry(QtCore.QRect(220, 160, 531, 41))
        self.lineEdit.setStyleSheet("border-radius:20px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.label_8 = QtWidgets.QLabel(self.search_menu)
        self.label_8.setGeometry(QtCore.QRect(240, 200, 301, 16))
        self.label_8.setObjectName("label_8")
        self.SEARCHALLPB_8 = QtWidgets.QPushButton(self.search_menu)
        self.SEARCHALLPB_8.setGeometry(QtCore.QRect(1060, 680, 201, 41))
        self.SEARCHALLPB_8.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.SEARCHALLPB_8.setObjectName("SEARCHALLPB_8")
        self.MAINMENU_1 = QtWidgets.QPushButton(self.search_menu)
        self.MAINMENU_1.setGeometry(QtCore.QRect(10, 680, 201, 41))
        self.MAINMENU_1.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.MAINMENU_1.setObjectName("MAINMENU_1")
        self.SEARCHALLPB_11 = QtWidgets.QPushButton(self.search_menu)
        self.SEARCHALLPB_11.setGeometry(QtCore.QRect(20, 80, 151, 21))
        self.SEARCHALLPB_11.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.SEARCHALLPB_11.setObjectName("SEARCHALLPB_11")
        self.tableWidget_search = QtWidgets.QTableWidget(self.search_menu)
        self.tableWidget_search.setEnabled(True)
        self.tableWidget_search.setGeometry(QtCore.QRect(10, 231, 1251, 441))
        self.tableWidget_search.setObjectName("tableWidget_search")
        self.tableWidget_search.setColumnCount(10)
        self.tableWidget_search.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search.setHorizontalHeaderItem(8, item)
        self.tableWidget_search.horizontalHeader().setDefaultSectionSize(134)
        self.listWidget_tags = QtWidgets.QListWidget(self.search_menu)
        self.listWidget_tags.setGeometry(QtCore.QRect(20, 104, 171, 41))
        self.listWidget_tags.setDisabled(True)
        self.listWidget_tags.setObjectName("listWidget_tags")

        self.pushButton = QtWidgets.QPushButton(self.search_menu)
        self.pushButton.setGeometry(QtCore.QRect(197, 104, 71, 45))
        self.pushButton.setObjectName("pushButton")
        self.SEEMORE_1 = QtWidgets.QWidget(self.search_menu)
        self.SEEMORE_1.setGeometry(QtCore.QRect(-4, 12, 1131, 851))
        self.SEEMORE_1.setStyleSheet("QWidget#SEEMORE_1{\n"
"background-color: qlineargradient(spread:pad, x1:0.551975, y1:0.341, x2:0.553, y2:1, stop:0.810945 rgba(0, 122, 201, 255), stop:1 rgba(255, 255, 255, 255)border-color: rgb(0, 0, 0))  ;}\n"
"\n"
"\n"
"")
        self.SEEMORE_1.setObjectName("SEEMORE_1")
        self.SEEMORE_EXIT_1 = QtWidgets.QPushButton(self.SEEMORE_1)
        self.SEEMORE_EXIT_1.setGeometry(QtCore.QRect(1090, 6, 31, 28))
        self.SEEMORE_EXIT_1.setStyleSheet("background-color: rgb(255, 56, 49);")
        self.SEEMORE_EXIT_1.setObjectName("SEEMORE_EXIT_1")
        self.SEARCHALLPB_9 = QtWidgets.QPushButton(self.SEEMORE_1)
        self.SEARCHALLPB_9.setGeometry(QtCore.QRect(980, 790, 141, 41))
        self.SEARCHALLPB_9.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.SEARCHALLPB_9.setObjectName("SEARCHALLPB_9")
        self.tableWidget_search_2 = QtWidgets.QTableWidget(self.SEEMORE_1)
        self.tableWidget_search_2.setEnabled(True)
        self.tableWidget_search_2.setGeometry(QtCore.QRect(30, 36, 1081, 741))
        self.tableWidget_search_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_search_2.setColumnCount(1)
        self.tableWidget_search_2.setObjectName("tableWidget_search_2")
        self.tableWidget_search_2.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_2.setHorizontalHeaderItem(0, item)
        self.tableWidget_search_2.horizontalHeader().setVisible(False)
        self.tableWidget_search_2.horizontalHeader().setDefaultSectionSize(920)
        self.tableWidget_search_2.verticalHeader().setDefaultSectionSize(96)
        self.label_4 = QtWidgets.QLabel(self.SEEMORE_1)
        self.label_4.setGeometry(QtCore.QRect(50, 10, 241, 21))
        self.label_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.SEARCHALLPB_18 = QtWidgets.QPushButton(self.SEEMORE_1)
        self.SEARCHALLPB_18.setGeometry(QtCore.QRect(30, 790, 141, 41))
        self.SEARCHALLPB_18.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.SEARCHALLPB_18.setObjectName("SEARCHALLPB_18")
        self.SEARCHALLPB_9.raise_()
        self.SEEMORE_EXIT_1.raise_()
        self.tableWidget_search_2.raise_()
        self.label_4.raise_()
        self.SEARCHALLPB_18.raise_()
        self.SEARCHALLPB_14 = QtWidgets.QPushButton(self.search_menu)
        self.SEARCHALLPB_14.setGeometry(QtCore.QRect(1060, 180, 201, 41))
        self.SEARCHALLPB_14.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.SEARCHALLPB_14.setObjectName("SEARCHALLPB_14")
        self.tableWidget_search.raise_()
        self.SEARCHALLPB_7.raise_()
        self.label_7.raise_()
        self.lineEdit.raise_()
        self.label_8.raise_()
        self.SEARCHALLPB_8.raise_()
        self.MAINMENU_1.raise_()
        self.SEARCHALLPB_11.raise_()

        self.pushButton.raise_()
        self.SEARCHALLPB_14.raise_()
        self.SEEMORE_1.raise_()
        self.stackedWidget.addWidget(self.SEARCH_PG)
        self.FULLLIST_PG = QtWidgets.QWidget()
        self.FULLLIST_PG.setObjectName("FULLLIST_PG")
        self.bgwidget_3 = QtWidgets.QWidget(self.FULLLIST_PG)
        self.bgwidget_3.setGeometry(QtCore.QRect(0, 0, 1281, 921))
        self.bgwidget_3.setStyleSheet("QWidget#bgwidget_3{\n"
"background-color: qlineargradient(spread:pad, x1:0.551975, y1:0.341, x2:0.553, y2:1, stop:0.810945 rgba(0, 122, 201, 255), stop:1 rgba(255, 255, 255, 255));}\n"
"\n"
"")
        self.bgwidget_3.setObjectName("bgwidget_3")
        self.label_9 = QtWidgets.QLabel(self.bgwidget_3)
        self.label_9.setGeometry(QtCore.QRect(20, 20, 491, 61))
        self.label_9.setStyleSheet("font: 8pt \"AIGDT\";\n"
"font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.SEARCHALLPB_10 = QtWidgets.QPushButton(self.bgwidget_3)
        self.SEARCHALLPB_10.setGeometry(QtCore.QRect(1060, 810, 201, 41))
        self.SEARCHALLPB_10.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.SEARCHALLPB_10.setObjectName("SEARCHALLPB_10")
        self.SEARCHALLPB_13 = QtWidgets.QPushButton(self.bgwidget_3)
        self.SEARCHALLPB_13.setGeometry(QtCore.QRect(10, 190, 131, 41))
        self.SEARCHALLPB_13.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.SEARCHALLPB_13.setObjectName("SEARCHALLPB_13")
        self.MAINMENU_2 = QtWidgets.QPushButton(self.bgwidget_3)
        self.MAINMENU_2.setGeometry(QtCore.QRect(12, 817, 201, 41))
        self.MAINMENU_2.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.MAINMENU_2.setObjectName("MAINMENU_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.bgwidget_3)
        self.listWidget_2.setGeometry(QtCore.QRect(150, 110, 256, 121))
        self.listWidget_2.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_2.setBatchSize(101)
        self.listWidget_2.setWordWrap(True)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.tableWidget = QtWidgets.QTableWidget(self.bgwidget_3)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(10, 234, 1251, 541))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(134)
        self.SEEMORE_2 = QtWidgets.QWidget(self.bgwidget_3)
        self.SEEMORE_2.setGeometry(QtCore.QRect(0, 20, 1131, 851))
        self.SEEMORE_2.setStyleSheet("QWidget#SEEMORE_2{\n"
"background-color: qlineargradient(spread:pad, x1:0.551975, y1:0.341, x2:0.553, y2:1, stop:0.810945 rgba(0, 122, 201, 255), stop:1 rgba(255, 255, 255, 255)border-color: rgb(0, 0, 0))  ;}\n"
"\n"
"\n"
"")
        self.SEEMORE_2.setObjectName("SEEMORE_2")
        self.SEEMORE_EXIT_2 = QtWidgets.QPushButton(self.SEEMORE_2)
        self.SEEMORE_EXIT_2.setGeometry(QtCore.QRect(1090, 6, 31, 28))
        self.SEEMORE_EXIT_2.setStyleSheet("background-color: rgb(255, 56, 49);")
        self.SEEMORE_EXIT_2.setObjectName("SEEMORE_EXIT_2")
        self.SEARCHALLPB_12 = QtWidgets.QPushButton(self.SEEMORE_2)
        self.SEARCHALLPB_12.setGeometry(QtCore.QRect(980, 798, 141, 41))
        self.SEARCHALLPB_12.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.SEARCHALLPB_12.setObjectName("SEARCHALLPB_12")
        self.label_5 = QtWidgets.QLabel(self.SEEMORE_2)
        self.label_5.setGeometry(QtCore.QRect(30, 10, 241, 21))
        self.label_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.tableWidget_search_3 = QtWidgets.QTableWidget(self.SEEMORE_2)
        self.tableWidget_search_3.setEnabled(True)
        self.tableWidget_search_3.setGeometry(QtCore.QRect(10, 40, 1081, 751))
        self.tableWidget_search_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_search_3.setObjectName("tableWidget_search_3")
        self.tableWidget_search_3.setColumnCount(1)
        self.tableWidget_search_3.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_3.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_3.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_3.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_search_3.setHorizontalHeaderItem(0, item)
        self.tableWidget_search_3.horizontalHeader().setVisible(False)
        self.tableWidget_search_3.horizontalHeader().setDefaultSectionSize(920)
        self.tableWidget_search_3.verticalHeader().setDefaultSectionSize(96)
        self.SEARCHALLPB_17 = QtWidgets.QPushButton(self.SEEMORE_2)
        self.SEARCHALLPB_17.setGeometry(QtCore.QRect(10, 798, 141, 41))
        self.SEARCHALLPB_17.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.SEARCHALLPB_17.setObjectName("SEARCHALLPB_17")
        self.SEARCHALLPB_15 = QtWidgets.QPushButton(self.bgwidget_3)
        self.SEARCHALLPB_15.setGeometry(QtCore.QRect(1060, 186, 201, 41))
        self.SEARCHALLPB_15.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.SEARCHALLPB_15.setObjectName("SEARCHALLPB_15")
        self.label_9.raise_()
        self.SEARCHALLPB_10.raise_()
        self.SEARCHALLPB_13.raise_()
        self.MAINMENU_2.raise_()
        self.listWidget_2.raise_()
        self.tableWidget.raise_()
        self.SEARCHALLPB_15.raise_()
        self.SEEMORE_2.raise_()
        self.stackedWidget.addWidget(self.FULLLIST_PG)
        self.ADD_PG = QtWidgets.QWidget()
        self.ADD_PG.setObjectName("ADD_PG")
        self.bgwidget_4 = QtWidgets.QWidget(self.ADD_PG)
        self.bgwidget_4.setGeometry(QtCore.QRect(0, 0, 1271, 871))
        self.bgwidget_4.setStyleSheet("QWidget#bgwidget_4{\n"
"background-color: qlineargradient(spread:pad, x1:0.551975, y1:0.341, x2:0.553, y2:1, stop:0.810945 rgba(0, 122, 201, 255), stop:1 rgba(255, 255, 255, 255));}\n"
"\n"
"")
        self.bgwidget_4.setObjectName("bgwidget_4")
        self.label_10 = QtWidgets.QLabel(self.bgwidget_4)
        self.label_10.setGeometry(QtCore.QRect(20, 20, 491, 61))
        self.label_10.setStyleSheet("font: 8pt \"AIGDT\";\n"
"font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.SEARCHALLPB_16 = QtWidgets.QPushButton(self.bgwidget_4)
        self.SEARCHALLPB_16.setGeometry(QtCore.QRect(1000, 680, 201, 41))
        self.SEARCHALLPB_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SEARCHALLPB_16.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.SEARCHALLPB_16.setObjectName("SEARCHALLPB_16")
        self.MAINMENU_3 = QtWidgets.QPushButton(self.bgwidget_4)
        self.MAINMENU_3.setGeometry(QtCore.QRect(10, 682, 201, 41))
        self.MAINMENU_3.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.MAINMENU_3.setObjectName("MAINMENU_3")
        self.label_41 = QtWidgets.QLabel(self.bgwidget_4)
        self.label_41.setGeometry(QtCore.QRect(10, 200, 211, 41))
        self.label_41.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.bgwidget_4)
        self.label_42.setGeometry(QtCore.QRect(10, 317, 211, 41))
        self.label_42.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.bgwidget_4)
        self.label_43.setGeometry(QtCore.QRect(10, 258, 171, 41))
        self.label_43.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.bgwidget_4)
        self.label_44.setGeometry(QtCore.QRect(10, 380, 171, 41))
        self.label_44.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_44.setObjectName("label_44")
        self.label_51 = QtWidgets.QLabel(self.bgwidget_4)
        self.label_51.setGeometry(QtCore.QRect(730, 260, 171, 41))
        self.label_51.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.bgwidget_4)
        self.label_52.setGeometry(QtCore.QRect(730, 318, 171, 41))
        self.label_52.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.bgwidget_4)
        self.label_53.setGeometry(QtCore.QRect(730, 377, 171, 41))
        self.label_53.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_53.setObjectName("label_53")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.bgwidget_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 270, 241, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.bgwidget_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 330, 241, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.bgwidget_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(240, 390, 241, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.bgwidget_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(990, 270, 211, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.bgwidget_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(990, 330, 211, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.bgwidget_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(990, 390, 211, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_54 = QtWidgets.QLabel(self.bgwidget_4)
        self.label_54.setGeometry(QtCore.QRect(730, 200, 221, 41))
        self.label_54.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_54.setObjectName("label_54")
        self.SEARCHALLPB_33 = QtWidgets.QPushButton(self.bgwidget_4)
        self.SEARCHALLPB_33.setGeometry(QtCore.QRect(10, 450, 201, 41))
        self.SEARCHALLPB_33.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.SEARCHALLPB_33.setObjectName("SEARCHALLPB_33")
        self.SEARCHALLPB_34 = QtWidgets.QPushButton(self.bgwidget_4)
        self.SEARCHALLPB_34.setGeometry(QtCore.QRect(10, 500, 201, 41))
        self.SEARCHALLPB_34.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.SEARCHALLPB_34.setObjectName("SEARCHALLPB_34")
        self.comboBox = QtWidgets.QComboBox(self.bgwidget_4)
        self.comboBox.setGeometry(QtCore.QRect(350, 200, 51, 41))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.bgwidget_4)
        self.comboBox_2.setGeometry(QtCore.QRect(240, 200, 81, 41))
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.spinBox = QtWidgets.QSpinBox(self.bgwidget_4)
        self.spinBox.setGeometry(QtCore.QRect(430, 200, 51, 41))
        self.spinBox.setObjectName("spinBox")
        self.comboBox_3 = QtWidgets.QComboBox(self.bgwidget_4)
        self.comboBox_3.setGeometry(QtCore.QRect(990, 200, 211, 41))
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(0, "")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.widget = QtWidgets.QWidget(self.bgwidget_4)




        self.widget.setGeometry(QtCore.QRect(240, 450, 511, 291))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")

        self.picwidget = QtWidgets.QWidget(Dialog)
        self.picwidget.setGeometry(QtCore.QRect(240, 450, 511, 291))
        self.picwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.picwidget.setObjectName("picwidget")






        # Set up a layout inside picwidget
        self.picwidget_layout = QVBoxLayout(self.picwidget)

        # Create an instance of ImageDropZone and add it to the layout
        self.image_drop_zone = ImageDropZone()
        self.picwidget_layout.addWidget(self.image_drop_zone)



        self.label_91 = QtWidgets.QLabel(self.widget)
        self.label_91.setGeometry(QtCore.QRect(10, 0, 191, 41))
        self.label_91.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_91.setObjectName("label_91")




        self.label_93 = QtWidgets.QLabel(self.widget)
        self.label_93.setGeometry(QtCore.QRect(210, 100, 21, 20))
        self.label_93.setLineWidth(-7)
        self.label_93.setObjectName("label_93")
        self.tableWidget_SPECIAL = QtWidgets.QTableWidget(self.widget)
        self.tableWidget_SPECIAL.setGeometry(QtCore.QRect(10, 40, 475,  231))
        self.tableWidget_SPECIAL.setToolTipDuration(3)
        self.tableWidget_SPECIAL.setObjectName("tableWidget_SPECIAL")
        self.tableWidget_SPECIAL.setColumnCount(2)
        self.tableWidget_SPECIAL.setRowCount(20)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_SPECIAL.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_SPECIAL.setHorizontalHeaderItem(1, item)
        self.tableWidget_SPECIAL.horizontalHeader().setDefaultSectionSize(212)
        self.stackedWidget.addWidget(self.ADD_PG)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        header = self.tableWidget_search.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget_search.setColumnWidth(self.tableWidget_search.columnCount() - 1, 1)
        header.setStretchLastSection(True)

        self.SEARCHALLPB.clicked.connect(self.go_to_search_page)
        self.VIEWSTOCKPB.clicked.connect(self.go_to_full_list_page)
        self.ADDPB.clicked.connect(self.go_to_add_page)
        self.MAINMENU_1.clicked.connect(self.go_to_welcome_page)
        self.MAINMENU_2.clicked.connect(self.go_to_welcome_page)
        self.MAINMENU_3.clicked.connect(self.go_to_welcome_page)

        self.SEARCHALLPB_16.clicked.connect(self.go_to_welcome_page) #take out

        self.SEARCHALLPB_11.clicked.connect(self.toggleSearchControls)
        self.SEARCHALLPB_13.clicked.connect(self.toggleSortList)

        self.SEARCHALLPB_33.clicked.connect(self.toggleWidget)
        self.SEARCHALLPB_34.clicked.connect(self.togglePicWidget)

        self.widget.setVisible(False)
        self.picwidget.setVisible(False)



        self.SEEMORE_1.setVisible(False)
        self.SEEMORE_2.setVisible(False)
        self.listWidget_tags.setVisible(False)
        self.pushButton.setVisible(False)
        self.listWidget_2.setVisible(False)


        self.SEARCHALLPB_7.clicked.connect(self.performDatabaseSearch)

        self.SEEMORE_EXIT_1.clicked.connect(self.on_seemore_exit_1_clicked)
        self.SEEMORE_EXIT_2.clicked.connect(self.on_seemore_exit_2_clicked)



        self.populateTableWidget()

        self.SEARCHALLPB_14.clicked.connect(self.saveTableChanges)
        self.SEARCHALLPB_15.clicked.connect(self.saveTableChanges)


        self.pushButton.clicked.connect(self.filterByTag)
        self.populateComboBox()

        self.SEARCHALLPB_16.clicked.connect(self.on_submit)

    def go_to_search_page(self):
        self.stackedWidget.setCurrentWidget(self.SEARCH_PG)

    def go_to_full_list_page(self):
        self.stackedWidget.setCurrentWidget(self.FULLLIST_PG)

    def go_to_add_page(self):
        self.stackedWidget.setCurrentWidget(self.ADD_PG)

    def go_to_welcome_page(self):
        self.stackedWidget.setCurrentWidget(self.WELCOME_PG)
        self.picwidget.setVisible(False)

    def toggleSearchControls(self):
            self.listWidget_tags.setVisible(not self.listWidget_tags.isVisible())
            self.pushButton.setVisible(not self.pushButton.isVisible())

    def toggleSortList(self):
            self.listWidget_2.setVisible(not self.listWidget_2.isVisible())

    def toggleWidget(self):
        # Hide picwidget if it's visible
        if self.picwidget.isVisible():
            self.picwidget.setVisible(False)
        # Toggle widget visibility
        self.widget.setVisible(not self.widget.isVisible())

    def togglePicWidget(self):
        # Hide widget if it's visible
        if self.widget.isVisible():
            self.widget.setVisible(False)
        # Toggle picwidget visibility
        self.picwidget.setVisible(not self.picwidget.isVisible())

    def on_seemore_exit_1_clicked(self):
            self.hideSeeMoreWidget()

    def hideSeeMoreWidget(self):
            self.SEEMORE_1.setVisible(False)
            # Clear the second column of tableWidget_search_2
            for row in range(self.tableWidget_search_2.rowCount()):
                    self.tableWidget_search_2.setItem(row, 1, QtWidgets.QTableWidgetItem(""))

    def on_seemore_exit_2_clicked(self):
            self.hideSeeMoreWidget_2()

    def hideSeeMoreWidget_2(self):
            self.SEEMORE_2.setVisible(False)
            # Clear the second column of tableWidget_search_2
            for row in range(self.tableWidget_search_3.rowCount()):
                    self.tableWidget_search_3.setItem(row, 1, QtWidgets.QTableWidgetItem(""))

    def performDatabaseSearch(self):
            # Initialize the cache for original data
            self.original_data = []

            search_text = self.lineEdit.text().lower()
            if not search_text.strip():  # Checks for both empty string and strings made up of only spaces
                    return

            db_path = "OCWA_AAF.db"
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()

            keywords = search_text.split()

            # Construct the dynamic query based on the number of keywords and columns
            query_parts = []
            params = []

            columns = ["ROOM", "\"SHELF LOCATION\"", "NAME", "MANUFACTURER", "\"ITEM no\"", "DESCRIPTION", "QUANTITY",
                       "TAGS"]
            for col in columns:
                    keyword_conditions = []
                    for keyword in keywords:
                            keyword_conditions.append(f"LOWER({col}) LIKE ?")
                            params.append('%' + keyword + '%')
                    query_parts.append("(" + " OR ".join(keyword_conditions) + ")")

            query = f"""
        SELECT * FROM OCWA_AAF
        WHERE {' OR '.join(query_parts)}
        """

            cursor.execute(query, params)
            data = cursor.fetchall()
            connection.close()

            # Assign a score for each record by counting the number of matching keywords
            scored_data = []
            for record in data:
                    score = sum([sum([1 if keyword in str(value).lower() else 0 for keyword in keywords]) for value in
                                 record[:-1]])
                    scored_data.append((score, record))

            # Sort the records based on their scores in descending order
            sorted_data = sorted(scored_data, key=lambda x: x[0], reverse=True)
            sorted_records = [record for _, record in sorted_data]

            # Populate the table with the sorted data
            self.tableWidget_search.setRowCount(len(sorted_records))
            for row, record in enumerate(sorted_records):
                    row_data = {}
                    for col, value in enumerate(record[:-1]):  # We exclude the last item which is ID
                            column_name = self.tableWidget_search.horizontalHeaderItem(col).text()
                            row_data[column_name] = str(value)

                            item = QtWidgets.QTableWidgetItem(str(value))
                            self.tableWidget_search.setItem(row, col, item)

                    # Add the "SEE MORE" button in the second to last column
                    button = QPushButton("SEE MORE")
                    button.setFixedWidth(115)
                    button.clicked.connect(lambda _, row=row: self.showSeeMoreWidget(row))
                    self.tableWidget_search.setCellWidget(row, len(record) - 1,
                                                          button)  # Adjusted column index for SEE MORE

                    # Add the ID in the last column
                    id_item = QtWidgets.QTableWidgetItem(str(record[-1]))
                    self.tableWidget_search.setItem(row, len(record) - 0, id_item)

                    row_data["ID"] = str(record[-1])
                    self.original_data.append(row_data)

    def saveTableChanges(self):
            print("Saving...")

            db_path = "OCWA_AAF.db"
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()

            changed_rows = []

            print("Saving 1.5...")

            for row in range(self.tableWidget_search.rowCount()):
                    print(f"Fetching primary key for row {row}.")
                    primary_key = self.original_data[row]['ID']
                    print(f"Row: {row}, Primary Key: {primary_key}")
                    changes = {}

                    for col in range(self.tableWidget_search.columnCount()):
                            if col == self.tableWidget_search.columnCount() - 1:
                                    column_name = 'ID'
                            else:
                                    column_name = self.tableWidget_search.horizontalHeaderItem(col).text()

                            item = self.tableWidget_search.item(row, col)
                            new_value = item.text() if item else "EMPTY_ITEM"

                            print(f"Checking for column '{column_name}' in original data for row {row}.")
                            if column_name in self.original_data[row]:
                                    if self.original_data[row][column_name] != new_value:
                                            changes[column_name] = new_value
                            else:
                                    print(f"Column '{column_name}' not found in original data for row {row}.")

                    if changes:
                            changes["ID"] = primary_key
                            changed_rows.append(changes)

            print("Finished gathering changed rows...")

            # Start the transaction for batch updates
            connection.execute('BEGIN')

            for change in changed_rows:
                    columns_to_update = ", ".join(f"{col} = ?" for col in change.keys() if col != "ID")
                    values = [change[col] for col in change.keys() if col != "ID"]
                    values.append(change["ID"])

                    try:
                            cursor.execute(f"UPDATE OCWA_AAF SET {columns_to_update} WHERE ID = ?", values)
                    except Exception as e:  # This will capture any database-related exceptions
                            print(f"Error encountered while updating ID {change['ID']}: {e}")

            # Commit the transaction after all updates
            connection.commit()
            connection.close()

            print("Saving finished...")

    def populateTableWidget(self):
            db_path = "OCWA_AAF.db"  # Replace with the actual database file path
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()

            query = "SELECT * FROM OCWA_AAF"  # Replace with your query

            cursor.execute(query)
            data = cursor.fetchall()
            connection.close()

            self.tableWidget.setRowCount(len(data))
            for row, record in enumerate(data):
                    for col, value in enumerate(record):
                            item = QtWidgets.QTableWidgetItem(str(value))
                            self.tableWidget.setItem(row, col, item)

                    button = QPushButton("SEE MORE")
                    button.setFixedWidth(115)
                    button.clicked.connect(
                            lambda _, row=row: self.showSeeMoreWidget_2(row)
                    )
                    self.tableWidget.setCellWidget(
                            row, self.tableWidget.columnCount() - 1, button
                    )

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.find_image_directory()

    def showSeeMoreWidget_2(self, row):
            print("See more clicked!")  # Print statement to check function call
            self.openAssociatedImage(row, self.tableWidget)

            for r in range(self.tableWidget_search_3.rowCount()):
                    self.tableWidget_search_3.setItem(r, 1, QtWidgets.QTableWidgetItem(""))

            # Explicit order mapping
            order_mapping = {
                    0: 4,
                    1: 5,
                    2: 0,
                    3: 1,
                    4: 2,
                    7: 3,
                    5: 6,
                    6: 7
            }

            # Get data based on the mapping
            for source_col, target_row in order_mapping.items():
                    value = self.tableWidget.item(row, source_col).text()
                    self.tableWidget_search_3.setItem(target_row, 0, QtWidgets.QTableWidgetItem(value))

                    # Resize the height of the current row to fit its content
                    self.tableWidget_search_3.resizeRowToContents(target_row)

                    # Check and set minimum height if required
                    min_height = 81  # adjust this value as per your needs
                    if self.tableWidget_search_3.rowHeight(target_row) < min_height:
                            self.tableWidget_search_3.setRowHeight(target_row, min_height)

            # Show the SEEMORE_1 widget
            self.SEEMORE_2.setVisible(True)


    def showSeeMoreWidget(self, row):
            print("See more clicked!")  # Print statement to check function call

            self.openAssociatedImage(row, self.tableWidget_search)

            for r in range(self.tableWidget_search_2.rowCount()):
                    self.tableWidget_search_2.setItem(r, 1, QtWidgets.QTableWidgetItem(""))

            # Explicit order mapping
            order_mapping = {
                    0: 4,
                    1: 5,
                    2: 0,
                    3: 1,
                    4: 2,
                    7: 3,
                    5: 6,
                    6: 7
            }

            # Get data based on the mapping
            for source_col, target_row in order_mapping.items():
                    value = self.tableWidget_search.item(row, source_col).text()
                    self.tableWidget_search_2.setItem(target_row, 0, QtWidgets.QTableWidgetItem(value))

                    # Resize the height of the current row to fit its content
                    self.tableWidget_search_2.resizeRowToContents(target_row)

                    # Check and set minimum height if required
                    min_height = 81  # adjust this value as per your needs
                    if self.tableWidget_search_2.rowHeight(target_row) < min_height:
                            self.tableWidget_search_2.setRowHeight(target_row, min_height)

            # Show the SEEMORE_1 widget
            self.SEEMORE_1.setVisible(True)

    def available_drives(self):
            """Return a list of available drives."""
            drive_bitmask = 2 ** (len(string.ascii_uppercase) - 1) - 1
            return [
                    drive + ":/" for drive in string.ascii_uppercase if os.path.exists(drive + ":/")
            ]

    def find_image_directory(self):
            """Find the OCWA_INV_PICTURES directory."""
            drives = self.available_drives()
            print(f"Searching in drives: {drives}")  # Check the drives it's searching in

            for drive in drives:
                    for dirpath, dirnames, filenames in os.walk(drive):
                            if "OCWA_INV_PICTURES" in dirnames:
                                    self.image_directory = os.path.join(dirpath, "OCWA_INV_PICTURES")
                                    print(f"Found image directory at: {self.image_directory}")  # <-- Added print
                                    return

            self.image_directory = None
            print("Image directory not found!")  # <-- Added print
        
        
    def openAssociatedImage(self, row, tableWidget):
            """Open the associated image for a given table row."""
            # Retrieve the ID
            item_id = tableWidget.item(row, tableWidget.columnCount() - 1).text()
            print(f"Retrieved Item ID: {item_id}")  # <-- Added print
            # Check if we found the image directory
            if not self.image_directory:
                    print("Image directory not set!")  # <-- Added print
                    return

            # Construct the image path
            image_path = os.path.join(self.image_directory, f"OCWA_INV_PIC_{item_id}.jpg")
            print(f"Constructed image path: {image_path}")  # <-- Added print

            # Check if image exists and open it using the default viewer
            if os.path.exists(image_path):
                    os.system(f'start "" "{image_path}"')  # Comment this line
                    print(f"Would have opened: {image_path}")

    def populateComboBox(self):
            # Connect to the database
            db_path = "OCWA_AAF.db"
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()

            # Fetch unique tags
            cursor.execute("SELECT DISTINCT TAGS FROM OCWA_AAF")
            unique_tags = [row[0] for row in cursor.fetchall()]

            # Close the connection
            connection.close()

            # Populate the listWidget_tags with checkboxes
            self.listWidget_tags.clear()
            for tag in unique_tags:
                    item = QtWidgets.QListWidgetItem(str(tag))

                    item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                    item.setCheckState(QtCore.Qt.Unchecked)
                    self.listWidget_tags.addItem(item)

    def filterByTag(self):
            selected_tags = [self.listWidget_tags.item(i).text() for i in range(self.listWidget_tags.count()) if
                             self.listWidget_tags.item(i).checkState() == QtCore.Qt.Checked]

            # Rest of your code remains the same

            print(f"Selected Tags: {selected_tags}")  # Diagnostic print

            # Connect to the database
            db_path = "OCWA_AAF.db"
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()

            # Fetch all items
            cursor.execute("SELECT * FROM OCWA_AAF")
            data = cursor.fetchall()

            # Close the connection
            connection.close()

            print(f"Total records fetched: {len(data)}")  # Diagnostic print

            # Sort data based on tags, items with matching tags will be prioritized
            data.sort(key=lambda x: any(tag in x[6] for tag in selected_tags),
                      reverse=True)  # Assuming TAGS column is index 6
            print(f"First 5 records after sorting: {data[:5]}")  # Diagnostic print

            # Clear previous items from tableWidget_search_2
            self.tableWidget_search.setRowCount(0)
            self.tableWidget_search.setRowCount(len(data))

            for row, record in enumerate(data):
                    for col, value in enumerate(record):
                            item = QtWidgets.QTableWidgetItem(str(value))
                            self.tableWidget_search.setItem(row, col, item)

            print("Table populated")  # Diagnostic print

    def gather_description(self):
            # First, grab the current text from the lineEdit for column 8
            description_base = self.lineEdit_6.text()

            # Initialize an empty list to hold the string components
            description_items = [description_base]

            # Let's say you have a QTableWidget named tableWidget_SPECIAL
            # Loop through its rows to gather the description
            for row in range(self.tableWidget_SPECIAL.rowCount()):
                    unit_item = self.tableWidget_SPECIAL.item(row, 0)
                    value_item = self.tableWidget_SPECIAL.item(row, 1)

                    if unit_item and value_item:  # Check if both items are not None
                            unit = unit_item.text()
                            value = value_item.text()
                            description_items.append(f"{unit}: {value}")

            # Join each component with a newline to create the full description
            full_description = '\n'.join(description_items)

            return full_description

    def get_data_from_form(self):
            # Get the individual values
            value_from_comboBox_2 = self.comboBox_2.currentText()
            value_from_comboBox = self.comboBox.currentText()
            value_from_spinBox = str(self.spinBox.value())

            # Combine the values as needed
            column_2_data = f"{value_from_comboBox_2} {value_from_comboBox}-{value_from_spinBox}"

            # Rest of the data extraction remains the same
            column_3_data = self.lineEdit_3.text()
            column_1_data = self.comboBox_3.currentText()
            column_4_data = self.lineEdit_4.text()
            column_5_data = self.lineEdit_5.text()
            column_8_data = self.lineEdit_6.text()
            column_6_data = self.lineEdit_7.text()
            column_7_data = self.lineEdit_9.text()
            column_8_data = self.gather_description()

            print("Get data check")
            return column_1_data, column_2_data, column_3_data, column_4_data, column_5_data, column_6_data, column_7_data, column_8_data

    def insert_data_into_db(self, data):
            with sqlite3.connect("OCWA_AAF.db") as connection:
                    cursor = connection.cursor()
                    sql = """INSERT INTO OCWA_AAF ("ROOM", "SHELF LOCATION", "NAME", "MANUFACTURER", "ITEM no", "QUANTITY", "TAGS", "DESCRIPTION")
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
                    cursor.execute(sql, data)
                    return cursor.lastrowid  # return the last row id


    def clear_form(self):
            self.lineEdit_3.clear()
            self.comboBox_2.setCurrentIndex(0)
            self.comboBox_3.setCurrentIndex(0)
            self.comboBox.setCurrentIndex(0)
            self.spinBox.setValue(0)
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.lineEdit_9.clear()
            self.tableWidget_SPECIAL.clearContents()
            print("clear form check")
            self.image_drop_zone.clear_image()  # Clear the dropped image

    def on_submit(self):
            try:
                    data = self.get_data_from_form()
                    last_row_id = self.insert_data_into_db(data)  # Get the last inserted row id

                    # Check if there's a dropped image and save it
                    if hasattr(self.image_drop_zone, 'current_image_path'):
                            image_folder_path = os.path.join(os.getcwd(), "OCWA_INV_PICTURES")
                            new_image_path = os.path.join(image_folder_path, f"OCWA_INV_PIC_{last_row_id}.jpg")

                            if not os.path.exists(image_folder_path):
                                    os.makedirs(image_folder_path)

                            shutil.copy2(self.image_drop_zone.current_image_path, new_image_path)

                    self.clear_form()
            except Exception as e:
                    print(f"Error: {e}")


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Welcome"))
        self.label.setText(_translate("Dialog", "EI Inventory"))
        self.label_3.setText(_translate("Dialog", "OCWA"))
        self.SEARCHALLPB.setText(_translate("Dialog", "SEARCH ALL"))
        self.VIEWSTOCKPB.setText(_translate("Dialog", "VIEW STOCK"))
        self.ADDPB.setText(_translate("Dialog", "ADD"))
        self.SENDSTOCKPB_1.setText(_translate("Dialog", "SEND STOCK"))
        self.SEARCHALLPB_7.setText(_translate("Dialog", "SEARCH"))
        self.label_7.setText(_translate("Dialog", "SEARCH MENU"))
        self.label_8.setText(_translate("Dialog", "Incluce as much key words as possible"))
        self.SEARCHALLPB_8.setText(_translate("Dialog", "SEND AS PDF"))
        self.MAINMENU_1.setText(_translate("Dialog", "Main Menu"))
        self.SEARCHALLPB_11.setText(_translate("Dialog", "TAG SEARCH"))
        item = self.tableWidget_search.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ROOM"))
        item = self.tableWidget_search.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "SHELF LOCATION"))
        item = self.tableWidget_search.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "NAME"))
        item = self.tableWidget_search.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "MANUFACTURER"))
        item = self.tableWidget_search.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "ITEM no"))
        item = self.tableWidget_search.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "QUANTITY"))
        item = self.tableWidget_search.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "TAGS"))
        item = self.tableWidget_search.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "DESCRIPTION"))
        self.pushButton.setText(_translate("Dialog", "SEARCH"))
        self.SEEMORE_EXIT_1.setText(_translate("Dialog", "X"))
        self.SEARCHALLPB_9.setText(_translate("Dialog", "SEND AS PDF"))
        item = self.tableWidget_search_2.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "NAME"))
        item = self.tableWidget_search_2.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "MANUFACTURER"))
        item = self.tableWidget_search_2.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "ITEM no."))
        item = self.tableWidget_search_2.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "DESCRIPTION"))
        item = self.tableWidget_search_2.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "ROOM"))
        item = self.tableWidget_search_2.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "SHELF LOCATION"))
        item = self.tableWidget_search_2.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "QUANTITY"))
        item = self.tableWidget_search_2.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "TAGS"))
        self.label_4.setText(_translate("Dialog", "ITEM INFORMATION"))
        self.SEARCHALLPB_18.setText(_translate("Dialog", "SAVE CHANGES"))
        self.SEARCHALLPB_14.setText(_translate("Dialog", "SAVE CHANGES"))
        self.label_9.setText(_translate("Dialog", "FULL STOCK LIST"))
        self.SEARCHALLPB_10.setText(_translate("Dialog", "SEND AS PDF"))
        self.SEARCHALLPB_13.setText(_translate("Dialog", "SORT BY"))
        self.MAINMENU_2.setText(_translate("Dialog", "Main Menu"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("Dialog", "ROOM LOCATION"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("Dialog", "TAGS"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("Dialog", "NAME"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("Dialog", "MANUFACTURER"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("Dialog", "QUANTITY"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ROOM"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "SHELF LOCATION"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "NAME"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "MANUFACTURER"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "ITEM no"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "DESCRIPTION"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "QUANTITY"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "TAGS"))
        self.SEEMORE_EXIT_2.setText(_translate("Dialog", "X"))
        self.SEARCHALLPB_12.setText(_translate("Dialog", "SEND AS PDF"))
        self.label_5.setText(_translate("Dialog", "ITEM INFORMATION"))
        item = self.tableWidget_search_3.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "NAME"))
        item = self.tableWidget_search_3.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "MANUFACTURER"))
        item = self.tableWidget_search_3.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "ITEM no."))
        item = self.tableWidget_search_3.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "DESCRIPTION"))
        item = self.tableWidget_search_3.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "ROOM"))
        item = self.tableWidget_search_3.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "SHELF LOCATION"))
        item = self.tableWidget_search_3.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "QUANTITY"))
        item = self.tableWidget_search_3.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "TAGS"))
        self.SEARCHALLPB_17.setText(_translate("Dialog", "SAVE CHANGES"))
        self.SEARCHALLPB_15.setText(_translate("Dialog", "SAVE CHANGES"))
        self.label_10.setText(_translate("Dialog", "ADD ITEM"))
        self.SEARCHALLPB_16.setText(_translate("Dialog", "ADD ITEM"))
        self.MAINMENU_3.setText(_translate("Dialog", "Main Menu"))
        self.label_41.setText(_translate("Dialog", "SHELF LOCATION"))
        self.label_42.setText(_translate("Dialog", "MANUFACTURER"))
        self.label_43.setText(_translate("Dialog", "ITEM CLASS"))
        self.label_44.setText(_translate("Dialog", "MODEL no."))
        self.label_51.setText(_translate("Dialog", "DESCRIPTION"))
        self.label_52.setText(_translate("Dialog", "QUANTITY"))
        self.label_53.setText(_translate("Dialog", "ITEM TAGS"))
        self.label_54.setText(_translate("Dialog", "ROOM LOCATION"))
        self.SEARCHALLPB_33.setText(_translate("Dialog", "SPECIAL ITEM"))
        self.SEARCHALLPB_34.setText(_translate("Dialog", "ADD PICTURE"))
        self.comboBox.setItemText(1, _translate("Dialog", "A"))
        self.comboBox.setItemText(2, _translate("Dialog", "B"))
        self.comboBox.setItemText(3, _translate("Dialog", "C"))
        self.comboBox.setItemText(4, _translate("Dialog", "D"))
        self.comboBox.setItemText(5, _translate("Dialog", "E"))
        self.comboBox.setItemText(6, _translate("Dialog", "F"))
        self.comboBox.setItemText(7, _translate("Dialog", "G"))
        self.comboBox.setItemText(8, _translate("Dialog", "H"))
        self.comboBox.setItemText(9, _translate("Dialog", "I"))
        self.comboBox.setItemText(10, _translate("Dialog", "J"))
        self.comboBox.setItemText(11, _translate("Dialog", "K"))
        self.comboBox.setItemText(12, _translate("Dialog", "L"))
        self.comboBox.setItemText(13, _translate("Dialog", "M"))
        self.comboBox.setItemText(14, _translate("Dialog", "N"))
        self.comboBox.setItemText(15, _translate("Dialog", "O"))
        self.comboBox.setItemText(16, _translate("Dialog", "P"))
        self.comboBox.setItemText(17, _translate("Dialog", "Q"))
        self.comboBox.setItemText(18, _translate("Dialog", "R"))
        self.comboBox.setItemText(19, _translate("Dialog", "S"))
        self.comboBox.setItemText(20, _translate("Dialog", "T"))
        self.comboBox.setItemText(21, _translate("Dialog", "U"))
        self.comboBox.setItemText(22, _translate("Dialog", "V"))
        self.comboBox.setItemText(23, _translate("Dialog", "W"))
        self.comboBox.setItemText(24, _translate("Dialog", "X"))
        self.comboBox.setItemText(25, _translate("Dialog", "Y"))
        self.comboBox.setItemText(26, _translate("Dialog", "Z"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "GREEN"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "BLUE"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "RED"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "GRAY"))
        self.comboBox_2.setItemText(5, _translate("Dialog", "YELLOW"))
        self.comboBox_2.setItemText(6, _translate("Dialog", "CABINET"))
        self.comboBox_2.setItemText(7, _translate("Dialog", "WHITE"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "KITCHEN ELECTRICAL"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "COMPLEX CAGE"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "BASEMENT CAGE"))
        self.comboBox_3.setItemText(4, _translate("Dialog", "MOTOR ROOM"))
        self.label_91.setText(_translate("Dialog", "SPECIAL ITEM"))


        self.label_93.setText(_translate("Dialog", ":"))
        item = self.tableWidget_SPECIAL.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "UNIT"))
        item = self.tableWidget_SPECIAL.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "VALUE"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
