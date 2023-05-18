import re
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


def salary_to_number(salary: str):
    # Remove all non-digit characters
    if not salary:
        return ""
    
    try:
        # Remove any non-digit character, except for dot and comma
        salary = re.sub(r"[^\d.,]", "", salary)

        # Split by comma and take the first part (to remove the ",00")
        salary = salary.split(",")[0]

        # Replace dots with nothing to convert to a plain number
        salary = salary.replace(".", "")

        # Convert to an integer
        return int(salary)
    except Exception as e:
        print(f"Could not parse Salary {salary} - {e}")
        return ""