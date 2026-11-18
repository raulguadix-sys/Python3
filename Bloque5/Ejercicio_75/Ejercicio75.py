def EscribirCentrado(texto):
    print(" "*(40 - len(texto) // 2) + texto)
    print(" "*(40-len(texto) // 2) + "=" * len(texto))

EscribirCentrado("Hola")
