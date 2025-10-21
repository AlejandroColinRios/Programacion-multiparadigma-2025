Este es un sistema de gestión de tareas por consola diseñado para aplicar y consolidar los principios de la Programacion Orientada a Objetos (POO) en Python

El proyecto modela tareas y su gestion, implementando herencia, encapsulacion y polimorfismo, ademas de persistencia de datos usando un archivo JSON

Estructura del Proyecto
El sistema esta dividido en dos archivos principales para separar las entidades (clases) de la logica de ejecucion (menu)

tareas.py: Contiene todas las definiciones de clases (Entidades y Gestor)

main.py: Contiene la logica del menu interactivo y la ejecucion principal

Ejecucion del Programa
Para ejecutar el sistema, asegurate de tener Python instalado y ambos archivos (tareas.py y main.py) en el mismo directorio

Pasos
Abre tu terminal o consola

Navega hasta el directorio del proyecto

Ejecuta el archivo principal:

Bash

python main.py
Al iniciar, el programa cargara las tareas desde el archivo tareas.json si existe, o comenzara con una lista vacia

o usa una extension de VISUAL STUDIO CODE para ejecutar el codigo

Diseño Orientado a Objetos (POO)
El diseño se basa en tres clases principales que cumplen con los requisitos academicos

1 Clase Tarea (Clase Base)
Encapsulacion: Implementa atributos privados (usando __atributo) como __titulo y __completada

Acceso Controlado: Utiliza propiedades (@property y @setter) para permitir la lectura y modificacion segura del estado completada

2 Herencia y Polimorfismo (Clases Derivadas)
Las siguientes clases heredan de Tarea

TareaUrgente: Anade el atributo fecha_limite y establece la prioridad en "ALTA"

TareaRecurrente: Anade el atributo recurrencia

Ambas clases derivadas demuestran Polimorfismo al redefinir el metodo mostrar_info() para incluir su informacion especifica (fecha limite o recurrencia)

3 Clase GestorTareas
Abstraccion: Centraliza toda la logica de negocio y gestion de la lista de tareas

Persistencia: Contiene los metodos internos _cargar_tareas() y _guardar_tareas() para manejar la lectura y escritura de objetos serializados en el archivo tareas.json