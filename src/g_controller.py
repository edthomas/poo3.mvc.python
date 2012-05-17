
import sys
from PyQt4 import QtCore, QtGui
from use_cd import Use_CD
from interface import Ui_Mostrador_de_CDs

class Controller(object):
	
	def __init__(self):
		bd_cd = Use_CD()
		view = Ui_Mostrador_de_CDs()
		app = QtGui.QApplication(sys.argv)
		interface = QtGui.QMainWindow()
	
	def run(self):
		view.setupUi(interface)
		interface.show()
		sys.exit(app.exe())
		

if __name__ == "__main__":
	cont = Controller()
	cont.run
