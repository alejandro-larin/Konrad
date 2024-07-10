#Sustituye los espacios entre "." o "_" 

from utils.formatName import formatNamePdfCapitalize,formatNamePdfRemoveAccents,formatNameSetting
from time import sleep
def RenamePdfGuideTeaching(pdf):

    name, ext = pdf.rsplit('.', 1)
    replace = {' ': '_', '.': '_'}
    new_name = ''.join(replace.get(c, c) for c in name)
    formatted_name = formatNamePdfRemoveAccents(formatNamePdfCapitalize(new_name))
    return f"{formatted_name}.pdf"

def RenamePdfCv(pdf):
    name, ext = pdf.rsplit('.', 1)
    replace = {' ': '.', '_': '.'}
    new_name = ''.join(replace.get(c, c) for c in name)
    formatted_name = formatNamePdfRemoveAccents(new_name.lower())
    fotmatted_name_setting = formatNameSetting(formatted_name)
    return f"{fotmatted_name_setting}.pdf"