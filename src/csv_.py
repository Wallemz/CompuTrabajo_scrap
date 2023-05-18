import pandas as pd

from typing import Any, Dict, List, Tuple

class CSV:
    def __init__(self, csv_file_path: str) -> None:
        self.csv_file_path = csv_file_path
    
    def write_to_csv(self, list_of_dicts: List[Dict[str, str]]):
        df = pd.DataFrame(list_of_dicts)
        df.to_csv(self.csv_file_path, sep = ";", index=False)