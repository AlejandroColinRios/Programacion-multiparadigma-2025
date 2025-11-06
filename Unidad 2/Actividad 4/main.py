"""
modulo principal que controla el flujo del programa de gestion de calificaciones de estudiantes

Este modulo proporciona una interfaz de menu en consola para interactuar con el sistema de estudiantes,
permitiendo agregar estudiantes, asignar calificaciones y calcular los promedios
"""

from modulos.modelo import Estudiante
from modulos.utilidades import calcular_promedio, validar_calificacion


def mostrar_menu():
    """
    Muestra las opciones disponibles en el menu principal

    No recibe parametros

    No retorna valores algunos
    """
    print("\n--- MENU DE GESTION DE CALIFICACIONES ---")
    print("1. Agregar estudiante")
    print("2. Agregar calificacion a estudiante")
    print("3. Mostrar promedio de estudiante")
    print("4. Listar estudiantes")
    print("5. Salir")
    print("------------------------------------------")


def main():
    """
    FunciOn principal del programa.

    Controla el bucle principal del menu y maneja las opciones del usuario

    No recibe parametros

    No retorna valores algunos tampoco
    """
    estudiantes = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del estudiante: ")
            estudiante = Estudiante(nombre)
            estudiantes.append(estudiante)
            print(f"Estudiante '{nombre}' agregado.")

        elif opcion == '2':
            if not estudiantes:
                print("No hay estudiantes registrados")
                continue
            print("Estudiantes disponibles:")
            for i, est in enumerate(estudiantes, 1):
                print(f"{i}. {est.nombre}")
            try:
                idx = int(input("Seleccione el numero del estudiante: ")) - 1
                if 0 <= idx < len(estudiantes):
                    calif = float(input("Ingrese la calificacion (0-10): "))
                    if validar_calificacion(calif):
                        estudiantes[idx].agregar_calificacion(calif)
                        print("Calificacion agregada")
                    else:
                        print("Calificaciion invalida")
                else:
                    print("Numero invalido")
            except ValueError:
                print("Entrada invalida")

        elif opcion == '3':
            if not estudiantes:
                print("No hay estudiantes registrados")
                continue
            print("Estudiantes disponibles:")
            for i, est in enumerate(estudiantes, 1):
                print(f"{i}. {est.nombre}")
            try:
                idx = int(input("Seleccione el numero del estudiante: ")) - 1
                if 0 <= idx < len(estudiantes):
                    promedio = calcular_promedio(estudiantes[idx].calificaciones)
                    print(f"Promedio de {estudiantes[idx].nombre}: {promedio:.2f}")
                else:
                    print("Numero invalido.")
            except ValueError:
                print("Entrada invalida.")

        elif opcion == '4':
            if not estudiantes:
                print("No hay estudiantes registrados")
            else:
                print("Lista de estudiantes:")
                for est in estudiantes:
                    promedio = calcular_promedio(est.calificaciones)
                    print(f"- {est.nombre}: {len(est.calificaciones)} calificaciones, Promedio: {promedio:.2f}")

        elif opcion == '5':
            print("Saliendo del programa")
            break

        else:
            print("Opcion no encontrada")


if __name__ == "__main__":
    main()
