import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

from main_window import Ui_MainWindow

class Cd():

	def __init__(self, artist, album, year):
		self.artist = artist
		self.album = album
		self.year = year		
		
	
