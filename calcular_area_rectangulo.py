def calcular_area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2

base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))

area = calcular_area_triangulo(base, altura)
print(f"El área del triángulo es: {area}")


