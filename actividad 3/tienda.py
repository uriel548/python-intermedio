from venta import Venta
from producto import Producto
from usuario import Usuario

class Tienda:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.ventas : list[Venta] = []
        self.productos_en_tienda: dict[str, Producto]= {}
        self.usuarios_registrados: dict[str, Usuario] = {}


    def registrar_venta(self, venta: Venta):
            self.ventas.append(venta)

    def registrar_producto(self, producto: Producto):
                self.productos_en_tienda[producto.nombre]= producto

    def mostrar_productos_disponibles(self):
        print(f"\n--- PRODUCTOS DISPONIBLES EN {self.nombre.upper()} ---")
        if not self.productos_en_tienda:
            print("No hay productos registrados.")
            return

        for i, producto in enumerate(self.productos_en_tienda.values()):

            print(f"{i + 1}. {producto.nombre.title()} - ${producto.precio:.2f}")
        print("-" * 40)

    def registrar_usuario(self,usuario: Usuario):
        self.usuarios_registrados[usuario.nombre]=usuario


