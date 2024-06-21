import os
from utils.rename import RenamePdfGuideTeaching , RenamePdfCv

def GuideTeaching(DIR):
    ArchElements = os.listdir(DIR) 
    for el in ArchElements:
        ROUTE= f'./pdf/{el}'
        #Aca poner el Directorio del usuario
        NEW_ROUTE = f'./pdf/{RenamePdfGuideTeaching(el)}'
        os.rename(ROUTE, NEW_ROUTE)
        
def Cv(DIR):
    ArchElements = os.listdir(DIR) 
    for el in ArchElements:
        ROUTE= f'./pdf/{el}'
        NEW_ROUTE = f'./pdf/{RenamePdfCv(el)}'
        os.rename(ROUTE, NEW_ROUTE)