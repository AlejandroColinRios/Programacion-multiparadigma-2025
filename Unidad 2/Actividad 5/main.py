"""
modulo principal que controla el flujo del programa de gestion de biblioteca

Este modulo proporciona una interfaz de menu en consola para interactuar
con el sistema, permitiendo agregar libros, usuarios, prestar y devolver
"""

from modulos.modelos import Biblioteca, Libro, Usuario
from modulos.operaciones import guardar_datos, cargar_datos


def mostrar_menu():
    """
    Muestra las opciones disponibles en el menu principal

    No recibe parametros

    No retorna valores
    """
    print("\n--- SISTEMA DE GESTION DE BIBLIOTECA ---")
    print("1. Agregar nuevo libro")
    print("2. Registrar nuevo usuario")
    print("3. Prestar un libro")
    print("4. Devolver un libro")
    print("5. Mostrar libros disponibles")
    print("6. Salir y guardar")
    print("------------------------------------------")


def main():
    """
    Funcion principal del programa

    Controla el bucle principal del menu y maneja las opciones del usuario
    Carga los datos al iniciar y los guarda al salir

    No recibe parametros

    No retorna valores
    """
    # Carga los datos guardados al iniciar
    biblioteca = cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            # Agregar libro
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese el autor del libro: ")
            try:
                año = int(input("Ingrese el año de publicacion: "))
                libro = Libro(titulo, autor, año)
                biblioteca.agregar_libro(libro)
            except ValueError:
                print("Error: El año debe ser un numero entero")

        elif opcion == '2':
            # Registrar usuario
            nombre = input("Ingrese el nombre del usuario: ")
            usuario = Usuario(nombre)
            biblioteca.agregar_usuario(usuario)

        elif opcion == '3':
            # Prestar libro
            if not biblioteca.libros or not biblioteca.usuarios:
                print("Debe haber libros y usuarios registrados para prestar")
                continue
            titulo_libro = input("Ingrese el titulo del libro a prestar: ")
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            biblioteca.prestar_libro(titulo_libro, nombre_usuario)

        elif opcion == '4':
            # Devolver libro
            if not biblioteca.libros or not biblioteca.usuarios:
                print("Debe haberr libros y usuarios registrados para  poder devolver")
                continue
            titulo_libro = input("Ingrese el titulo del libro a devolver: ")
            nombre_usuario = input("Ingrese el nombre del usuario: ")
            biblioteca.devolver_libro(titulo_libro, nombre_usuario)

        elif opcion == '5':
            # Mostrar libros disponibles
            biblioteca.mostrar_libros_disponibles()

        elif opcion == '6':
            # Salir y guardar1

            guardar_datos(biblioteca)
            print("Saliendo del programa")
            break

        else:
            print("esa opcion no existe jeje")


if __name__ == "__main__":
    main()