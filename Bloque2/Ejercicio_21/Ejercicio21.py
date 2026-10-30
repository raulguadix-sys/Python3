numero = int(input("Introduce un número: "))

#Le doy valor 1 a la variable i y a factorial.
factorial = 1
i = 1

while i <= numero:
    factorial = factorial * i
    i = i + 1

print(f"El factorial de {numero} es {factorial}")