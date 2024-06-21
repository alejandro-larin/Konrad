import os
from time import sleep
from utils.travel import GuideTeaching,Cv
from utils.Class.MenuClass import Menu
from colorama import init, Fore, Style
os.system('cls')
#Class
menu = Menu()
# Especificar el directorio
DIR = './pdf'
# Menu

while True:
    os.system('cls')
    #Menu Option Reponse
    menu.Menu()
    menuResponse= int(input(f"{Fore.MAGENTA}Plase write one option of the menu: {Fore.RESET}"))
    #Menu Structure 
    if menuResponse == 1:
        print('Option 1')
        os.system('cls')
    elif menuResponse == 2:
        print('Option 2')
        os.system('cls')
    elif menuResponse == 3:
        os.system('cls')
        menu.SubMenu_3()
        subMenuResponse= int(input(f"{Fore.MAGENTA}Plase write one option of the menu: {Fore.RESET}"))
        #SubMenu Structure
        if subMenuResponse == 1:
            Cv(DIR)
            menu.RenamedFilesAlert()
            os.system('cls')
            continue
        elif subMenuResponse == 2:
            GuideTeaching(DIR)
            menu.RenamedFilesAlert()
            os.system('cls')
            continue
        elif subMenuResponse == 3:
            os.system('cls')
        else:
            menu.MenuError()
            continue
    elif menuResponse == 4:
        menu.Warning()
        response=input(f'{Fore.MAGENTA}Are you sure to delete this folder?{Fore.RESET} {Fore.GREEN}[S/N]?:{Fore.RESET} ').lower()
        if response == 's':
            menu.AcceptAlert()
            continue
        else:
            menu.CancelledAlert()
            continue
    elif menuResponse == 5:
        break
    else:
        menu.MenuError()
   
print(f'Exit... {Style.RESET_ALL}')
os.system('cls')








