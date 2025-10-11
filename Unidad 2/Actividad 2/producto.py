class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre  # público
        self._precio = precio  # protegido
        self.__stock = 0  # privado
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("El stock no puede ser negativo")
        self.__stock = value

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        if value <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        self._precio = value

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}"

    def __eq__(self, other):
        if isinstance(other, Producto):
            return self.nombre == other.nombre
        return False
