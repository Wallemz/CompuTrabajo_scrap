import pandas as pd

from typing import Any, Dict, List, Tuple

class CSV:
    """Class to handle a CSV file
    """
    def __init__(self, csv_file_path: str) -> None:
        self.csv_file_path = csv_file_path
    
    def write_to_csv(self, list_of_dicts: List[Dict[str, str]]) -> bool:
        """Writes a CSV File with the List of dictionaries provided.

        Args:
            list_of_dicts (List[Dict[str, str]]): List of Dictionaries

        Returns:
            bool: True if the CSV was successfully writed.
        """
        try:
            df = pd.DataFrame(list_of_dicts)
            df.to_csv(self.csv_file_path, sep = ";", index=False)
            return True
        
        except Exception as e:
            print(f"Could not write CSV file {self.csv_file_path} - {e}")
            return False