

class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre: str = nombre
        self.precio: float = precio
        self.stock: int = stock

    def vender(self, cantidad: int) -> None:
        try:
            if cantidad > self.stock:
                raise ValueError("Stock insuficiente")

            self.stock -= cantidad
            total: float = cantidad * self.precio
            print(f"Venta exitosa de {cantidad} unidad(es) de {self.nombre}")
            print(f"Total: ${total}")
            print(f"Stock restante: {self.stock}")
            print("---------------------")

        except ValueError as e:
            print(f"Error en la venta de {self.nombre}: {e}")
            print("---------------------")


class ProductoPerecedero(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, dias_vencimiento: int):
        super().__init__(nombre, precio, stock)
        self.dias_vencimiento: int = dias_vencimiento



producto1 = Producto("Laptop", 2500.0, 5)
producto2 = ProductoPerecedero("Leche", 3.5, 10, 7)


producto1.vender(2)
producto2.vender(5)


producto1.vender(10)