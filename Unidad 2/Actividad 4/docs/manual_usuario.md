# Manual de Usuario

## Proposito del Programa

El porgama para la gestion de Calificaciones es un programa desarrollado en Python que permite gestionar estudiantes y sus calificaciones, Ofrece una interfaz de menu en cosola interactiva para agregar estudiantes, asignar calificaciones, calcular promedios y listar información de los estudiantes registrados

## Como Ejecutar el Proyecto

Para ejecutar el proyecto, abre una terminal entra a la carpeta del proyecto y ejectua: 

```
python main.py
```

Esto iniciara la interfaz de menu interactivo del programa 

## Modulos del Proyecto

El proyecto esta estructurado en los siguientes modulos:

- **main.py**: Modulo principal que controla el flujo del programa, Proporciona la interfaz de menú para interactuar con el sistema, permitiendo agregar estudiantes, asignar calificaciones, calcular promedios y listar estudiantes

- **modulos/modelo.py**: Contiene la clase `Estudiante`, que representa a un estudiante con sus atributos (nombre y lista de calificaciones) Incluye metodos para agregar calificaciones y representar al estudiante como cadena

- **modulos/utilidades.py**: Incluye funciones auxiliares como `calcular_promedio` para calcular el promedio de una lista de calificaciones y `validar_calificacion` para verificar que una calificacion estée entre 0 y 10.
