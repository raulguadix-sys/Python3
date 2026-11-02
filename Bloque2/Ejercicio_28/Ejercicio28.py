inferior = int(input("Límite inferior: "))
superior = int(input("Límite superior: "))

while inferior > superior:
    inferior = int(input("Límite inferior: "))
    superior = int(input("Límite superior: "))

suma_dentro = 0
fuera = 0
igual_limites = False

num = int(input("Introduce un número o 0 para salir"))

while num != 0:
    if num > inf and num < sup:
        suma_dentro += num
    elif num < inf or num > sup:
        fuera += 1
    else:
        igual_limites = True

    num = int(input("Introduce un número (0 para salir): "))

print(f"Suma dentro del intervalo: {suma_dentro}")
print(f"Números fuera del intervalo: {fuera}")
print(f"¿Se ha introducido algún límite?: {igual_limites}")