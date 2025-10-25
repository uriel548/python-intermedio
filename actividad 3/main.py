from cliente import Cliente
from administrador import Administrador
from producto import Producto
from venta import Venta
from tienda import Tienda
from usuario import Usuario, DescuentoLealtad

def funcion_principal():
    tienda = Tienda("tecSTORE")

    cliente1 = Cliente("Hector", "hector23@gmail.com", 900)
    cliente2 = Cliente("Ana", "an12@outlook.com", 3000)
    cliente3 = Cliente("Pedro", "pedro57@yahoo.com", 6000)

    admin1 = Administrador("Uriel", "fernandezurieluriel@outlook.com",
                           ["Gestion de inventario", "reportes"])


    tienda.registrar_usuario(cliente1)
    tienda.registrar_usuario(cliente2)
    tienda.registrar_usuario(cliente3)
    tienda.registrar_usuario(admin1)
    print("-----REGISTRO INICIAL-----")
    print(f"Usuarios registrados en tienda :{len(tienda.usuarios_registrados)}")

    p1 = Producto("teclado", 200, )
    p2 = Producto("mouse", 80)
    p3 = Producto("cable usb tipo c", 50)
    p4 = Producto("cargador", 300)
    p5 = Producto("laptop", 8000)
    p6 = Producto("memoria usb", 250)
    p7 = Producto("impresora", 3000)


    tienda.registrar_producto(p1)
    tienda.registrar_producto(p2)
    tienda.registrar_producto(p3)
    tienda.registrar_producto(p4)
    tienda.registrar_producto(p5)
    tienda.registrar_producto(p6)
    tienda.registrar_producto(p7)
    print(f"Productos disponibles en tienda: {len(tienda.productos_en_tienda)}")
    print("_" * 30)

    venta1 = Venta(cliente1)
    venta1.agregar_producto(p1)
    venta1.agregar_producto(p6)

    venta2 = Venta(cliente2)
    venta2.agregar_producto(p7)

    venta3 = Venta(cliente3)
    venta3.agregar_producto(p7)
    venta3.agregar_producto(p7)

    tienda.registrar_venta(venta1)
    tienda.registrar_venta(venta2)
    tienda.registrar_venta(venta3)

    tienda.mostrar_productos_disponibles()
    print("----------tecStore----------")
    print(admin1.mostrar_info())
    print("\n---RESULTADO DE LA VENTA---")
    print(cliente1.mostrar_info())
    venta1.mostrar_articulos_vendidos()
    print(f"Total de la venta: ${venta1.total():.2f}")
    print("-" * 30)
#cliente 2
    print(cliente2.mostrar_info())
    venta2.mostrar_articulos_vendidos()
    print(f"Total de la venta: ${venta2.total():.2f}")
    print("_"*30)
#cliente3
    print(cliente3.mostrar_info())
    venta3.mostrar_articulos_vendidos()
    descuento_a_aplicar = DescuentoLealtad()
    total_final = venta3.total(descuento_a_aplicar)
    print(f"Total de la venta con descuento: ${total_final:.2f}")
    print("_"*30)
    print(f"ventas registradas: {len(tienda.ventas)}")
if __name__ == "__main__":
    funcion_principal()








