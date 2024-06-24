import os
from utils.rename import RenamePdfGuideTeaching , RenamePdfCv
from utils.link import process_pdfs

def GuideTeaching(DIR,base_url):
    ArchElements = os.listdir(DIR)
    for el in ArchElements:
        ROUTE= f'{DIR}/{el}'
        NEW_ROUTE = f'{DIR}/{RenamePdfGuideTeaching(el)}'
        os.rename(ROUTE, NEW_ROUTE)
    process_pdfs(DIR,base_url)
def Cv(DIR, base_url):
    
    ArchElements = os.listdir(DIR)
    for el in ArchElements:
        ROUTE= f'{DIR}/{el}'
        NEW_ROUTE = f'{DIR}/{RenamePdfCv(el)}'
        os.rename(ROUTE, NEW_ROUTE)
    process_pdfs(DIR,base_url) 