class Inventario:
    def __init__(self):
        self.__productos = {}  # privado, dict con nombres como keys y objetos Producto como values

    def agregar_producto(self, producto):
        if producto.nombre in self.__productos:
            # Actualiza el stock usando el setter
            self.__productos[producto.nombre].stock = producto.stock
        else:
            self.__productos[producto.nombre] = producto

    def buscar_producto(self, nombre):
        return self.__productos.get(nombre, None)

    def total_valor_inventario(self):
        total = 0
        for p in self.__productos.values():
            total += p.precio * p.stock
        return total

    def __len__(self):
        return len(self.__productos)

    def __str__(self):
        if not self.__productos:
            return "Inventario vacío"
        result = "Productos en inventario:\n"
        for p in self.__productos.values():
            result += str(p) + "\n"
        return result.strip()
