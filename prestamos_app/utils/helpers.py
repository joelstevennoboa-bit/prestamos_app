def pedir_valor(mensaje, funcion):
    while True:
        valor = input(mensaje)
        if funcion(valor):
            return valor
        print("Dato inválido")


