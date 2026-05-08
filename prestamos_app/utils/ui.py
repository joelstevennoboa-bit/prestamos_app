import os

class Color:
    RESET = "\033[0m"
    VERDE = "\033[92m"
    ROJO = "\033[91m"
    CYAN = "\033[96m"

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def titulo(texto):
    print(Color.CYAN + "="*50)
    print(texto.center(50))
    print("="*50 + Color.RESET)
