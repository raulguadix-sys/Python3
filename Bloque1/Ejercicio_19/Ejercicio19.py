correctas = int(input("Introduce el número de respuestas correctas: "))
incorrectas = int(input("Introduce el número de respuestas incorrectas: "))
blanco = int(input("Introduce el número de respuestas en blanco: "))

nota_final = (correctas * 5) + (incorrectas * -1) + (blanco * 0)

print(f"La nota final del estudiante es de un {nota_final}")