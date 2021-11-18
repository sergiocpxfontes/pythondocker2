import pyodbc
class Utils:
    @staticmethod
    def ExecutaComandoSQL(sql):
        resultado=0
        cs="""Driver={SQL Server};Server=51.255.44.186,1433;
        Database=academia1;Uid=dt;Pwd=postit"""
        try:
            conn= pyodbc.connect(cs)
            cursor = conn.cursor()
            cursor.execute(sql)
            resultado=cursor.rowcount
            conn.commit()
        except  pyodbc.Error as erro:
            print(erro)
        finally:
            cursor.close()
            conn.close()
        return resultado
    @staticmethod
    def ExecutaConsultaSQL(sql):
        resultado=[]
        cs="""Driver={SQL Server};Server=51.255.44.186,1433;
        Database=academia1;Uid=dt;Pwd=postit"""
        try:
            conn= pyodbc.connect(cs)
            cursor = conn.cursor()
            registos = cursor.execute(sql)
            resultado = registos.fetchall()
            conn.commit()
        except  pyodbc.Error as erro:
            print(erro)
        finally:
            cursor.close()
            conn.close()
        return resultado