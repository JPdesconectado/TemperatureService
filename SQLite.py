import sqlite3

class Sqlite():

    def __init__(self):
        self.conexao = sqlite3.connect('sensorinfo.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists informacoes (
                    idinfo integer primary key autoincrement,
                    temperature text,
                    moisture text,
                    luminosity text,
                    date text,
                    hour text)""")
        self.conexao.commit()
        c.close()