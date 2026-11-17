m2 = int(input("Introduce el número de monedas de 2€: "))
m1 = int(input("Introduce el número de monedas de 1€: "))
c50 = int(input("Introduce el número de monedas de 50 céntimos: "))
c20 = int(input("Introduce el número de monedas de 20 céntimos: "))
c10 = int(input("Introduce el número de monedas de 10 céntimos: "))

total_centimos = (m2 * 200) + (m1 * 100) + (c50 * 50) + (c20 * 20) + (c10 * 10)

euros = total_centimos // 100
centimos = total_centimos % 100

print(f"Tenemos {euros} euros y {centimos} céntimos.")