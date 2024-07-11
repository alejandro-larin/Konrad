# The menu class calls alerts and submenus to save lines of code or keep the main cleaner
from colorama import init, Fore, Style
from time import sleep
import os
from utils.clear import ClearConsole
class Menu:
    def __init__(self):
        pass
#---------------MENU---------------
    def Menu(self):
        print(
f'''
{Style.BRIGHT}{Fore.CYAN}Welcome to Konrad!
-------------------------------------------------------------------------{Fore.RESET}
{Fore.YELLOW}1. PDF name conversion option.{Fore.RESET}
{Fore.RED}2. Delete{Fore.RESET}
{Fore.RED}3. Exit...{Fore.RESET}
''')
#---------------SUBMENU 2---------------
    def SubMenu_2(self):
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
        sleep(1.5)
        ClearConsole()
#---------------WARNING---------------
    def Warning(self):
        ClearConsole()
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
    def GoodByeAlert(self):
        print(f'{Fore.YELLOW}-- GOOD BYE !!!--')
        print('''

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣶⣶⣾⣿⣿⣿⣿⣷⣶⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⡳⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡌⢳⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣿⣄⣀⣤⠄⠀
⠀⠀⠀⠀⠀⠀⠀⢸⢃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣿⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢸⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⡟⠉⢿⢿⣿⠈⢿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠹⣿⣿⣿⣿⣿⣿⠃⠀⢸⠈⠏⠀⠈⢻⣿⣿⣿⣿⣿⡿⣇⠀⠀⠀
⠀⠀⠀⣤⡀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢹⡜⢿⣿⡄⠀⠈⢿⣿⣿⣿⠏⠠⠚⣡⣴⣶⠾⠿⢾⣿⣿⣿⣿⣿⣇⠛⠀⠀⠀
⠀⠀⠀⠈⠛⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⡏⠙⣿⣿⡇⠀⠑⢊⣻⣷⣐⡂⢀⣸⠿⣿⣧⠀⠿⠛⠉⠀⠀⠀⣸⡟⠻⣿⣿⣿⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⢸⠉⣿⣧⣴⣾⡿⠿⠟⠛⠋⠀⠀⠀⠀⠉⠓⠀⠀⠀⠀⠠⣠⢛⣧⢰⣿⣿⣿⣇⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⡇⢸⠀⢹⡿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢁⣾⢁⡾⠃⣹⣿⣿⣿⣿⢿⡶
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣯⠻⣝⣿⣿⣷⠈⠀⠀⢷⣄⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⢀⣼⠛⠋⠀⣰⣿⡿⠟⢉⡴⠋⠀
⠀⢀⣀⣰⢾⡏⢀⠀⠀⠀⠀⠀⠈⢙⡟⢿⣄⠀⠀⠀⠈⠙⠛⠓⠲⣤⡀⠀⣀⡀⠀⠀⣠⠖⠀⠀⣠⠞⠁⠀⠀⢠⣿⡟⠀⠀⡞⠁⠀⠀
⠸⣯⣉⡁⠘⣉⡽⠃⠀⠀⠀⠀⠀⣼⠹⡄⢿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠙⢦⠀⠉⠉⠉⠁⠀⢀⣼⠋⠀⠀⠀⢠⣿⣿⠀⠀⢰⡇⠀⠀⠀
⠀⠀⣸⣡⠾⣿⣷⠄⠀⠀⠀⠀⢰⡏⠀⢱⡾⠀⠈⢿⣷⣤⣀⠀⠀⠀⠀⣸⢷⣤⣄⣀⣀⣤⡿⠏⠀⠀⠀⢠⣿⣿⡇⠀⠀⡼⠀⠀⠀⠀
⠀⠀⠙⠁⠀⠈⠁⠀⠀⠀⠀⠀⣿⠁⠀⢸⠙⣆⡀⠈⣿⣿⡟⠙⠂⠀⠀⡟⠀⣿⣿⣿⡿⢻⡀⠀⠀⠀⠀⠀⠹⣿⠃⠀⣼⠁⠀⠀⡀⠀
''')