from utils.formatName import formatNamePdf

def RenamePdf(pdf):
    replace = {' ': '_'}
    newPdf = ''.join(replace.get(c, c) for c in pdf)
    
    return formatNamePdf(newPdf)

