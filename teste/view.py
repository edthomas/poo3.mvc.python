# -*- encoding: utf-8 -*-
from debug import Logar

class View():
    @Logar 
    def __init__(self, controller):
        print "==> View.__init__()"
        self.controller = controller

    @Logar 
    def printHeader(self):
        print "Artist / Album / Year"    

    @Logar 
    def invalidMenuEntry(self):
        print "Invalid Menu Option"

    @Logar 
    def showMenu(self):
        print "==> View.showMenu()"
        menu = {"1": self.controller.callInsert, 
                "2": self.controller.callRemove, 
                "3": self.controller.callListAll}
        while True:
            print "==> View.showMenu(): while True"
            print "\nSuper Mega Hyper CD Explorer 0.003 pre Alpha"
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
            
if __name__ == "__main__":
    print "Execute ./main.py"

