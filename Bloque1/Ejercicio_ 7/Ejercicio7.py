total_minutos = int(input("Introduce la cantidad de minutos: "))

horas = total_minutos // 60
minutos = total_minutos % 60

print(f"{total_minutos} minutos son {horas} horas y {minutos} minutos")