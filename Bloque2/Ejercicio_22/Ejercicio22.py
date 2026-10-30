import random
numero_secreto = random.randint(1, 100)

intentos = 10
print("Tienes 10 intentos para adivinar un número del 1 al 100.")

while intentos > 0:
    n = int(input("Introduce un número: "))

    if n == numero_secreto:
        intentos_usados = 10 - intentos + 1
        print(f"Enhorabuena has acertado en {intentos_usados} intentos.")
        break

    intentos -=1

    if n < numero_secreto:
        print(f"El número secreto es mayor. Te quedan {intentos} intentos.")
    else:
        print(f"Es número secreto es menor. Te quedan {intentos} intentos.")

if intentos == 0 and n != numero_secreto:
    print(f"¡Te has equivocado crack. El número secreto era: {numero_secreto}")    