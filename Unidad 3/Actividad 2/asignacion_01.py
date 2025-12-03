# 1. Crear Transformador 
def crear_transformador(funcion):
    """
    Recibe una funcion y retorna otra funcion que 
    aplica esa transformacion a cada elemento de una lista
    """
    def transformador_de_lista(lista):
        # Implementacin funcional usando list comprehension, crea una nueva lista
        return [funcion(elemento) for elemento in lista]
    return transformador_de_lista

# 2. Crear Filtro
def crear_filtro(predicado):
    """
    Recibe un predicado y retorna otra funcion 
    que filtra una lista dejando solo los elementos que cumplen el predicado
    """
    def filtro_de_lista(lista):
        return [elemento for elemento in lista if predicado(elemento)]
    return filtro_de_lista

# 3. Crear Reductor
def crear_reductor(funcion_reduccion, valor_inicial):
    """
    Recibe una funcion de reduccion y un valor inicial, retorna una funcion 
    que reduce una lista a un solo valor 
    """
    def reductor_de_lista(lista):
        acumulador = valor_inicial
        for elemento in lista:
            acumulador = funcion_reduccion(acumulador, elemento)
        return acumulador
    return reductor_de_lista

# 4. Componer
def componer(*funciones):
    """
    Recibe multiples funciones y retorna una nueva funcion que las aplica 
    en secuencia
    """
    def pipeline(argumento):
        resultado = argumento
        # Aplica cada función al resultado de la función anterior
        for funcion in funciones:
            resultado = funcion(resultado)
        return resultado
    return pipeline

