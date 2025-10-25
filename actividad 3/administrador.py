from usuario import Usuario

class Administrador (Usuario):
    def __init__ (self, nombre: str, correo: str,
                  permisos: list[str]):
        super().__init__(nombre, correo)
        self.permisos =permisos

    def mostrar_info(self):
        permisos_str =", ".join(self.permisos)
        return (f"Administrador: {self.nombre},"
                f" correo: {self.correo},"
                f" permisos: {', '.join(self.permisos)}")