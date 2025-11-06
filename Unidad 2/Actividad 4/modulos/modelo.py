"""
modulo modelo que contiene las clases principales del programa
"""


class Estudiante:
    """
    Clase que representa a un estudiante en el sistema de gestión de calificaciones

    Atributos:
        nombre (str): El nombre del estudiante
        calificaciones (list): Lista de calificaciones del estudiante
    """

    def __init__(self, nombre):
        """
        Inicializa un nuevo estudiante

        Parametros:
            nombre (str): El nombre del estudiante

        Retorna:
            nada
        """
        self.nombre = nombre
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        """
        Agrega una calificacion a la lista del estudiante

        Parametros:
            calificacion (float): La calificacion a agregar debe estar en el rango de 0 a 10

        Retorna:
            nada
        """
        self.calificaciones.append(calificacion)

    def __str__(self):
        """
        Retorna una representación en cadena del estudiante

        Parametros:
            ninguno

        Retorna:
            str: estudiante con nombre y numero de calificacion
        """
        return f"Estudiante: {self.nombre}, Calificaciones: {len(self.calificaciones)}"
