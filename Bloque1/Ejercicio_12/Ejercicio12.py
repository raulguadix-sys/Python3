import math

x1 = float(input("Introduce un número: "))
y1 = float(input("Introduce un número: "))
x2 = float(input("Introduce un número: "))
y2 = float(input("Introduce un número: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"La distancia entre los puntos es {distancia}")