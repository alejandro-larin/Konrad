import os
from utils.travel import TrabelPdf
os.system('cls')
#Class
class Menu:
    def Menu_1(self):
        print(
'''
Welcome to Konrad!
-------------------------------------------------------------------------
1. Link Base.
2. Abbreviation.
3. PDF name conversion option.
''')
    def Menu_2(self):
        print(
'''
Konrand Sub Menu
-------------------------------------------------------
1. Curriculum
2. Planning Studing
3. Returning 
''')
menu = Menu()

# Especificar el directorio
DIR = './pdf'
# TrabelPdf(DIR)



menu.Menu_1()
menuResponse= int(input("Plase write one option of the menu: "))
response=True

while response == True:
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
        menuResponse_2= int(input("Plase write one option of the menu: "))
        
        if menuResponse_2 == 1:
            print('b-1')
            continue
        elif menuResponse_2 == 2:
            print ('b-2')
            continue
        elif menuResponse_2 == 3:
            print('o')
            os.system('cls')

        else:
            os.system('cls')
            continue
    else:
        os.system('cls')
    #Response of the user
    #Menu Option
    menu.Menu_1()
    menuResponse= int(input("Plase write one option of the menu: "))
print('Exit...')







