num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 < num2:
    actual = num1
    limite = num2
else:
    actual = num2
    limite = num1

while actual <= limite:
    if actual % 2 == 0:
        print(actual)
    actual += 1