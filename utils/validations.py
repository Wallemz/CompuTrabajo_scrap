import json

# Revisar si un string es un JSON valido
def is_json(variable) -> bool:
    """Valida si una variable contiene un json válido.

    Args:
        variable (_type_): Variable con json

    Returns:
        bool: Booleano con validación
    """
    try:
        json.loads(variable)
        return True
    except json.JSONDecodeError:
        return False

# Revisar si la respuesta es un documento HTML
def is_html(response: str) -> bool:
    """Valida si un string contiene etiquetas HTML.

    Args:
        response (str): String a validar.

    Returns:
        bool: Booleano con la validación
    """
    return "<html" in response.lower() or "<head" in response.lower()