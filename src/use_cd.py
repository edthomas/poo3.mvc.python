'''
Created on 13/05/2012

@author: rafael
'''
import sqlite3

from cd import Cd



class Use_CD(object):

    def __init__(self, base ='database.sqlite'):
        self.database = base
            
    def list_cds(self):
        sql = 'SELECT cod, artist, album, year FROM cds'
        con = sqlite3.connect(self.database)

        cursor = con.cursor()
        cursor.execute(sql)
        cds = []

        for r in cursor:
            cds.append(Cd(r[0], r[1], r[2], r[3],))
            
        con.close()
                
        return cds

    def insert(self, cd):
            
        sql = 'INSERT INTO cds (artist,album,year) VALUES (?, ?, ?)'
        con = sqlite3.connect(self.database)
            
        cursor = con.cursor()
        cursor.execute(sql, (cd.artist, cd.album,cd.year))
        con.commit()
        con.close()

    def update(self, cd):
        sql = 'UPDATE cds SET artist = ?, album = ?, year = ?'
        con = sqlite3.connect(self.database)
        cursor = con.cursor()
        cursor.execute(sql, (cd.artist, cd.album,cd.year))
        con.commit()
        con.close()
                
    def delete(self, cd):
        sql = 'DELETE FROM cds WHERE cod = ?'
        con = sqlite3.connect(self.database)

        cursor = con.cursor()
        cursor.execute(sql, (cd.cod,))
        con.commit()
        con.close()

    def exist(self, cd):

        sql = 'SELECT COUNT(cod) FROM cds WHERE cod = ?'
        con = sqlite3.connect(self.database)
        
        cursor = con.cursor()
        cursor.execute(sql, (cd.cod,))
        rs = cursor.fetchone()[0]
        return rs
        con.close()
                  
        
