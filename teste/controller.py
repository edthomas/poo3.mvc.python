# -*- encoding: utf-8 -*-
from view import View
from model import Cd
from debug import Logar

class Controller(object): 
    @Logar 
    def __init__(self):
        self.model = Cd()
        self.view = View(self)

    @Logar 
    def main(self):
        ''' Executa a tela principal '''
        print "==> Controller.main()"
        self.view.showMenu()

    @Logar 
    def callInsert(self):
        ''' Lê os dados, adiciona e mostra se deu certo '''
        print "==> Callback: callInsert()"
        artist = raw_input("Artist: ")
        album = raw_input("Album: ")
        year = raw_input("Year: ")
        self.model.save(Cd(artist=artist, album=album, year=year))
        print "New cd inserted sucessfully"

    @Logar         
    def callRemove(self):
        ''' Mostra a lista, lê um código e manda remover. '''
        print "==> Callback: callListAll()"
        self.callListAll()
        selection = raw_input("Which one do you wanna remove?:  ")
        self.model.delete(selection)
        print "Done."

    @Logar 
    def callListAll(self):
        ''' Imprime a lista de cds e em seguida o menu '''
        print "==> Callback: callListAll()"
        for cd in self.model.getAll():
            print cd

if __name__ == "__main__":
    print "Execute ./main.py"

