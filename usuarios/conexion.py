
import mysql.connector

def conectar():
    database=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="passworld", 
        database="master_python",
        port= 3306 
    )
    # el puerto lo saque de php my admin 
    cursor=database.cursor(buffered=True)

    return[database,cursor]