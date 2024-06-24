import os
from time import sleep
from utils.travel import GuideTeaching,Cv
from utils.Class.MenuClass import Menu
from colorama import init, Fore, Style
from utils.link import read_conf_file
import glob

os.system('cls')
#Class
menu = Menu()
# Especificar el directorio
DIR = './pdf'
# Menu
while True:
    os.system('cls')
    menu.Menu()
    menuResponse= int(input(f"{Fore.MAGENTA}Plase write one option of the menu: {Fore.RESET}"))
    if menuResponse == 1:
        os.system('cls')
        menu.SubMenu_2()
        subMenuResponse= int(input(f"{Fore.MAGENTA}Plase write one option of the menu: {Fore.RESET}"))
   
        if subMenuResponse == 1:
            config = read_conf_file('config.conf')
            base_url = config['urlCv']
            os.system('cls')
            
            Cv(DIR,base_url)
            menu.RenamedFilesAlert()
            os.system('cls')
            continue
        elif subMenuResponse == 2:
            config = read_conf_file('config.conf')
            base_url = config['urlGuie']
            os.system('cls')

            GuideTeaching(DIR,base_url)
            menu.RenamedFilesAlert()
            continue
        elif subMenuResponse == 3:
            os.system('cls')
        else:
            menu.MenuError()
            continue
    elif menuResponse == 2:
        menu.Warning()
        response=input(f'{Fore.MAGENTA}Are you sure to delete this folder?{Fore.RESET} {Fore.GREEN}[S/N]?:{Fore.RESET} ').lower()
        if response == 's':
            menu.AcceptAlert()
            for extension in ('*.pdf', '*.txt'):
                files = glob.glob(os.path.join(DIR, extension))
                for file in files:
                    os.remove(file)
            continue
        else:
            menu.CancelledAlert()
            continue
    elif menuResponse == 3:
        break
    else:
        menu.MenuError()
print(f'{Style.RESET_ALL}')

os.system('cls')



