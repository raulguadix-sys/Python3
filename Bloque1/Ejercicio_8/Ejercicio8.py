sueldo_base = float(input("Introduce el sueldo base: "))
venta1 = float(input("Introduce el valor de la primera venta: "))
venta2 = float(input("Introduce el valor de la segunda venta: "))
venta3 = float(input("Introduce el valor de la tercera venta: "))

total_ventas = venta1 + venta2 + venta3
comision = total_ventas * 0.10
sueldo_total = sueldo_base + comision

print(f"Dinero obtenido por comisiones: {comision:.2f} €")
print(f"Sueldo total a recibir en el mes: {sueldo_total:.2f} €")