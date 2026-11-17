hh = int(input("Introduce las horas de salida: "))
mm = int(input("Introduce los minutos de salida: "))
ss = int(input("Introduce los segundos de salida: "))
t = int(input("Introduce el tiempo de viaje en segundos: "))

total_segundos = (hh * 3600) + (mm * 60) + ss + t

horas_llegada = (total_segundos // 3600) % 24
minutos_llegada = (total_segundos % 3600) // 60
segundos_llegada = total_segundos % 60

print(f"Hora de llegada: {horas_llegada}:{minutos_llegada}:{segundos_llegada}")