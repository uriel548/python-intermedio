#verificar datos (nombre, edad y correo ) de un usuario
def verificar_name(nombre):
    if type(nombre) is not str:
        raise TypeError("El nombre "
                        "tiene que ser una cadena de texto")
    if not nombre.strip():
        raise ValueError("el nombre no puede estar vacio")
#.strip eliminar espacios,
# .replace para eliminar los espacios en medio y solo queden las letras,
# .isalpha para comprobar si solo hay letras
    if not nombre.strip().replace(' ', '').isalpha():
        raise ValueError(f"los numeros no son validos")

def verificar_edad(edad):
    if type(edad) is not int:
        raise TypeError(f"La edad debe ser un numero entero.")
    if edad <= 0:
        raise ValueError(f"La edad no puede ser cero")


def verificar_email(correo, extensiones_permitidas):
    if type(correo) is not str:
        raise TypeError(f"El correo tiene que"
                        f" ser una cadena de texto.")
    if "@" not in correo:
        raise ValueError(f"El cooreo debe contener el simbolo '@'")
    partes = correo.split('@')
    if len(partes) != 2 or not partes[0] or not partes[1]:
        raise ValueError(F"el formato del correo es incorrecto")
    dominio = partes[1]
    if dominio not in extensiones_permitidas:
        nombres = ",".join(extensiones_permitidas)
        raise ValueError(f"el correo debe ser uno de"
                         f" los siguientes dominios: {nombres}.")
    return True


def validar_datos():
    extensiones_permitidas = ["gmail.com", "outlook.com",
                              "yahoo.com", "icloud.com",
                              "protonmail.com", "zoho.com"]
    print(f"---VALIDAR DATOS---\n")
    while True:
        try:
            dato_nombre = input("INGRES TU NOMBRE COMPLETO:")
            verificar_name(dato_nombre)
            print(f"NOMBRE'{dato_nombre}' correcto")
            break

        except TypeError as e:
            print(f"x ERROR de tipo capturado: {e}")

        except ValueError as e:
            print(f" x ERROR de valor capturado: {e}")

        except Exception as e:
            print(f"ERROR INESPERADO: {e}")
        finally:
            print(f"Registro finalizado.")

    while True:
        dato_edad = input("INGRESA TU EDAD")
        try:
            dato_edad_num = int(dato_edad)
            verificar_edad(dato_edad_num)
            print(f"edad`{dato_edad_num}` correcto")
            break
        except TypeError as e:
            print(f"X Error de tipo : {e} ")
        except ValueError as e:
            print(f"X ERROR de valor capturado: {e}")
        except Exception as e:
            print(f"Error inesperado:{e}")
        finally:
            print(f"Registro finalizado.")

    while True:
        try:
            dato_correo = input("INGRESA TU CORREO ELECTRONICO")
            verificar_email(dato_correo, extensiones_permitidas)
            print(f"correo: {dato_correo} correcto")
            break
        except TypeError as e:
            print(f"X ERROR de tipo:{e}")
        except ValueError as e:
            print(f"X ERROR de valor:{e}")
        except Exception as e:
            print(f"Error inesperado:{e}")
        finally:
            print(f"Registro finalizado.")

    print(f"\n_____todos los datos son correctos_____")

#llamar ala funcion principal para su ejecuccion
if __name__ == "__main__":
    validar_datos()