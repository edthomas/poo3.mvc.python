# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Wed May 16 15:38:50 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(425, 415)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Super Mega Hyper CD Explorer", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setToolTip(_fromUtf8(""))
        MainWindow.setStatusTip(_fromUtf8(""))
        MainWindow.setWhatsThis(_fromUtf8(""))
        MainWindow.setAccessibleName(_fromUtf8(""))
        MainWindow.setAccessibleDescription(_fromUtf8(""))
        MainWindow.setWindowFilePath(_fromUtf8(""))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.albumField = QtGui.QLineEdit(self.centralwidget)
        self.albumField.setGeometry(QtCore.QRect(80, 280, 113, 21))
        self.albumField.setObjectName(_fromUtf8("albumField"))
        self.yearField = QtGui.QLineEdit(self.centralwidget)
        self.yearField.setGeometry(QtCore.QRect(80, 320, 71, 21))
        self.yearField.setObjectName(_fromUtf8("yearField"))
        self.insertButtom = QtGui.QPushButton(self.centralwidget)
        self.insertButtom.setGeometry(QtCore.QRect(170, 340, 80, 25))
        self.insertButtom.setText(QtGui.QApplication.translate("MainWindow", "Insert", None, QtGui.QApplication.UnicodeUTF8))
        self.insertButtom.setObjectName(_fromUtf8("insertButtom"))
        self.artistField = QtGui.QLineEdit(self.centralwidget)
        self.artistField.setGeometry(QtCore.QRect(80, 240, 113, 21))
        self.artistField.setObjectName(_fromUtf8("artistField"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 240, 56, 15))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Artist", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 280, 56, 15))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Album", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 320, 56, 15))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Year", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 411, 221))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.setStyleSheet(_fromUtf8(""))
        self.tableWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.tableWidget.setMidLineWidth(1)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "Cod", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(_fromUtf8("Artist"))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "Album", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "Year", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(260, 240, 20, 141))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.removeButton = QtGui.QPushButton(self.centralwidget)
        self.removeButton.setGeometry(QtCore.QRect(290, 340, 80, 25))
        self.removeButton.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(280, 240, 111, 91))
        self.plainTextEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.plainTextEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.plainTextEdit.setPlainText(QtGui.QApplication.translate("MainWindow", "Select an entry and push the button below to remove it.", None, QtGui.QApplication.UnicodeUTF8))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.insertButtom, QtCore.SIGNAL(_fromUtf8("clicked()")), self.insertButtom.click)
        QtCore.QObject.connect(self.removeButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.removeButton.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item = self.tableWidget.horizontalHeaderItem(2)
        item = self.tableWidget.horizontalHeaderItem(3)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

