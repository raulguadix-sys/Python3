frase = input("Introduce una frase: ")

contador = 1

for c in frase:
    if c == " ":
        contador = contador + 1

print(f"La frase tiene {contador} palabras")