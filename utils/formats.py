import re
import unicodedata

from typing import Union

def format_string(texto: str) -> str:
    """Formats a string -> No caps -> No tildes -> No spaces, underscore instead

    Args:
        texto (str): Text to convert.

    Returns:
        str: Formatted text.
    """
    try:
        # To lowercase
        texto = texto.lower()
        
        # Delete tildes
        texto = ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        )
        
        # Replace spaces to underscore
        texto = texto.replace(' ', '-')
        return texto
    
    except Exception as e:
        print(f"Could not parse - {texto} - {e}")
        return ""
    
    
def salary_to_number(salary: str) -> Union[int, str]:
    """Converts "$1.000.000 (mensual)" to just the salary number -> 1000000

    Args:
        salary (str): Text to convert.

    Returns:
        Union[int, str]: Number or empty string
    """
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