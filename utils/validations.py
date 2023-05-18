import json
import os

def is_json(variable: str | bytes | bytearray) -> bool:
    """Check if a string is a valid JSON

    Args:
        variable (str | bytes | bytearray): Variable to check

    Returns:
        bool: _description_
    """
    try:
        json.loads(variable)
        return True
    except json.JSONDecodeError:
        return False

def is_html(response: str) -> bool:
    """Check if response contains html tags

    Args:
        response (str): String to check

    Returns:
        bool: _description_
    """
    return "<html" in response.lower() or "<head" in response.lower()

def ensure_dir(directory: str) -> bool:
    """Check if a dolder exists if not creates it.

    Args:
        directory (str): Folder path

    Returns:
        bool: Created, already created or not
    """
    try:
        os.makedirs(directory)
        print("Output folder created")
        return True
    except FileExistsError:
        print(f"Output folder already exists")
        return True
    except Exception as e:
        print(f"Could not create output folder -{e}")
        return False