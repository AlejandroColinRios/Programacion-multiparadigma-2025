"""
modulo operaciones que contiene funciones auxiliares para la persistencia de datos
del sistema de biblioteca
"""

import json
from modulos.modelos import Biblioteca, Libro, Usuario

ARCHIVO_DATOS = "biblioteca.json"


def guardar_datos(biblioteca):
    """
    Guarda el estado actual de la biblioteca (libros y usuarios) en un archivo JSON

    Parametros:
        biblioteca (Biblioteca): El objeto Biblioteca principal

    Retorna:
        nada
    """
    datos = {
        "libros": [],
        "usuarios": []
    }

    # Convertir objetos Libro a diccionarios
    for libro in biblioteca.libros:
        datos["libros"].append(libro.__dict__)

    # Convertir objetos Usuario a diccionarios
    for usuario in biblioteca.usuarios:
        libros_prestados_titulos = [l.titulo for l in usuario.libros_prestados]
        datos["usuarios"].append({
            "nombre": usuario.nombre,
            "libros_prestados": libros_prestados_titulos
        })

    try:
        with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print(f"Datos guardados exitosamente en {ARCHIVO_DATOS}")
    except IOError as e:
        print(f"Error al guardar datos: {e}")


def cargar_datos():
    """
    Carga el estado de la biblioteca desde un archivo JSON
    Reconstruye los objetos Libro, Usuario y la relacion de prestamos

    Parametros:
        ninguno

    Retorna:
        Biblioteca: Un objeto Biblioteca inicializado con los datos cargados
    """
    try:
        with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as f:
            datos = json.load(f)

        biblioteca = Biblioteca()

        # Cargar libros
        for datos_libro in datos.get("libros", []):
            libro = Libro(datos_libro['titulo'], datos_libro['autor'], datos_libro['anio'])
            libro.estado = datos_libro['estado']
            biblioteca.libros.append(libro)

        # Cargar usuarios y reconstruir prestamos
        for datos_usuario in datos.get("usuarios", []):
            usuario = Usuario(datos_usuario['nombre'])
            
            # Re asignar los objetos libro a la lista de prestados
            for titulo_prestado in datos_usuario.get("libros_prestados", []):
                libro_obj = biblioteca.buscar_libro(titulo_prestado)
                if libro_obj:
                    usuario.libros_prestados.append(libro_obj)
            
            biblioteca.usuarios.append(usuario)

        print(f"Datos cargados exitosamente desde {ARCHIVO_DATOS}")
        return biblioteca

    except FileNotFoundError:
        print(f"Archivo {ARCHIVO_DATOS} no encontrado. Creando nueva biblioteca")
        return Biblioteca()
    except Exception as e:
        print(f"Error al cargar datos: {e}. Creando nueva biblioteca")
        return Biblioteca()