from colorama import init, Fore, Style
from time import sleep
import os
class Menu:
    def __init__(self):
        pass
#---------------PRINCIPAL---------------
    def Menu(self):
        print(
f'''
{Style.BRIGHT}{Fore.CYAN}Welcome to Konrad!
-------------------------------------------------------------------------{Fore.RESET}
{Fore.YELLOW}1. Link Base.
2. Abbreviation.
3. PDF name conversion option.{Fore.RESET}
{Fore.RED}4. Delete{Fore.RESET}
{Fore.RED}5. Exit...{Fore.RESET}
''')
#---------------SUBMENU 1---------------

#---------------SUBMENU 2---------------

#---------------SUBMENU 3---------------
    def SubMenu_3(self):
        print(
f'''
{Fore.CYAN}Konrand SubMenu
-------------------------------------------------------{Fore.RESET}
{Fore.YELLOW}1. Curriculum
2. Planning Studing{Fore.RESET}
{Fore.RED}3. Returning... {Fore.RESET}
''')
#---------------ERROR---------------      
    def MenuError(self):
        print(f'{Fore.RED}This option not existing in this menu...{Fore.RESET}')
        sleep(1)
        os.system('cls')
#---------------WARNING---------------
    def Warning(self):
        os.system('cls')
        print(
f'''
{Fore.YELLOW}                       WARNING
-------------------------------------------------------{Fore.RESET}
''')
#---------------ALERT---------------
    def AcceptAlert(self):
        print(f'{Fore.GREEN}--Accepted--{Fore.RESET}')
        sleep(1)
    def CancelledAlert(self):
        print(f'{Fore.RED}--Cancelled--{Fore.RESET}')
        sleep(1)
    def RenamedFilesAlert(self):
        print(f'{Fore.GREEN}--Renamed Files--{Fore.RESET}')
        sleep(1)