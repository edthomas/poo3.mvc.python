'''
Created on 13/05/2012

@author: rafael
'''

class Cd(object):
    
    def __init__(self,cod = None,album='', artist='', year=''):
        self.cod = cod
        self.album = album
        self.artist = artist
        self.year = year
        
    def clean(self): 
        self.cod = None
        self.artist = ''
        self.artist = ''
        self.year = '' 
            

    