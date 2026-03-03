class MascotaVirtual:
    def __init__(self,nombre:str):
        self.nombre:str=nombre
        self.energia: int=10
    def jugar(self) -> None:
        self.energia -=3
        print(f"{self.nombre} esta jugando ")
        print(f"Energia actual: {self.energia}")
        print("------------------")
    def dormir(self) -> None:
        self.energia +=5
        print(f"{self.nombre} esta durmiento")
        print(f"Energia actual: {self.energia}")
        print("------------------")


mascota= MascotaVirtual("Luna")

mascota.jugar()
mascota.dormir()
