#This contains the menu structure for the user to choose the functionality they want
import os
from time import sleep
from utils.travel import GuideTeaching,Cv
from utils.Class.MenuClass import Menu
from colorama import init, Fore, Style
from utils.link import read_conf_file
import glob
from utils.clear import ClearConsole
ClearConsole()
menu = Menu()
DIR = './pdf'

try:
    while True:
        #---------------MENU---------------
        ClearConsole()
        menu.Menu()
        menuResponse= int(input(f"{Fore.MAGENTA}Plase write one option of the menu: {Fore.RESET}"))
        #---------------ESTRUCTURE---------------
        if menuResponse == 1:
            ClearConsole()
            menu.SubMenu_2()
            subMenuResponse= int(input(f"{Fore.MAGENTA}Please write one option of the menu: {Fore.RESET}"))
            #---------------SUBMENU---------------
            if subMenuResponse == 1:
                config = read_conf_file('config.conf')
                base_url = config['urlCv']
                ClearConsole() 
                Cv(DIR,base_url)
                menu.RenamedFilesAlert()
                ClearConsole()
                continue
            elif subMenuResponse == 2:
                config = read_conf_file('config.conf')
                base_url = config['urlGuie']
                ClearConsole()
                GuideTeaching(DIR,base_url)
                menu.RenamedFilesAlert()
                continue
            elif subMenuResponse == 3:
                ClearConsole()
            else:
                menu.MenuError()
                continue
        elif menuResponse == 2:
            menu.Warning()
            response=input(f'{Fore.MAGENTA}Are you sure to delete this folder?{Fore.RESET} {Fore.GREEN}[Y/N]?:{Fore.RESET} ').lower()
            if response == 'y':
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
    #---------------FINALLY---------------
    print(f'{Style.RESET_ALL}')
    ClearConsole()

except KeyboardInterrupt:
    ClearConsole()
    menu.GoodByeAlert()
    sleep(1)
    print(f'{Style.RESET_ALL}')
    ClearConsole()
    ClearConsole()



