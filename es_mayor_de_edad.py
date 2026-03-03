def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18



edad_usuario = int(input("Ingresa tu edad: "))


if es_mayor_de_edad(edad_usuario):
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
