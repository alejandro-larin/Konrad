import unicodedata

def formatNamePdf(text):
    normalized = unicodedata.normalize('NFD', text.title())
    return ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')