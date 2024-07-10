#Recorre los archivos y utiliza distintos metodos dependiendo cual de las funciones sean llamadas
import os
from utils.rename import RenamePdfGuideTeaching , RenamePdfCv
from utils.link import process_pdfs
from colorama import Fore
from utils.formatName import formatNameSetting
from time import sleep
ARCH_LINKS = os.path.exists('pdf/all_links.txt')


#---------------TRAVEL GUIE---------------
def GuideTeaching(DIR,base_url):
    #---------------REMOVE---------------
    if  ARCH_LINKS:
        os.remove('pdf/all_links.txt')
    #---------------RENAME---------------
    ArchElements = os.listdir(DIR)
    for el in ArchElements:
        ROUTE= f'{DIR}/{el}'
        NEW_ROUTE = f'{DIR}/{RenamePdfGuideTeaching(el)}'
        os.rename(ROUTE, NEW_ROUTE)
    #---------------URL---------------
    abbreviation= input(f'{Fore.MAGENTA}Write abbreviation: {Fore.RESET}')
    year= input(f'{Fore.MAGENTA}Write the year of PDF: {Fore.RESET}')
    process_pdfs(DIR,base_url,abbreviation,year)



#---------------TRAVEL CURRICULUM---------------
def Cv(DIR, base_url):
    if  ARCH_LINKS:
        os.remove('pdf/all_links.txt')
    #---------------RENAME---------------
    ArchElements = os.listdir(DIR)
    for el in ArchElements:
        ROUTE= f'{DIR}/{el}'
        NEW_ROUTE = f'{DIR}/{RenamePdfCv(el)}'
        os.rename(ROUTE, NEW_ROUTE)
    #---------------URL--------------
    abbreviation= input(f'{Fore.MAGENTA}Write abbreviation: {Fore.RESET}')
    year= input(f'{Fore.MAGENTA}Write the year of PDF: {Fore.RESET}')
    process_pdfs(DIR,base_url,abbreviation,year)
    #---------------INVALID NAMES--------------
