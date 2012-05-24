# -*- encoding: utf-8 -*-
from view import View
from model import Cd
from debug import Debugar

class Controller(object): 
    @Debugar 
    def __init__(self):
        self.model = Cd()
        self.view = View(self)

    @Debugar 
    def main(self):
        ''' Executa a tela principal '''
        #print "==> Controller.main()"
        self.view.showMenu()

    @Debugar 
    def callInsert(self):
        ''' Lê os dados, adiciona e mostra se deu certo '''
        #print "==> Callback: callInsert()"
        artist = raw_input("Artista: ")
        album = raw_input("Album: ")
        year = raw_input("Ano: ")
        if ((artist == '') or (album == '') or (year == '')):
            print "Campos invalidos inseridos, saindo."
            return
        else:
            self.model.save(Cd(artist=artist, album=album, year=year))
            print "Novo cd inserido com sucesso!"
                    
    @Debugar        
    def callRemove(self):
        ''' Mostra a lista, lê um código e manda remover. '''
        #print "==> Callback: callListAll()"
        self.callListAll()
        selection = raw_input("Qual entrada tu desejas remover?  ")
        result = self.model.selectOne(selection)
        if (result == 0):
            print "A chave informada não foi encontrada, saindo."
            return
        else:      
            self.model.delete(selection)
            print "Removido com sucesso."

    @Debugar 
    def callListAll(self):
        ''' Imprime a lista de cds e em seguida o menu '''
        # print "==> Callback: callListAll()"
        for cd in self.model.getAll():
            print cd

if __name__ == "__main__":
    print "Execute ./main.py"

