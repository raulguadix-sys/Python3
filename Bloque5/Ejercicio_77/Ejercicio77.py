def Login(usuario, contraseña, intentos):
    if usuario == "usuario1" and contraseña == "asdasd":
        return True, intentos
    else:
        intentos += 1
        return False, intentos

intentos = 0
acceso = False

while intentos < 3 and not acceso:
    usuario = input("Introduce el nombre de usuario: ")
    contraseña = input("Introduce la contraseña: ")
    acceso, intentos = Login(usuario, contraseña, intentos)
    if not acceso:
        print(f"Los datos son incorrectos. Te quedan {3 - intentos} intentos.")
    else:
        print("¡Bienvenido!")

if not acceso:
    print("Has superado el número máximo de intentos. Cuenta bloqueada.")