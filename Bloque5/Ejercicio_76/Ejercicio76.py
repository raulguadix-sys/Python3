def EsMultiplo(num1, num2):
    return num1 % num2 == 0

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if EsMultiplo(num1, num2):
    print(f"El número {num1} es múltiplo del número {num2}")
elif EsMultiplo(num2, num1):
    print(f"El número {num2} es múltiplo del número {num1}")
else:
    print("Ningún número es múltiplo del otro.")