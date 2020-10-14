import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format

# > Inputs
texto = input("Ingrese Su Texto: ")
colores = input("Ingresa el color de tu Ascii: ")
font = input("Ingresa una fuente valida: ")

# > Condiciones
while texto == "":
    print("Debes ingresar un texto")
    break
else:
    cprint(figlet_format(texto, font=font), colores) 
