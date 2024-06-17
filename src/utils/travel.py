import os
from utils.rename import RenamePdf

def TrabelPdf(DIR):
    ArchElements = os.listdir(DIR) 
    for el in ArchElements:
        ROUTE= f'./pdf/{el}'
        NEW_ROUTE = f'./pdf/{RenamePdf(el)}'
        os.rename(ROUTE, NEW_ROUTE)