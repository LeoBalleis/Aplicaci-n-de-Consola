import notas.nota as modelo

class Acciones:
    def crear(self,usuario):
        print(f'ok{usuario[1]}!!! Vamos a crear una nueva nota... ')
        titulo=input('Introduce el titulo de tu nota: ')
        descripcion=input('Mete el contenido de tu nota: ')

        nota=modelo.Nota(usuario[0],titulo,descripcion)
        guardar= nota.guardar()
        
        if guardar[0]>=1:
            print(f'\nPerfecto has guardado la nota:{nota.titulo}')
        else:
            print(f'\nNo se ha guardado la nota, lo siento {usuario[1]} ')
    
    def mostrar(self, usuario):
        print(f'\nAqui tienes tus notas {usuario[1]} ')
        nota=modelo.Nota(usuario[0],"","")# ojo aca 
        notas=nota.listar()# este me saca todos los datos de la base de datso
        print(notas)# esto es una lista

        for nota in notas:
            print('\n******************************************')
            print(nota[2])
            print(nota[3])

    def borrar (self,usuario):
        print(f"\n ok {usuario[1]}!!! vamos a borrar notas")
        titulo=input("introduce el titulo de la nota a borrar: ")
        nota=modelo.Nota(usuario[0], titulo)
        eliminar=nota.eliminar()
    
        if eliminar[0]>= 1:
            print(f"hemos borrado la nota: {nota.titulo}")
        else:
            print('no se ha borrado la nota')

    



