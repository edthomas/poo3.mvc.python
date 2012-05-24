# -*- encoding: utf-8 -*-
from debug import Logar

class View():
    @Logar 
    def __init__(self, controller):
        #print "==> View.__init__()"
        self.controller = controller

    @Logar 
    def printHeader(self):
        print "Artista / Album / Ano"    

    @Logar 
    def invalidMenuEntry(self):
        print "Opção inválida!"

    @Logar 
    def showMenu(self):
        #print "==> View.showMenu()"
        menu = {"1": self.controller.callInsert, 
                "2": self.controller.callRemove, 
                "3": self.controller.callListAll}
        while True:
        #    print "==> View.showMenu(): while True"
            print "\nSuper Mega Hyper CD Explorer 0.004 pre Alpha - (Text Mode)"
            print "--------------------------------------------"
            print "Menu Principal"
            print "1 - Inserir um CD"
            print "2 - Remover um CD"
            print "3 - Mostrar todos os CDs"
            print "4 - Abandonar o navio."
            print "--------------------------------------------"
            opt = raw_input("Digite vossa escolha aqui: ")
            if "4" == opt:
                print"Deixando o sistema..."
                return
            parse = menu.get(opt, self.invalidMenuEntry)
            parse()            
            
if __name__ == "__main__":
    print "Execute ./main.py"

