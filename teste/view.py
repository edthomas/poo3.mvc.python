from controller import *
from model import *
class View():

	def __init__(self):
		pass

	def insert(self):
		artist = raw_input("Artist: ")
		album = raw_input("Album: ")
		year = raw_input("Year: ")
		newCd = (artist,album,year)
		controller.callInsert(newCd)
		print("New cd inserted sucessfully")
		self.showMenu		

	def remove(self):
		self.printHeader
		self.printAll
		selection = raw_input("Which cd do you wanna remove?:  ")
		print selection
		self.showMenu	
		
	def printHeader(self):
		print "Artist / Album / Year"	

	def printAll(self):
		self.printHeader
		print controller.callListAll
		
	def invalidMenuEntry(self):
		print "Invalid Menu Option"

	def showMenu(self):
		menu = {"1": self.insert, "2": self.remove, "3": self.printAll}
		while True:
			print "Super Mega Hyper CD Explorer 0.003 pre Alpha"
			print "--------------------------------------------"
			print "Main Menu"
			print "1 - Insert a CD"
			print "2 - Remove a CD"
			print "3 - Show all CDs"
			print "4 - Leave this thing."
			print "--------------------------------------------"
			opt = raw_input("Choose your option: ")
			if "4" == opt:
				print"Leaving the system"
				return
			parse = menu.get(opt, self.invalidMenuEntry)
			parse()			

	def run(self):
			self.showMenu()			
			
if __name__ == "__main__":
	model = Cd('artist', 'album', 'year')
	model.createDatabase()
	controller = Controller()
	view = View();
	view.run()			
