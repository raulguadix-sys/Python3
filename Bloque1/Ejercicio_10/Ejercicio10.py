nota1 = float(input("Introduce la primera nota: "))
nota2 = float(input("Introduce la segunda nota: "))
nota3 = float(input("Introduce la tercera nota: "))
examen_final = float(input("Introduce la nota del examen final: "))
trabajo_final = float(input("Introduce la nota del trabajo final: "))

promedio_notas = (nota1 + nota2 + nota3) / 3 * 0.55
promedio_examen = examen_final * 0.30
promedio_trabajo = trabajo_final * 0.15

nota_final = promedio_notas + promedio_trabajo + promedio_examen
print(f"La nota final del curso es un {nota_final}")