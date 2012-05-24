# -*- encoding: utf-8 -*-
import sqlite3
from debug import Debugar

class Cd(object):
    def __init__(self, cod=None, artist='', album='' , year='', database='database.sqlite'):
        self.cod = cod
        self.artist = artist
        self.album = album
        self.year = year
        self.database = database        

    @Debugar  
    def createDatabase(self):        
        connection = sqlite3.connect('database.sqlite')
        cur = connection.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS cds (cod INTEGER PRIMARY KEY,artist TEXT, album TEXT,year TEXT)')
        connection.commit()
        cur.close()        
    
    @Debugar  
    def data(self):
        ''' Retorna uma tupla com os dados do CD '''
        return (self.cod, self.artist, self.album, self.year)

    @Debugar  
    def save(self, cd):  
        sql = 'INSERT INTO cds (artist, album, year) VALUES (?, ?, ?)'
        con = sqlite3.connect(self.database)
            
        cur = con.cursor()
        cur.execute(sql, cd.data()[1:]) # remove "cod" da tupla
        con.commit()
        con.close()
        
    @Debugar  
    def delete(self, cod):
        sql = 'DELETE FROM cds WHERE cod = ?'
        con = sqlite3.connect(self.database)

        cur = con.cursor()
        cur.execute(sql, (cod,))
        con.commit()
        con.close()

    @Debugar
    def selectOne(self, cod):
        sql = 'SELECT COUNT(*) FROM cds WHERE cod = ?'
        con = sqlite3.connect(self.database)
        
        cur = con.cursor() 
        cur.execute(sql, (cod,))        
        data = cur.fetchone()[0]
        con.close()        
        return data        
        
    @Debugar  
    def getAll(self):
        _all = []
        sql = 'SELECT cod, artist, album, year FROM cds'
        con = sqlite3.connect(self.database)

        cur = con.cursor()
        cur.execute(sql)
        result = cur.fetchall()

        for i in result:
            row = list(i)
            cd = Cd(cod=row[0], artist=row[1], album=row[2], year=row[3])
            _all.append(cd)

        con.close()
        return _all

    def __str__(self):
        scod = str(self.cod).ljust(4)
        sart = self.artist.ljust(40)
        salb = self.album.ljust(40)
        syear = str(self.year).ljust(4)
        return scod + sart + salb + syear

if __name__ == "__main__":
    print "Execute ./main.py"

