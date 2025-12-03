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


    # Datos de prueba
    numeros = [1, -2, 3, -4, 5, -6, 7, 8, -9, 10]

    print("--- Ejecucion del Pipeline Configurable ---")
    print(f"Datos de entrada: {numeros}")

    # Pipeline: filtrar positivos -> elevar al cuadrado -> sumar todo
    pipeline = componer( 
        # 1. FILTRAR: Solo positivos
        crear_filtro(lambda x: x > 0), 
        
        # 2. MAPEAR/TRANSFORMAR: Elevar al cuadrado
        crear_transformador(lambda x: x ** 2), 
        
        # 3. REDUCIR: Sumar todos los elementos, comenzando en 0
        crear_reductor(lambda acc, x: acc + x, 0)
    )

    resultado = pipeline(numeros)

    # Verificación de la operacion:
    # 1. Positivos: [1, 3, 5, 7, 8, 10]
    # 2. Al cuadrado: [1, 9, 25, 49, 64, 100]
    # 3. Suma: 1 + 9 + 25 + 49 + 64 + 100 = 248

    print(f"Resultado: {resultado}")

    # Se confirma que el resultado es 248

