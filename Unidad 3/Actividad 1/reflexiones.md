# Analisis de las funciones puras e impuras

## Parte 1: Identificacion y analisis

### 1. Funcion A: `calcular_promedio(numeros)`

| Caracteristica | Analisis |
| :--- | :--- |
| **Pura o impura?** | **Pura** |
| **por que?** | El resultado depende solo del argumento de entrada,no tiene efectos secundarios externos |
| **Como convcertirla a pura** | ya es pura |

---

### 2. Funcion B: `siguiente_id()`

| Caracteristica | Analisis |
| :--- | :--- |
| **Pura o impura?** | **Impura** |
| ***por que?** | Modifica una variable global utilizando la declaración `global`, lo que provoca un efecto secundario y Su resultado no es determinista, ya que depende del estado global |
| **Como convertirla a pura** | Se debe recibir el estado actual como argumento y devolver el nuevo estado y el ID |
| **Conversion** | ```python def generar_id_puro(contador_actual): return contador_actual + 1, f"ID-{contador_actual + 1}" ``` |

---

### 3. Función C: `agregar_fecha(registro)`

| Caracteristica | Analisis |
| :--- | :--- |
| **Pura o impura?** | **Impura** |
| **por que?** | Modifica el argumento de entrada al asignarle una nueva clave y porque Depende de una fuente externa |
| **Como convertirla a pura** | devolviendo un nuevo diccionario que incluya la fecha|
| **Conversion** | ```python def agregar_fecha_puro(registro, timestamp): return {**registro, 'fecha': timestamp} ``` |

---

### 4. Funcion D: `filtrar_positivos(numeros)`

| Caracteristica | Analisis |
| :--- | :--- |
| **Pura o impura?** | **Pura** |
| **por que?** | El resultado depende solo de la entrada |
| **Como convertirla a pura** | ya es pura |

---

### 5. Funcion E: `mezclar_lista(lista)`

| Caracteristica | Analisis |
| :--- | :--- |
| **Pura o impura?** | **Impura** |
| **por que?** | usa `random.shuffle(lista)`, que es una operación *in-place* que modifica el argumento de entrada y El orden es aleatorio en cada llamada  |
| **Como convertirla a pua** | La funcion debe trabajar sobre una **copia** de la lista de entrada para evitar la mutación osea que se modifique el argumento de entrada |
| **Conversion** | ```python import random def mezclar_lista_puro(lista): lista_copia = lista[:] random.shuffle(lista_copia) return lista_copia ```