# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created: Thu May 17 11:38:07 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Mostrador_de_CDs(object):
    def setupUi(self, Mostrador_de_CDs):
        Mostrador_de_CDs.setObjectName(_fromUtf8("Mostrador_de_CDs"))
        Mostrador_de_CDs.resize(400, 280)
        Mostrador_de_CDs.setWindowTitle(QtGui.QApplication.translate("Mostrador_de_CDs", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(Mostrador_de_CDs)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lista = QtGui.QTableWidget(self.centralwidget)
        self.lista.setGeometry(QtCore.QRect(0, 0, 401, 191))
        self.lista.setObjectName(_fromUtf8("lista"))
        self.lista.setColumnCount(4)
        self.lista.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Mostrador_de_CDs", "Artista", None, QtGui.QApplication.UnicodeUTF8))
        self.lista.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Mostrador_de_CDs", "Álbum", None, QtGui.QApplication.UnicodeUTF8))
        self.lista.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Mostrador_de_CDs", "Ano", None, QtGui.QApplication.UnicodeUTF8))
        self.lista.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Mostrador_de_CDs", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.lista.setHorizontalHeaderItem(3, item)
        self.entradaArtista = QtGui.QLineEdit(self.centralwidget)
        self.entradaArtista.setGeometry(QtCore.QRect(10, 200, 91, 27))
        self.entradaArtista.setObjectName(_fromUtf8("entradaArtista"))
        self.entradaAlbum = QtGui.QLineEdit(self.centralwidget)
        self.entradaAlbum.setGeometry(QtCore.QRect(110, 200, 91, 27))
        self.entradaAlbum.setObjectName(_fromUtf8("entradaAlbum"))
        self.entradaAno = QtGui.QLineEdit(self.centralwidget)
        self.entradaAno.setGeometry(QtCore.QRect(210, 200, 81, 27))
        self.entradaAno.setObjectName(_fromUtf8("entradaAno"))
        self.botaoInsert = QtGui.QPushButton(self.centralwidget)
        self.botaoInsert.setGeometry(QtCore.QRect(10, 230, 281, 27))
        self.botaoInsert.setText(QtGui.QApplication.translate("Mostrador_de_CDs", "Inserir", None, QtGui.QApplication.UnicodeUTF8))
        self.botaoInsert.setObjectName(_fromUtf8("botaoInsert"))
        self.botaoRemove = QtGui.QPushButton(self.centralwidget)
        self.botaoRemove.setGeometry(QtCore.QRect(310, 230, 81, 27))
        self.botaoRemove.setText(QtGui.QApplication.translate("Mostrador_de_CDs", "Remover", None, QtGui.QApplication.UnicodeUTF8))
        self.botaoRemove.setObjectName(_fromUtf8("botaoRemove"))
        self.entradaId = QtGui.QLineEdit(self.centralwidget)
        self.entradaId.setGeometry(QtCore.QRect(310, 200, 81, 27))
        self.entradaId.setObjectName(_fromUtf8("entradaId"))
        Mostrador_de_CDs.setCentralWidget(self.centralwidget)

        self.retranslateUi(Mostrador_de_CDs)
        QtCore.QMetaObject.connectSlotsByName(Mostrador_de_CDs)

    def retranslateUi(self, Mostrador_de_CDs):
        item = self.lista.horizontalHeaderItem(0)
        item = self.lista.horizontalHeaderItem(1)
        item = self.lista.horizontalHeaderItem(2)
        item = self.lista.horizontalHeaderItem(3)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Mostrador_de_CDs = QtGui.QMainWindow()
    ui = Ui_Mostrador_de_CDs()
    ui.setupUi(Mostrador_de_CDs)
    Mostrador_de_CDs.show()
    sys.exit(app.exec_())

