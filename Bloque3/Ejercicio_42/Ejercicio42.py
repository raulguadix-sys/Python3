cadena = input("Introduce una cadena: ")
subcadena = input("Introduce una subcadena: ")

inicio = cadena[:len(subcadena)]

if inicio == subcadena:
    print("La cadena empieza por la subcadena")
else: 
    print("La cadena no empieza por la subcadena")
    