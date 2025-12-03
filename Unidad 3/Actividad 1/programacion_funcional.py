from functools import reduce

# Datos de prueba
ventas_ejemplo = [ 
    {'id': 1, 'monto': 50},
    {'id': 2, 'monto': 150},
    {'id': 3, 'monto': 200},
    {'id': 4, 'monto': 80}, 
    {'id': 5, 'monto': 300},
]
 

def es_venta_mayor_a_100(venta):
    """Funcion Pura: Devuelve True si el monto es mayor a 100"""
    return venta['monto'] > 100

def aplicar_impuesto(venta):
    """
    Funcion Pura: Calcula el monto final con 15% de impuesto
    Retorna un nuevo diccionario sin modificar el original.
    """
    monto_original = venta['monto']
    monto_con_impuesto = monto_original * 1.15
    
    return {
        'id': venta['id'],
        'monto_original': monto_original,
        'monto_final': round(monto_con_impuesto, 2) 
    }

def acumular_total(acumulador, venta_procesada):
    """
    Funcion Pura: Suma el 'monto_final' de la venta procesada al acumulador
    """
    return acumulador + venta_procesada['monto_final']


def procesar_ventas_funcional(ventas):
    """
    Convierte el código imperativo a un pipeline funcional: Filter -> Map -> Reduce
    """
    
    ventas_filtradas = filter(es_venta_mayor_a_100, ventas)
    
    ventas_procesadas = list(map(aplicar_impuesto, ventas_filtradas))
    
    # Inicializa el acumulador en 0.0
    total_final = reduce(acumular_total, ventas_procesadas, 0.0)
    
    # Retorna el resultado idwntico al codigo original
    return ventas_procesadas, round(total_final, 2)




ventas_resultantes, total_calculado = procesar_ventas_funcional(ventas_ejemplo)

print("--- Resultado del Codigo Funcional ---")
print("Ventas Procesadas:")
for venta in ventas_resultantes:
    print(venta)

print(f"\nTotal Calculado: {total_calculado:.2f}")

print("\n--- Verificacion de Inmutabilidad ---")
print(f"Lista original sin modificar: {ventas_ejemplo}")