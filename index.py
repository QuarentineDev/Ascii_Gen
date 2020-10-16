import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format

# > Inputs
texto = input("Ingrese Su Texto: ")
colores = input("Ingresa el color de tu Ascii: ")
font = input("Ingresa una fuente valida: ")
"""
Input pendiente:
fuentes = input("¿Desea imprimir la lista de fuentes? [SI], [NO]: ")
"""

# > Listas
fonts = ['standard', 'graffiti', 'acrobatic', 'avatar', 'big', 'bulbhead', 'doh', 'epic',
        'graceful', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'ogre', 'rectangles',
        'slant', 'small', '3x5', '3-d', 'alligator', 'alligator2', 'alphabet', 'arrows', 'banner',
        'banner3', 'banner4', 'barbwire', 'basic', 'bell', 'binary', 'block', 'broadway', 'bubble',
        'caligraphy', 'catwalk', 'chunky', 'coinstak', 'colossal', 'computer', 'contessa', 'contrast',
        'cosmike']

# > Condiciones
"""
 - ERROR: Al parecer la condicion del usuario si la respuesta es "NO", tiene ciertos fallos -

if fuentes == "SI":
    print(fonts)
    font = input("Ingresa una fuente valida: ")
elif fuentes == "NO":
    font = input("Ingresa una fuente valida: ") 
"""
if texto == "":
    print("Debes ingresar un texto")
elif texto == " ":
    print("Debes ingresar un texto")
elif font == "":
    print("Debes ingresar una fuente")
elif font == " ":
    print("Debes ingresaruna fuente valida")
elif font not in fonts:
    print("Este font no esta disponible")
elif colores == "":
    print("Ese no es un color valido o no has asignado ninguno aun")
elif colores == " ":
    print("Ese no es un color valido o no has asignado ninguno aun")
else:
    cprint(figlet_format(texto, font=font), colores) 
