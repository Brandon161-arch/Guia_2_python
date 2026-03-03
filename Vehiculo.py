class Vehiculo:
    def __init__(self, marca: str, modelo: str, anio: int):
        self.marca: str = marca
        self.modelo: str = modelo
        self.anio: int = anio
        self.estado: str = "bien"
vehiculo1 = Vehiculo("Toyota", "Corolla", 2020)
vehiculo2 = Vehiculo("Ford", "Fiesta", 2018)
print("Vehículo 1:")
print(vehiculo1.marca)
print(vehiculo1.modelo)
print(vehiculo1.anio)
print(vehiculo1.estado)

print("\nVehículo 2:")
print(vehiculo2.marca)
print(vehiculo2.modelo)
print(vehiculo2.anio)
print(vehiculo2.estado)