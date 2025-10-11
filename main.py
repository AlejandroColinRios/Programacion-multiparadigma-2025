from producto import Producto
from inventario import Inventario

# Crear un Inventario
inv = Inventario()

# Agregar 3-4 Productos
p1 = Producto("Laptop", 1000.0)
p1.stock = 5
inv.agregar_producto(p1)

p2 = Producto("Mouse", 20.0)
p2.stock = 10
inv.agregar_producto(p2)

p3 = Producto("Teclado", 50.0)
p3.stock = 8
inv.agregar_producto(p3)

p4 = Producto("Monitor", 200.0)
p4.stock = 3
inv.agregar_producto(p4)

# Modificar stock/precios usando setters
p1.stock = 7  # Modificar stock
p2.precio = 25.0  # Modificar precio

# Mostrar total valor
print(f"Total valor inventario: ${inv.total_valor_inventario()}")

# Buscar un producto
buscado = inv.buscar_producto("Mouse")
if buscado:
    print(f"Producto encontrado: {buscado}")
else:
    print("Producto no encontrado")

# Comparar dos productos iguales (mismo nombre)
p5 = Producto("Laptop", 1200.0)  # Mismo nombre
print(f"¿p1 == p5? {p1 == p5}")

# Mostrar todos los productos
print(inv)
