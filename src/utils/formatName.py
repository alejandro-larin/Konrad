#Se utiliza para cambiar las letras como capitalizar o quitar tildes todo lo que tenga que ver con el cambio del nombre del archivo. (Vinculado con "rename.py")
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
    
    


