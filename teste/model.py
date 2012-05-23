import sqlite3
class Cd(object):
    
    def __init__(self,cod = None,artist='', album='' , year='', database = 'database.sqlite'):
        self.cod = cod
        self.artist = artist
        self.album = album
        self.year = year
        self.database = database
        
        
        
    def clean(self): 
        self.cod = None
        self.artist = ''
        self.artist = ''
        self.year = '' 

    def getCd(self):
        return self.__artist, self.__artist, self.__year

    def setCd(self, cod, artist, album, year):
        self._cod = cod
        self._artist = artist
        self._album = album
        self._year = year 
  

    def createDatabase(self):        
        connection = sqlite3.connect('database.sqlite')
        cur = connection.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS cds (cod INTEGER PRIMARY KEY,artist TEXT, album TEXT,year NUMERIC);')
        connection.commit()
        cur.close()
        
    
    def save(self, cd):  
        sql = 'INSERT INTO cds (artist,album,year) VALUES (?, ?, ?)'
        con = sqlite3.connect(self.database)
            
        cur = con.cursor()
        cur.execute(sql, (cd.artist, cd.album, cd.year))
        con.commit()
        con.close()
        
    def delete(self, cd):
        sql = 'DELETE FROM cds WHERE cod = ?'
        con = sqlite3.connect(self.database)

        cur = con.cursor()
        cur.execute(sql, (cd.cod,))
        con.commit()
        con.close()
        
    def showAall(self):
        _all = []
        sql= 'SELECT * FROM cds'
        con = sqlite3.connect(self.database)
        
        cur = con.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        
        for i in result:
            row = list(i)
            _all.append(Cd(row[0], row[1], row[2], row[3]))
             
       
        con.commit()
        con.close()
        return _all
        
        
        