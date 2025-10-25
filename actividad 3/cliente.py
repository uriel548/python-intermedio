from usuario import Usuario
class Cliente(Usuario):

     def __init__(self, nombre: str, correo: str, saldo: float):
         super().__init__(nombre, correo)
         self.saldo = saldo

     def mostrar_info(self):
         return (f"Cliente: {self.nombre},"
                 f" Correo: {self.correo}, "
                 f"Saldo: ${self.saldo :.2f}")