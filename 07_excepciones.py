class CajeroAutomatico:
    def __init__(self):
        self.efectivo_disponible: float = 10000.0
    def solicitar_retiro(self) -> None:
        print("Bienvenido al cajero")
        try:
            monto_str: str=input("Ingrese la cantidad a retirar(solo numeros)")
            monto: float = float(monto_str)
            if monto ==0:
                raise ValueError("No puede retirar cero pesos.")
            self.efectivo_disponible -= monto
            print(f"Retiro Exitoso. Quedan ${self.efectivo_disponible} en el cajero")
        except ValueError as es:
            print(f"Error de formato : usted ingreso caracteres invalidos.")
        except Exception as e:
            print("Error desconocido")
        finally:
            print("Expulsando tarjeta...Gracias por utilizar nuestra red")
mi_cajero= CajeroAutomatico()
mi_cajero.solicitar_retiro()

  