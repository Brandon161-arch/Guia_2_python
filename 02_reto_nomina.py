def calcular_salario_neto(salario_base: float, bonificacion: float = 0.0) -> float:
    salud: float = salario_base * 0.08
    pension: float = salario_base * 0.08
    return salario_base - salud - pension + bonificacion


salario = float(input("Ingresa el salario base: "))
bono = float(input("Ingresa la bonificación (0 si no hay): "))

resultado = calcular_salario_neto(salario, bono)

print(f"Salario neto: {resultado}")