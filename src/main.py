import os
from utils.travel import TrabelPdf
from colorama import init, Fore, Style
os.system('cls')
#Class
class Menu:
    def Menu_1(self):
        print(
f'''
{Style.BRIGHT}{Fore.CYAN}Welcome to Konrad!
-------------------------------------------------------------------------{Fore.RESET}
{Fore.YELLOW}1. Link Base.
2. Abbreviation.
3. PDF name conversion option.{Fore.RESET}
{Fore.RED}4. Exit{Fore.RESET}
''')
    def Menu_2(self):
        print(
f'''
{Fore.CYAN}Konrand Sub Menu
-------------------------------------------------------{Fore.RESET}
{Fore.YELLOW}1. Curriculum
2. Planning Studing{Fore.RESET}
{Fore.RED}3. Returning {Fore.RESET}
''')
menu = Menu()

# Especificar el directorio
DIR = './pdf'
 



menu.Menu_1()
menuResponse= int(input(f"{Fore.MAGENTA}Plase write one option of the menu: {Fore.RESET}"))


while True:
    #Menu Structure 
    if menuResponse == 1:
        print('Option 1')
        os.system('cls')
    elif menuResponse == 2:
        print('Option 2')
        os.system('cls')
    elif menuResponse == 3:
        os.system('cls')
        #Print menu
        menu.Menu_2()
        subMenuResponse= int(input("Plase write one option of the menu: "))
        
        if subMenuResponse == 1:
            print('b-1')
            continue
        elif subMenuResponse == 2:
            print('Change...')
            TrabelPdf(DIR)
            continue
        elif subMenuResponse == 3:
            os.system('cls')
        else:
            os.system('cls')
            continue
    elif menuResponse == 4:
        break
    else:
        os.system('cls')
    #Menu Option
    menu.Menu_1()
    menuResponse= int(input(f"{Fore.MAGENTA}Plase write one option of the menu: {Fore.RESET}"))
print(f'Exit... {Style.RESET_ALL}')
os.system('cls')








