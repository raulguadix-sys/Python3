suma = 0
contador = 0

numero = int(input("Introduce un número (Introduce 0 para salir): "))

while numero != 0:
    suma += numero
    contador += 1

    numero = int(input("Introduce un número (Introduce 0 para salir: )"))

if contador > 0:
    media = suma / contador
    print(f"La suma total es: {suma}")
    print(f"La media es: {media}")
else:
    print("No se ha introducido ningún número.")
