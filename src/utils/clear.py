# This function is used for the menu and clearing the console in any operating system
from platform import system

import os 
def ClearConsole():
    if system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')