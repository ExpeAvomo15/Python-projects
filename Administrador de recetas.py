'''
Program through which a user can read, create and delete recipes found
in a database.
'''

from pathlib import Path
import os
from os import listdir, system

ruta = Path(Path.home(), 'C:/Users/soyex/PycharmProjects/pythonProject/Día 6/Día 6/Recetas')
print(f'La ruta es: {ruta}')
#print()
print('Menu: \n 1. Leer receta \n 2. Crear receta \n 3. Crear categoría \n 4. Eliminar receta \n 5. Eliminar categoria \n 6. Finalizar ')
print()

opcion = int(input('Elige una opción del Menú: '))

while opcion!=6:


    def listar_recetas():
        cont = 0
        for txt in Path(ruta).glob('**/*.txt'):
            #print(txt)
            cont += 1
            #print()
        return f'Hay un total de {cont} recetas'

    print(listar_recetas())

    def mostrar_categorias():
        return listdir(ruta)


    def elegir_categoria ():
        print(f'Categorias disponibles: {mostrar_categorias()}')
        print()
        carpeta = input ('Elige una categoria: ')
        categoria = Path(ruta, carpeta)
        return categoria

    def mostrar_recetas(ruta):
       print(listdir(ruta))

    def leer_receta():
        categoria = elegir_categoria()
        mostrar = mostrar_recetas(categoria)
        receta = input ('Elige una receta: ')
        ruta_receta = Path(categoria, receta)
        isFile = os.path.isfile(ruta_receta)
        if isFile :
            print(ruta_receta.read_text())

    def crear_receta():
        categoria = elegir_categoria()
        nombre_receta = input('Nombre de la receta terminado en .txt: ')
        ruta_receta = Path(categoria, nombre_receta)
        nueva_receta = ruta_receta.write_text('Esta es la nueva receta')
        mostrar_lista_recetas = mostrar_recetas(categoria)
        return ruta_receta

    def crear_categoria():
        nombre_categoria = input('Introduce el nombre de la nueva categoria: ')
        nueva_ruta = Path(ruta, nombre_categoria)
        nueva_categoria = os.makedirs(nueva_ruta)
        return nueva_categoria


    def eliminar_receta():
        categoria = elegir_categoria()
        mostrar = mostrar_recetas(categoria)
        receta_a_eliminar = input ('Receta que quieres eliminar: ')
        ruta_receta_delete = Path(categoria, receta_a_eliminar)
        os.remove(ruta_receta_delete)

    def eliminar_categoria():
        categoria=elegir_categoria()
        categoria.rmdir()

    match opcion:
        case 1:
            print(leer_receta())
        case 2:
           print(crear_receta())
        case 3:
            print(crear_categoria())
        case 4:
            print(eliminar_receta())
        case 5:
            delete = eliminar_categoria()
            print(delete)
        case 6:
            system('cls')
    print()

    opcion = int(input('Elige una opción del Menú: '))














