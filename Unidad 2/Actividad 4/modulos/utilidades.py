"""
modulo utilidades que contiene funciones auxiliares para el programa principal

"""


def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones

    Parametros:
        calificaciones (list): Lista de calificaciones (float).

    Retorna:
        float: El promedio de las calificaciones
    """
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def validar_calificacion(calificacion):
    """
    Valida si una calificacion esta dentro del rango permitido 

    Parametros:
        calificacion (float): La calificacion a validar

    Retorna:
        bool: True si la calificación es valida, False en caso de que no
    """
    return 0 <= calificacion <= 10