from cliente import Cliente
from producto import Producto
from usuario import EstrategiaDescuento, DescuentoNinguno
class Venta:
    def __init__(self,cliente: Cliente):
        self.cliente =cliente
        self.productos: list[Producto] = []

    def agregar_producto(self,producto: Producto):
            self.productos.append(producto)

    # modificacion del total para agregar descuentos
    def total(self, estrategia: EstrategiaDescuento = None) -> float:
        total_base = sum(p.precio for p in self.productos)

        #  Si no se pasa una estrategia, usa el valor por defecto
        if estrategia is None:
            estrategia = DescuentoNinguno()

        # 2. Usa la estrategia elegida (ya sea Lealtad o Ninguno)
        return estrategia.aplicar_descuento(total_base)

    def mostrar_articulos_vendidos(self):
        print(f"Artículos comprados por {self.cliente.nombre}:")

        if not self.productos:
            print("  (Ningún producto registrado en esta venta.)")
            return

        for producto in self.productos:
            # Asumiendo que tu clase Producto tiene atributos 'nombre' y 'precio'
            print(f"  - {producto.nombre.title()} (${producto.precio:.2f})")