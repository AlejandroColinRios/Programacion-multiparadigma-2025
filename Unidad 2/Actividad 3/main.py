from tareas import GestorTareas, Tarea, TareaUrgente, TareaRecurrente

def mostrar_menu():
    """Muestra las opciones del menu"""
    print("\n--- MENU DE GESTION DE TAREAS ---")
    print("1. Agregar nueva tarea")
    print("2. Listar todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir y Guardar")
    print("----------------------------------")

def obtener_datos_comunes():
    """Solicita los datos basicos de cualquier tarea"""
    titulo = input("  Titulo de la tarea: ")
    descripcion = input("  Descripcion: ")
    return titulo, descripcion

def agregar_tarea_interactivo(gestor):
    """Maneja la logica para agregar diferentes tipos de tareas"""
    print("\n--- TIPOS DE TAREA ---")
    print("a) Tarea Normal (Prioridad Personalizada)")
    print("b) Tarea Urgente (con Fecha Limite)")
    print("c) Tarea Recurrente (con Patron de Repeticion)")
    
    tipo = input("Seleccione el tipo de tarea (a/b/c): ").lower()
    
    if tipo in ('a', 'b', 'c'):
        titulo, descripcion = obtener_datos_comunes()
        nueva_tarea = None

        if tipo == 'a':
            prioridad = input("  Prioridad (Alta/Media/Baja - Media por defecto): ") or "Media"
            nueva_tarea = Tarea(titulo, descripcion, prioridad)
        
        elif tipo == 'b':
            fecha_limite = input("  Fecha limite (ej. 2025-12-31): ")
            nueva_tarea = TareaUrgente(titulo, descripcion, fecha_limite)
        
        elif tipo == 'c':
            recurrencia = input("  Recurrencia (Diaria/Semanal/Mensual - Diaria por defecto): ") or "Diaria"
            nueva_tarea = TareaRecurrente(titulo, descripcion, recurrencia)

        if nueva_tarea:
            gestor.agregar_tarea(nueva_tarea) 
        else:
            print("Tipo de tarea no reconocido")

    else:
        print("Opcion no valida")

def main():
    """Funcion principal del programa"""
    gestor = GestorTareas() 

    while True:
        mostrar_menu()
        opcion = input("Ingrese su opcion: ")

        if opcion == '1':
            agregar_tarea_interactivo(gestor)
        
        elif opcion == '2':
            gestor.listar_tareas()
            
        elif opcion == '3':
            gestor.listar_tareas()
            try:
                indice = int(input("Ingrese el numero de la tarea a marcar como completada: "))
                gestor.marcar_completada(indice)
            except ValueError:
                print("Entrada no valida Debe ser un numero")
                
        elif opcion == '4':
            gestor.listar_tareas()
            try:
                indice = int(input("Ingrese el numero de la tarea a eliminar: "))
                gestor.eliminar_tarea(indice)
            except ValueError:
                print("Entrada no valida Debe ser un numero")
                
        elif opcion == '5':
            print("\nSaliendo del Sistema de Gestion de Tareas Los datos han sido guardados")
            break
            
        else:
            print("Opcion no valida Por favor, intente de nuevo")

if __name__ == "__main__":
    main()