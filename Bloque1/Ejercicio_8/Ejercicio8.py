sueldo_base = float(input("Introduce el sueldo base: "))
venta1 = float(input("Introduce el valor de la primera venta: "))
venta2 = float(input("Introduce el valor de la segunda venta: "))
venta3 = float(input("Introduce el valor de la tercera venta: "))

total_ventas = venta1 + venta2 + venta3
comisión = total_ventas * 0.10
total = sueldo_base + comisión

print(f"El sueldo que obtendrá por comisiones es de {comisión} y el que obtendrá en total es de {total}")