'''
Proyecyo python mysql
    -Abrir asistente
    -Login o Registro
    -Si elegimos registro, creara un ususario en la base de datos
    -Si elegimos login, identifica al usuario y nos pregunta
    -Crea nota, mostrar notas, borrarlas.
'''
from usuarios import acciones # importo mi modulo 




print('''
Acciones disponibles:
    -registro
    -login
''')
accion=1
hazEL= acciones.Acciones()#creo una variable para que quede logico caundoi llame al objeto guado ahi el objeto 
while accion != "registro" and accion !="login":
    accion=input("Que quieres hacer?: ")

    if accion == "registro":
        hazEL.registro()# me llama toda la logica de este metodo 

    elif accion == "login":# tengo que usar mi paquete de usuario en mi programa principal 
        hazEL.login()

    else:
        print('debe colocar correctamente las instrucciones vuelva a intentarlo porfavor')

# LO LOGICO ES CREAR PAQUETES/MODULOS PARA QUE EL CODIGO NO QUEDE  EL PROGRAMA GIGANTE Y TODO EL CODIGO JUNTO 
# EJ PAQUETE USUSARIOS Y DENTRO D ESTE VARIOS MODULOS POR CONECCIONS OBJETOS ETC

