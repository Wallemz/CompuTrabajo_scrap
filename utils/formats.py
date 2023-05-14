import unicodedata

# Convertir texto a lower case, cambiar espacio por underscores y quitar tildes.
def format_string(texto: str):
    # Convertir a minúsculas
    texto = texto.lower()
    
    # Eliminar tildes
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    
    # Reemplazar espacios por guiones bajos
    texto = texto.replace(' ', '-')
    
    return texto


