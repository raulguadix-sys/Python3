v1 = int(input("Introduce una velocidad:"))
v2 = int(input("Introduce una velocidad:"))

distancia = float(input("Introduce la distancia que hay entre los dos vehículos: "))

tiempo_minutos = int((distancia / (v1 - v2)) * 60)

print(f"El vehículo alcanzará al otro en {tiempo_minutos} minutos.")