base = float(input("Introduce un número real: "))
exponente = int(input("Introduce un número entero positivo: "))

resultado = 1
contador = 1

while contador <= exponente:
    resultado = resultado * base
    contador += 1

print(f"El resultado de {base} elevado a {exponente} es: {resultado}")