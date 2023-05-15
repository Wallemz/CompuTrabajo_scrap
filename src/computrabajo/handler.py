from typing import Any, Optional

from src.computrabajo.computrabajo import CompuTrabajo
from src.bolsas_de_empleo import BolsaDeEmpleo


class CompuTrabajoHandler(BolsaDeEmpleo):
    def __init__(self) -> None:
        super().__init__()
        self.handler = CompuTrabajo()
        self.jobs_summary = None
        self.jobs_details = None

    def get_jobs_info(self) -> Optional[Any]:
        for job in self.jobs:
            for location in self.locations:
                # Obtiene los HTML que contienen la lista de ofertas para un solo trabajo.
                self.handler.get_job_details(job, location)