import unicodedata

# Convertir texto a lower case, cambiar espacio por underscores y quitar tildes.
def format_string(texto: str) -> str:
    """Convierte un string al formato requerido:
    * Todo minúsculas
    * Sin tíldes
    * Espacios reemplazados por guión bajo

    Args:
        texto (str): Texto a formatear

    Returns:
        str: Texto formateado
    """
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