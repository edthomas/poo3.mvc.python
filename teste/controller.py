from view import View
from model import Cd

class Controller(object):
 
    def __init__(self):
        self.model = Cd()
        self.view = View()
        

    def callInsert(self, cd):
        self.model.save(cd)
        
    def callRemove(self, cd):
        self.model.delete(cd)

    def callListAll(self):
        self.model.showAll
        
  


