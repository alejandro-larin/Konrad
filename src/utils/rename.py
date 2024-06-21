from utils.formatName import formatNamePdfCapitalize

def RenamePdfGuideTeaching(pdf):
    if not pdf.lower().endswith('.pdf'):
        raise ValueError("El archivo no tiene la extensión '.pdf'")
    
    name, ext = pdf.rsplit('.', 1)
    replace = {' ': '_', '.': '_'}
    new_name = ''.join(replace.get(c, c) for c in name)
    

    formatted_name = formatNamePdfCapitalize(new_name)
    return f"{formatted_name}.pdf"

def RenamePdfCv(pdf):
    if not pdf.lower().endswith('.pdf'):
        raise ValueError("El archivo no tiene la extensión '.pdf'")
    
    name, ext = pdf.rsplit('.', 1)
    replace = {' ': '.', '_': '.'}
    new_name = ''.join(replace.get(c, c) for c in name)
    
    formatted_name = new_name.lower()
    return f"{formatted_name}.pdf"