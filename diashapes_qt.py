import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
#from PySide import QtCore, QtGui
from diashapes_ui import Ui_MainWindow as UIMW

from diashapes import open_search_page, open_download_page, get_sheets_data, update_available, install_sheets


class DiaShapesWindow(QMainWindow, UIMW):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.btnInstall.setEnabled(False)
        self.diasheets = get_sheets_data()
        self.diatable.setColumnCount(6)
        self.diatable.setRowCount(len(self.diasheets))
        self.diatable.setHorizontalHeaderLabels(
            ["Name", "Desc", "Creator", "Website", "Download", "Selected"])

        self.installationprogress = QProgressBar()

        self.prepare_diasheets()
        # AFTER PREPARING DIASHEETS
        self.diatable.cellChanged.connect(self.on_cell_changed)
        # self.connect(self.diatable, QtCore.SIGNAL(
        #     'cellChanged(int,int)'), self.on_cell_changed)

        self.__setupConnections()

    def __setupConnections(self):
        self.btnInstall.clicked.connect(self.on_install_clicked)
        self.btnUpdate.clicked.connect(self.on_update_clicked)
        self.btnSearch.clicked.connect(self.on_search_clicked)
        self.btnAbout.clicked.connect(self.on_about)

        # self.connect(self.btnInstall, QtCore.SIGNAL(
        #     'clicked()'), self.on_install_clicked)
        # self.connect(self.btnUpdate, QtCore.SIGNAL(
        #     'clicked()'), self.on_update_clicked)
        # self.connect(self.btnSearch, QtCore.SIGNAL(
        #     'clicked()'), self.on_search_clicked)
        # self.connect(self.btnAbout, QtCore.SIGNAL('clicked()'), self.on_about)
        self.actionAbout.triggered.connect(self.on_about)
        self.actionAbout_Qt.triggered.connect(
            lambda: QMessageBox.aboutQt(self, "About Qt"))
        self.actionExit.triggered.connect(qApp.quit)
        self.actionCheck_update.triggered.connect(self.on_update_clicked)

    def prepare_diasheets(self):

        for ridx, r in enumerate(self.diasheets):
            for cidx, c in enumerate(r):
                item = QTableWidgetItem()

                if cidx == 5:
                    item.setFlags(
                        QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsSelectable)
                    item.setCheckState(QtCore.Qt.Unchecked)
                else:
                    item.setText(c)
                self.diatable.setItem(ridx, cidx, item)

    def on_cell_changed(self, row, col):
        if not self.btnInstall.isEnabled():
            self.btnInstall.setEnabled(True)
        if col == 5:
            # print "BEFORE:", self.diasheets[row]
            self.diasheets[row][col] = not self.diasheets[row][col]
            # print "AFTER:", self.diasheets[row]

    def on_install_clicked(self):
        toinstall = [x for x in self.diasheets if x[5]]
        # print "Items to install: ", toinstall

        self.installationprogress.setRange(0, len(toinstall))
        self.statusbar.addWidget(self.installationprogress)
        for idx in install_sheets(toinstall):
            self.installationprogress.setValue(idx + 1)

        self.statusbar.removeWidget(self.installationprogress)
        self.statusbar.showMessage(
            str(len(toinstall)) + " shapes installed successfully.")

    def on_update_clicked(self):
        if update_available():
            self.statusbar.showMessage("Update available")
            reply = QMessageBox.question(self, 'Update available', "Do you want download newer version?",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                open_download_page()

        else:
            self.statusbar.showMessage("Using Dia's last version.")

    def on_search_clicked(self):
        open_search_page()

    def on_about(self):
        QMessageBox.about(self, "About Diashapes",
                                "Quickly install dia shapes from the repository")


def qt_main():
    app = QApplication(sys.argv)
    w = DiaShapesWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    qt_main()
