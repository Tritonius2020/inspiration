import pymysql

class DataBase:
    def _init_ (self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='cursosql'
        )

        self.cursor = self.connection.cursor()
print("conexion estable!")
 
def select_all_clientes(self):
            sql = 'SELECT '
            sql = 'SELECT CODIGOCLIENTE , EMPRESA , DIRECCION FROM clientes '
    
try:
            self.cursor.execute(sql)
            clientes = self.cursor.fetchall()
for clientes in clientes:
            print ("CODIGOCLIENTE:", clientes[0])
            print ("EMPRESA:", CLIENTES[1])

    #except Exception as e:
    #raise


database = DataBase()   
database.select_all_clientes()
