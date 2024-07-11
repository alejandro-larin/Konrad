#It is used to change letters such as capitalization or removing accent marks, anything that has to do with changing the file name. (Linked with "rename.py")
import unicodedata
from unidecode import unidecode

def formatNamePdfCapitalize(text):
    normalized = unicodedata.normalize('NFD', text.title())
    return ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')
    
def formatNamePdfRemoveAccents(text):
    return unidecode(text)

def formatNameSetting(nameArch):
    string = nameArch.split('.')
    if len(string) > 2:
        return '.'.join(string[:2])
    else:
        return nameArch 
    
    


