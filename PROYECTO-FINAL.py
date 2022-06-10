#           ----AGENDA TELEFONICA EJECUTABLE EN CONSOLA----

import os


# No modificar
CARPETA = 'Agenda/'
EXTENSION = '.txt' 

class Contacto:
    def __init__(self,nombre,telefono,categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria




def app():
    crear_directorio()
    
    mostrar_menu()
    
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opcion: \r\n')
        opcion = int(opcion)

        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contacto()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False    
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no valida, intente de nuevo')


def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea buscar \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\n Contacto eliminado con exito \r\n')
    except:
        print('No existe ese contacto')
    
    app()


def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion de contacto \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)

    app()

def mostrar_contacto():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    app()

def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar \r\n')

    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            nombre_contacto = input('Agrega un nuevo nombre: \r\n')
            telefono_contacto = input('Agrega un nuevo telefono \r\n')
            categoria_contacto = input('Agrega una nueva categoria \r\n')

            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Numero: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
        print('Contacto editado con exito')
    else:
        print('Ese contacto no existe')
    
    app()
    
def agregar_contacto():
    print('Escribe los datos para agregar el nuevo Contacto')
    nombre_contacto = input('Nombre del contacto \r\n')
    existe = existe_contacto(nombre_contacto)

    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            telefono_contacto = input('Telefono del contacto \r\n')
            categoria_contacto = input('Categoria del contacto \r\n')

            contacto = Contacto(nombre_contacto,telefono_contacto,categoria_contacto)

            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Numero: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            print('\r\n Contacto creado exitosamente \r\n')         
    else:
        print('Ese contacto ya existe')

    app()    

def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)

   
def mostrar_menu():
    print('Seleccione del menu lo que desea hacer:')
    print('1- Agregar nuevo contacto')
    print('2- Editar un contacto')
    print('3- Ver contacto')
    print('4- Buscar contacto')
    print('5- Eliminar contacto')
  
def existe_contacto(nombre):
    return  os.path.isfile(CARPETA + nombre + EXTENSION)


app()