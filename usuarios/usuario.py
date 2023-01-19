# definimos la clase de usuario

import datetime
import hashlib #para cifrar las contracenas 
import usuarios.conexion as conexion
connect=conexion.conectar()
database=connect[0]# en el indice 0 esta la base de datos 
cursor=connect[1]

class Usuario:
    def __init__(self, nombre, apellidos, email,password):# con estos datos vamos a poder guardar un usuario en la base de datos 
        self.nombre= nombre
        self.apellidos= apellidos
        self.email=email
        self.password=password

    def registrar(self):

        cifrado=hashlib.sha256()#cifrar la contracena
        cifrado.update(self.password.encode('utf8'))# le paso un dato para cifrar pero no le paso el valor de una recibe bytes para eso use encode 

        fecha= datetime.datetime.now()
        sql= "insert into usuarios Values(null, %s, %s, %s, %s, %s)"
        usuario= (self.nombre, self.apellidos, self.email,cifrado.hexdigest(), fecha)#la tupla que va ser ingresada en sql por las s
        try:                                             #utilizo el valor hexadecimal del cifrado que me genero la libreria            
            cursor.execute(sql,usuario)
            database.commit()
            result=[cursor.rowcount,self]
        except:# me deja manejar el error 
            result = [0,self]
        return result

    def identificar(self):#comprueva si existe el mail y la contra
        #consulta para comprobar si exite el usuario
        sql="select * from usuarios where email = %s and password= %s"
        #cifrar contracena         
        cifrado=hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        #datos para la consulta 
        usuario=(self.email,cifrado.hexdigest())# aca pasamos los datos que despues le pasamos a la consulta 
        cursor.execute(sql,usuario)# le pasamos la consulta y los datos para la misma 
        result= cursor.fetchone()#queremos solo un ususario
        return result
        #return[cursor.rowcount,self]# me devuelve la cantidad de registros modificados y el objeto con los datos que tenga 
    #def identificar(self):


