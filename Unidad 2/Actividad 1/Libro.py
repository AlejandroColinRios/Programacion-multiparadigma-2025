# libro.py

class Libro:
    """
    Clase que modela un libro en una biblioteca
    """
    
    # Atributo de clase (compartido por todos los objetos)
    biblioteca = "Biblioteca Central"

    def __init__(self, titulo: str, autor: str, anio_publicacion: int):
        """
        Constructor de la clase Libro
        """
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.prestado = False

    def prestar(self):
        """
        Cambia el estado del libro a "prestado"
        """
        if not self.prestado:
            self.prestado = True
            print(f"El libro '{self.titulo}' ha sido prestado")
        else:
            print(f"El libro '{self.titulo}' ya esta prestado")

    def devolver(self):
        """
        Cambia el estado del libro a "no prestado"
        """
        if self.prestado:
            self.prestado = False
            print(f"El libro '{self.titulo}' ha sido devuelto")
        else:
            print(f"El libro '{self.titulo}' no esta prestado")

    def mostrar_estado(self):
        """
        Muestra la informacion del libro y su estado
        """
        estado_prestamo = "Prestado" if self.prestado else "Disponible"
        print("----------------------------------------")
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Anio de Publicacion: {self.anio_publicacion}")
        print(f"Estado: {estado_prestamo}")
        print(f"Biblioteca: {Libro.biblioteca}")
        print("----------------------------------------")