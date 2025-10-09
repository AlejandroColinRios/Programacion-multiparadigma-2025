# main.py

# Importa la clase Libro desde el archivo libro.py
from Libro import Libro

if __name__ == "__main__":
    print("Iniciando la gestion de libros")

    # Instancia 3 objetos de Libro
    libro1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez", 1967)
    libro2 = Libro("1984", "George Orwell", 1949)
    libro3 = Libro("El principito", "Antoine de Saint-Exupery", 1943)

    # Muestra el estado inicial
    print("--- Estado Inicial de los Libros ---")
    libro1.mostrar_estado()
    libro2.mostrar_estado()
    libro3.mostrar_estado()

    # Llama a metodos
    print("\n--- Simulando Prestamos y Devoluciones ---")
    libro1.prestar()
    libro2.devolver()
    libro3.prestar()

    # Muestra el estado final
    print("\n--- Estado Final de los Libros ---")
    libro1.mostrar_estado()
    libro2.mostrar_estado()
    libro3.mostrar_estado()
    
    print("\nEjecucion completada")