cadena = input("Introduce una cadena: ")
caracter = input("Introduce un caracter: ")

contador = 0

for c in cadena:
    if c == caracter:
        contador = contador + 1

print(f"El caracter aparece {contador} veces")