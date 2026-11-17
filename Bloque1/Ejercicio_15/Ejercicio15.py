variableA = int(input("Introduce la variable numérica A: "))
variableB = int(input("Introduce la variable numérica B: "))

valor = variableA
variableA = variableB
variableB = valor

print(f"Ahora A vale: {variableA}")
print(f"Ahora B vale: {variableB}")