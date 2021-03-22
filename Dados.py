from SQLite import Sqlite

class Dados(object):
    def __init__(self, idinfo = 0, temperature = "", moisture = "", luminosity = "", date = "", hour = ""):
        self.info = {}
        self.idinfo = idinfo
        self.temperature = temperature
        self.moisture = moisture
        self.luminosity = luminosity
        self.date = date
        self.hour = hour

    def insertDate(self):
        banco = Sqlite()
        try:
            c = banco.conexao.cursor()

            c.execute("""insert into informacoes (temperature, moisture, luminosity, date, hour) values (?, ?, ?, ?, ?) """,
            (self.temperature, self.moisture, self.luminosity, self.date, self.hour))
            banco.conexao.commit()
            c.close()

            return "Dados inseridos com sucesso!"
        except:
            return "Ocorreu um erro na inserção dos dados"


    def deleteDate(self):
        banco = Sqlite()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from informacoes where id = " + self.id + " ")
            banco.conexao.commit()
            c.close()

            return "Dados excluídos com sucesso!"
        except:
            return "Ocorreu um erro na exclusão dos dados"

    def selectDate(self, idinfo):
        banco = Sqlite()
        try:
            c = banco.conexao.cursor()

            data = c.execute("select * from informacoes where idinfo = " + idinfo + " ")

            for linha in c:
                self.temperature = linha[1]
                self.moisture = linha[2]
                self.luminosity = linha[3]
                self.date = linha[4]
                self.hour = linha[5]
            c.close()

            return data

        except:
            return "Ocorreu um erro na busca dos dados"    

    def selectAll(self):
        banco = Sqlite()
        try:

            c = banco.conexao.cursor()

            data = c.execute("select * from informacoes").fetchall()

            for linha in c:
                self.idinfo = linha[0]
                self.temperature = linha[1]
                self.moisture = linha[2]
                self.luminosity = linha[3]
                self.date = linha[4]
                self.hour = linha[5]
            c.close()

            return data
        except:
            return "Dado não encontrado."
