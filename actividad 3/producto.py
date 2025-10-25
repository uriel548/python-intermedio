class Producto:
    contador_productos = 0
    def __init__(self,nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

        Producto.contador_productos += 1

    @staticmethod
    def es_precio_valido(precio: float):
            return precio > 0

    @classmethod
    def total_productos (cls):
        return cls.contador.productos
