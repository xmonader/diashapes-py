# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diashapes.ui'
#
# Created: Fri Jul 26 01:15:24 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 472)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.diatable = QTableWidget(self.centralwidget)
        self.diatable.setObjectName("diatable")
        self.verticalLayout.addWidget(self.diatable)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnInstall = QPushButton(self.centralwidget)
        self.btnInstall.setObjectName("btnInstall")
        self.horizontalLayout.addWidget(self.btnInstall)
        self.btnUpdate = QPushButton(self.centralwidget)
        self.btnUpdate.setObjectName("btnUpdate")
        self.horizontalLayout.addWidget(self.btnUpdate)
        self.btnSearch = QPushButton(self.centralwidget)
        self.btnSearch.setObjectName("btnSearch")
        self.horizontalLayout.addWidget(self.btnSearch)
        self.btnAbout = QPushButton(self.centralwidget)
        self.btnAbout.setObjectName("btnAbout")
        self.horizontalLayout.addWidget(self.btnAbout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 27))
        self.menubar.setObjectName("menubar")
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCheck_update = QAction(MainWindow)
        self.actionCheck_update.setObjectName("actionCheck_update")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.menu_File.addAction(self.actionCheck_update)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionExit)
        self.menu_Help.addAction(self.actionAbout)
        self.menu_Help.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QApplication.translate("MainWindow", "MainWindow", None))
        self.btnInstall.setText(QApplication.translate("MainWindow", "Install", None))
        self.btnUpdate.setText(QApplication.translate("MainWindow", "Update", None))
        self.btnSearch.setText(QApplication.translate("MainWindow", "Search", None))
        self.btnAbout.setText(QApplication.translate("MainWindow", "About", None))
        self.menu_File.setTitle(QApplication.translate("MainWindow", "&File", None))
        self.menu_Help.setTitle(QApplication.translate("MainWindow", "&Help", None))
        self.actionCheck_update.setText(QApplication.translate("MainWindow", "Check update", None))
        self.actionExit.setText(QApplication.translate("MainWindow", "E&xit", None))
        self.actionAbout.setText(QApplication.translate("MainWindow", "About", None))
        self.actionAbout_Qt.setText(QApplication.translate("MainWindow", "About Qt", None))

