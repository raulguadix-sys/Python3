cadena = input("Introduce una cadena de caracteres: ")

diccionario = {}

for elemento in cadena:
    if elemento in diccionario:
        diccionario[elemento] += 1
    else:
        diccionario[elemento] = 1

print(f"La cantidad de apariciones de cada carácter es: {diccionario}")