notas = []

print("Introduce las 5 notas: ")
notas.append(float(input("Nota 1: ")))
notas.append(float(input("Nota 2: ")))
notas.append(float(input("Nota 3: ")))
notas.append(float(input("Nota 4: ")))
notas.append(float(input("Nota 5: ")))

print(f"Tus notas son: {notas}")

suma = notas[0] + notas[1] + notas[2] + notas[3] + notas[4]
media = suma / 5

alta = max(notas)
baja = min(notas)

print(f"Nota media: {media}")
print(f"Nota más alta: {alta}")
print(f"Nota más baja: {baja}")