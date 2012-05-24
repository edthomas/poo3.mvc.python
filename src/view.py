# -*- encoding: utf-8 -*-
from debug import Debugar

class View():
    @Debugar 
    def __init__(self, controller):
        self.controller = controller
                
    @Debugar 
    def invalidMenuEntry(self):
        print "Opção inválida!"

    @Debugar
    def lerOpcao(self):
        menu = {"1": self.controller.callInsert, 
                "2": self.controller.callRemove, 
                "3": self.controller.callListAll}
        print "\nSuper Mega Hyper CD Explorer 0.004 pre Alpha - (Text Mode)"
        print "Menu Principal".center(44, '-')
        print " 1 - Inserir um CD"
        print " 2 - Remover um CD"
        print " 3 - Mostrar todos os CDs"
        print " 4 - Abandonar o navio."
        print "-" * 44
        opt = raw_input("Digite vossa escolha aqui: ")
        if "4" == opt:
            print"Deixando o sistema..."
            exit(0)
        parse = menu.get(opt, self.invalidMenuEntry)
        parse()  

    @Debugar
    def showMenu(self):
        while True:
            self.lerOpcao()
            
if __name__ == "__main__":
    print "Execute ./main.py"

