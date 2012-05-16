import sqlite3

def createDatabase():

    conexao = sqlite3.connect('database.sqlite')
    c = conexao.cursor()

    c.execute('CREATE TABLE cds (cod INTEGER PRIMARY KEY,artist TEXT, album TEXT,year NUMERIC);')
    conexao.commit()

    print 'Database created!!'
  
    c.close()

createDatabase()

