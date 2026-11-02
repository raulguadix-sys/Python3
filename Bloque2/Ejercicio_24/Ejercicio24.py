cantidad = int(input("Cuántos números vas a introducir?: "))

mayores = 0
menores = 0
iguales = 0
contador = 0

while contador < cantidad:
    numero = int(input("Introduce un número: "))

    if numero > 0:
        mayores = mayores + 1
    elif numero < 0:
        menores = menores + 1
    else:
        iguales = iguales + 1
    
    contador = contador + 1 #Para que avance de número.

print(f"Números mayores que 0: {mayores}")
print(f"Números menores que 0: {menores}")
print(f"Números iguales a 0: {iguales}")