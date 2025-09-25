import os

def mostrar_menu():
    print("\n--- Gestor de Tareas Personales ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def agregar_tarea(tareas):
    descripcion = input("Ingresa la nueva tarea: ")
    if descripcion:
        # Se usa un ID basado en la longitud actual para simplicidad
        id_tarea = len(tareas) + 1
        tareas[id_tarea] = {"descripcion": descripcion, "completada": False}
        print(f"Tarea '{descripcion}' agregada con éxito.")
    else:
        print("La descripcion de la tarea no puede estar vacia.")

def listar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes")
        return

    print("\n--- Tareas Actuales ---")
    for id_tarea, tarea in tareas.items():
        estado = "Terminada" if tarea["Coompletada"] else "Pendiente"
        print(f"{id_tarea}. [{estado}] {tarea['descripcion']}")

def marcar_como_completada(tareas):
    listar_tareas(tareas)
    if not tareas:
        return
    
    try:
        id_a_completar = int(input("Ingresa el numero de la tarea a completar: "))
        if id_a_completar in tareas:
            tareas[id_a_completar]["completada"] = True
            print(f"Tarea '{tareas[id_a_completar]['descripcion']}' marcada como completada")
        else:
            print("Numero de tarea no válido")
    except ValueError:
        print("Entrada no valida, Por favor, ingresa un numero")

def eliminar_tarea(tareas):
    listar_tareas(tareas)
    if not tareas:
        return
        
    try:
        id_a_eliminar = int(input("Ingresa el numero de la tarea a eliminar: "))
        if id_a_eliminar in tareas:
            descripcion = tareas.pop(id_a_eliminar)["descripcion"]
            # Reorganiza los IDs después de eliminar para mantener la numeración secuencial
            nuevas_tareas = {}
            for i, (id_tarea, tarea) in enumerate(tareas.items()):
                nuevas_tareas[i + 1] = tarea
            tareas.clear()
            tareas.update(nuevas_tareas)

            print(f"Tarea '{descripcion}' eliminada con exito")
        else:
            print("Número de tarea no válido.")
    except ValueError:
        print("Entrada no valida, Por favor, ingresa un numero")

def main():
    tareas = {}
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_tarea(tareas)
        elif opcion == '2':
            listar_tareas(tareas)
        elif opcion == '3':
            marcar_como_completada(tareas)
        elif opcion == '4':
            eliminar_tarea(tareas)
        elif opcion == '5':
            print("Saliendo del programa")
            break
        else:
            print("Opcionn no valida, Por favor, elige una opcion del 1 al 5")

if __name__ == "__main__":
    main()