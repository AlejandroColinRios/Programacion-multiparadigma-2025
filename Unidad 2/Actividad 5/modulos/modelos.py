"""
modulo modelos que contiene las clases principales del sistema de gestion de biblioteca

Este modulo define las clases Libro, Usuario y Biblioteca
"""


class Libro:
    """
    Clase que representa un libro en la biblioteca

    Atributos:
        titulo (str): El titulo del libro
        autor (str): El autor del libro
        anio (int): El anio de publicacion del libro
        estado (str): "disponible" o "prestado"
    """

    def __init__(self, titulo, autor, anio):
        """
        Inicializa un nuevo libro

        Parametros:
            titulo (str): El titulo del libro
            autor (str): El autor del libro
            anio (int): El anio de publicacion

        Retorna:
            nada
        """
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.estado = "disponible"  # Estado inicial

    def __str__(self):
        """
        Retorna una representacion en cadena del libro

        Parametros:
            ninguno

        Retorna:
            str: libro con su estado
        """
        return f"Libro: {self.titulo} por {self.autor} ({self.anio}) - Estado: {self.estado}"


class Usuario:
    """
    Clase que representa a un usuario de la biblioteca

    Atributos:
        nombre (str): El nombre del usuario
        libros_prestados (list): Lista de objetos de los libros que el usuario tiene prestados
    """

    def __init__(self, nombre):
        """
        Inicializa un nuevo usuario

        Parametros:
            nombre (str): El nombre del usuario

        Retorna:
            nada
        """
        self.nombre = nombre
        self.libros_prestados = []

    def __str__(self):
        """
        Retorna una representacion en cadena del usuario

        Parametros:
            nada

        Retorna:
            str: Representacion del usuario y cuantos libros tiene
        """
        return f"Usuario: {self.nombre}, Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    """
    Clase que gestiona las colecciones de libros y usuarios

    Atributos:
        libros (list): Lista de todos los objetos Libro en la biblioteca
        usuarios (list): Lista de todos los objetos Usuario registrados
    """

    def __init__(self):
        """
        Inicializa la biblioteca con listas vacias

        Parametros:
            ninguno

        Retorna:
            nada
        """
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        """
        Agrega un nuevo libro a la coleccion de la biblioteca

        Parametros:
            libro (Libro): El objeto Libro a agregar

        Retorna:
            nada
        """
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca")

    def agregar_usuario(self, usuario):
        """
        Registra un nuevo usuario en el sistema

        Parametros:
            usuario (Usuario): El objeto Usuario a agregar

        Retorna:
            nada
        """
        self.usuarios.append(usuario)
        print(f"Usuario '{usuario.nombre}' registrado")

    def buscar_libro(self, titulo):
        """
        Busca un libro por titulo

        Parametros:
            titulo (str): El titulo del libro a buscar

        Retorna:
            Libro: El objeto Libro si se encuentra, o nada si no
        """
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def buscar_usuario(self, nombre):
        """
        Busca un usuario por nombre

        Parametros:
            nombre (str): El nombre del usuario a buscar

        Retorna:
            Usuario: El objeto Usuario si se encuentra, o nada si no
        """
        for usuario in self.usuarios:
            if usuario.nombre.lower() == nombre.lower():
                return usuario
        return None

    def prestar_libro(self, titulo_libro, nombre_usuario):
        """
        Gestiona el prestamo de un libro a un usuario

        Parametros:
            titulo_libro (str): El titulo del libro a prestar
            nombre_usuario (str): El nombre del usuario que lo solicita

        Retorna:
            nada
        """
        libro = self.buscar_libro(titulo_libro)
        usuario = self.buscar_usuario(nombre_usuario)

        if not usuario:
            print(f"Error: Usuario '{nombre_usuario}' no encontrado")
            return
        if not libro:
            print(f"Error: Libro '{titulo_libro}' no encontrado")
            return

        if libro.estado == "disponible":
            libro.estado = "prestado"
            usuario.libros_prestados.append(libro)
            print(f"Exito: Libro '{libro.titulo}' prestado a {usuario.nombre}")
        else:
            print(f"Info: Libro '{libro.titulo}' ya esta prestado")

    def devolver_libro(self, titulo_libro, nombre_usuario):
        """
        Gestiona la devolucion de un libro de un usuario

        Parametros:
            titulo_libro (str): El titulo del libro a devolver
            nombre_usuario (str): El nombre del usuario que lo devuelve

        Retorna:
            nada
        """
        libro = self.buscar_libro(titulo_libro)
        usuario = self.buscar_usuario(nombre_usuario)

        if not usuario:
            print(f"Error: Usuario '{nombre_usuario}' no encontrado")
            return
        if not libro:
            print(f"Error: Libro '{titulo_libro}' no encontrado")
            return

        if libro in usuario.libros_prestados:
            libro.estado = "disponible"
            usuario.libros_prestados.remove(libro)
            print(f"Exito: Libro '{libro.titulo}' devuelto por {usuario.nombre}")
        else:
            print(f"Error: {usuario.nombre} no tiene el libro '{libro.titulo}'")

    def mostrar_libros_disponibles(self):
        """
        Imprime en consola todos los libros con estado 'disponible'

        Parametros:
            ninguno

        Retorna:
            nada
        """
        disponibles = [libro for libro in self.libros if libro.estado == "disponible"]
        if not disponibles:
            print("No hay libros disponibles en este momento")
            return

        print("\n--- LIBROS DISPONIBLES ---")
        for libro in disponibles:
            print(f"- {libro.titulo} por {libro.autor} ({libro.anio})")
        print("----------------------------")