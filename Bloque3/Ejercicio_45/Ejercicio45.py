nombre = input("Introduce tu nombre y apellidos: ")

iniciales = ""
siguiente_es_inicial = True

for c in nombre:
    if c == " ":
        siguiente_es_inicial = True
    elif siguiente_es_inicial:
        iniciales = iniciales + c.upper()
        siguiente_es_inicial = False

print(f"Las iniciales son: {iniciales}")