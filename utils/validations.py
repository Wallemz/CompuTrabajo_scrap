import json

# Revisar si un string es un JSON valido
def is_json(variable):
    try:
        json.loads(variable)
        return True
    except json.JSONDecodeError:
        return False

# Revisar si la respuesta es un documento HTML
def is_html(response: str) -> bool:
    if "<html" in response.lower() or "<head" in response.lower():
        return True
    return False