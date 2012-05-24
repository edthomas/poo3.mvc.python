# -*- encoding: utf-8 -*-
import sqlite3
from debug import Logar

class Cd(object):  
    @Logar  
    def __init__(self, cod=None, artist='', album='' , year='', database='database.sqlite'):
        #print "==> Cd.__init__(",cod,",",artist,",",album,",",year,",",database,")"
        self.cod = cod
        self.artist = artist
        self.album = album
        self.year = year
        self.database = database        

    @Logar  
    def createDatabase(self):        
        #print "==> Cd.createDatabase()"
        connection = sqlite3.connect('database.sqlite')
        cur = connection.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS cds (cod INTEGER PRIMARY KEY,artist TEXT, album TEXT,year TEXT)')
        connection.commit()
        cur.close()        
    
    @Logar  
    def data(self):
        ''' Retorna uma tupla com os dados do CD '''
        return (self.cod, self.artist, self.album, self.year)

    @Logar  
    def save(self, cd):  
        #print "==> Cd.save(",cd.__dict__,")"
        sql = 'INSERT INTO cds (artist, album, year) VALUES (?, ?, ?)'
        con = sqlite3.connect(self.database)
            
        cur = con.cursor()
        cur.execute(sql, cd.data()[1:]) # remove "cod" da tupla
        con.commit()
        con.close()
        
    @Logar  
    def delete(self, cod):
        #print "==> Cd.delete(",cod,")"
        sql = 'DELETE FROM cds WHERE cod = ?'
        con = sqlite3.connect(self.database)

        cur = con.cursor()
        cur.execute(sql, (cod,))
        con.commit()
        con.close()

    def selectOne(self, cod):
        #print "==> Cd.select()One"
        sql = 'SELECT COUNT(*) FROM cds WHERE cod = ?'
        con = sqlite3.connect(self.database)
        
        cur = con.cursor()
        for name in ('bar','foo'): 
            result = cur.execute(sql, (cod,))        
            data = cur.fetchone()[0]
        con.close()        
        return data        
        
    @Logar  
    def getAll(self):
        #print "==> Cd.getall()"
        _all = []
        sql = 'SELECT cod, artist, album, year FROM cds'
        con = sqlite3.connect(self.database)

        cur = con.cursor()
        cur.execute(sql)
        result = cur.fetchall()

        for i in result:
            row = list(i)
            cd = Cd(cod=row[0], artist=row[1], album=row[2], year=row[3])
            #print '==> Processando', cd.__dict__
            _all.append(cd)

        con.close()
        return _all

    @Logar  
    def __str__(self):
        return 'Cod: %d\t\tArtista: %s\t\tAlbum: %s\t\tAno: %s' % self.data()

if __name__ == "__main__":
    print "Execute ./main.py"

