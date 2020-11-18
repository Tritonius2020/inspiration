import pymysql

cnn = connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='cursosql'
        )
print(cnn ,"Se conecto")

        
cur = cnn.cursor()


cur.execute("select CODIGOCLIENTE , EMPRESA from clientes ")
datos = cur.fetchall()
for fila in datos:
    print (fila)




