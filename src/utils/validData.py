#Does validation of names that are joined to fix them by hand
import os
from utils.formatName import  formatNamePdfRemoveAccents, formatNameSetting
from colorama import Style, Fore

def validNamePdf(pdf):
    name, ext = pdf.rsplit('.', 1)
    replace = {' ': '.', '_': '.'}
    new_name = ''.join(replace.get(c, c) for c in name)
    formatted_name = formatNamePdfRemoveAccents(new_name.lower())
    formatted_name_setting = formatNameSetting(formatted_name)
    
    if ext.lower() == 'pdf':
        if '.' not in formatted_name_setting:  
            return (formatted_name_setting, 'invalid')
        else:
            return (formatted_name_setting, 'valid')
    else:
        return (None, 'not_pdf')
#---------------RUN METHOD---------------
def startProccesValid():
    invalidNames = []
    validNames = []

    for arch in os.listdir('pdf'):
        formatted_name, status = validNamePdf(arch)
        if status == 'invalid':
            invalidNames.append(formatted_name)
        elif status == 'valid':
            validNames.append(formatted_name)

    print(Fore.RED + "Invalid Names:")
    print(invalidNames)
    print(Style.RESET_ALL)

    print(Fore.GREEN + "Valid Names:")
    print(validNames)
    print(Style.RESET_ALL)
