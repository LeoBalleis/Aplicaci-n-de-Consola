# creamos la clase acciones cuando agrupamos una serie de funciones es mejor agruparlas
# en una clase 

import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    def registro(self):
        print('\nOK!! vamos a registrarte en el sistema...')
        nombre= input("cual es tu nombre?:  ") 
        apellidos= input("Cuales son tus apellidos?:  ")
        email= input("Introduce tu email: ")
        password= input ("Introduce tu contrasena: ") 
        #creo el objeto usuario y al instanciarlo le paso los datos 
        usuario=modelo.Usuario(nombre,apellidos,email,password)#Usuario es la clase que tengo en ese modulo
        registro=usuario.registrar()# no le tengo que pasar nada porq los datos estan el el objeto al instanciarlo
        #comprovacion
        if registro[0]>=1:
            print (f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print ("no te has registrado correctamente ")
    
    def login(self):
        print('\nIdentificate en el sistema.')
        try:
            email= input("Introduce tu email: ")
            password= input ("Introduce tu contrasena: ")
            usuario=modelo.Usuario('','',email,password)# a este objeto solo le pasamos email y pass a la hora de definirlo 
            login=usuario.identificar()
            #comprovamso si el login es correcto 
            if email == login[3]:# el mail esta en la tercera posicion 
                print(f'\nBienvenido{login[1]}, te has registrado en el sistema el {login[5]}')
                self.proximasAcciones(login)
        except Exception as e:
            print(type (e))
            print(type(e).__name__)
            print(f"Login incorrecto!")

    def proximasAcciones(self,usuario): # asistente de proximas acciones
        print('''
        -Crear nota (crear)
        -Mostrar notas (mostrar)
        -Eliminar nota (eliminar)
        -Salir (salir)
        ''') 

        accion=input('Que quieres hacer?: ')
        hazEl=notas.acciones.Acciones()# creo el objeto de acciones importado del paquete notas 
        
        if accion=='crear':
            hazEl.crear(usuario)
            print('vamos a crear')
            self.proximasAcciones(usuario)#llamo denuevo al metodo para que el asistente nunca salga haste que le ponga el exit 
        
        elif accion=='mostrar':
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion=='eliminar':
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion=='salir':
            print(f'ok {usuario[1]} hasta pronto!!! ')
            exit()#corta la ejecucuion del programa


        

            
