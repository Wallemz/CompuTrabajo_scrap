from typing import Dict

from src.computrabajo_handler import CompuTrabajoHandler
from src.constants import jobs, locations

class BolsaDeEmpleo:
    """
    Clase base para todas las bolsas de empleo.
    """
    def __init__(self) -> None:
        self.jobs = jobs
        self.locations = locations

class CompuTrabajo(BolsaDeEmpleo):
    """
    Especialización para CompuTrabajo
    """
    def __init__(self) -> None:
        super().__init__()
        self.handler = CompuTrabajoHandler()

    def get_jobs_details(self) -> Dict[str, str]:
        pass

    def get_summary(self, jobs_details: Dict[str, str]) -> Dict[str, str]:
        pass