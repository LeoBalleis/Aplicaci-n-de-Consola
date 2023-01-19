import usuarios.conexion as conexion
connect=conexion.conectar()#accedo a ala funcion conectar dentro del modulo coneccion 
database=connect[0]# tengo guardado en el indice 0 de la variable conect database eso esta en conexion
cursor=connect[1]


class Nota:# clase para crear diferente objetos de notas 
    def __init__(self,usuario_id,titulo="",descripcion=""):#datos propiedades que boy a aestar rellenando 
        self.usuario_id=usuario_id
        self.titulo=titulo
        self.descripcion=descripcion

    def guardar(self):
        sql="insert into notas values(null,%s,%s,%s, now())"# funcion now my sql me guarda la fech aahi directamente
        nota=(self.usuario_id,self.titulo,self.descripcion)# va a a tener los datos que se van a a sustituir en la consulta inicial 
        cursor.execute(sql,nota)
        database.commit()
        return[cursor.rowcount,self]# la cantidad de filas afectadas y el objeto

    def listar(self):
        sql=f'select  * from notas where usuario_id = {self.usuario_id}' # saca todas las notas del ususrio que yo le paso
        cursor.execute(sql)# ejecuto mi consulta
        result=cursor.fetchall()# todos los registos en una lista
        return result

    def eliminar(self):
        sql= f"delete from notas where usuario_id = {self.usuario_id} and titulo like '%{self.titulo}%' "
        cursor.execute(sql)
        database.commit()

        return[cursor.rowcount, self]