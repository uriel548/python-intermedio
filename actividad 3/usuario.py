from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__ (self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo

    @abstractmethod
    def mostrar_info(self):
            pass
#usando SOLId "cerrado o abierto" para evitar ser modificado
class EstrategiaDescuento(ABC):
    @abstractmethod
    def aplicar_descuento(self, total_base: float) -> float:
            pass

class DescuentoLealtad(EstrategiaDescuento):
    def aplicar_descuento(self, total_base: float) -> float:
            # print("  -> Aplicando 10% de descuento por Lealtad.")
        return total_base * 0.90

class DescuentoNinguno(EstrategiaDescuento):
    def aplicar_descuento(self, total_base: float) -> float:
        return total_base  # No aplica descuento