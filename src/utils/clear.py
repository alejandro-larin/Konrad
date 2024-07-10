# Esta funcion se utiliza para el menu y limpiar la consola en cualquier sistema operativo

from platform import system

import os 
def ClearConsole():
    if system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')