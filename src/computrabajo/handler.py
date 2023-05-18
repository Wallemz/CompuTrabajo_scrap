from typing import Any, Dict, Iterator, List

from src.computrabajo.computrabajo import CompuTrabajo
from src.bolsas_de_empleo import BolsaDeEmpleo


class CompuTrabajoHandler(BolsaDeEmpleo):
    def __init__(self) -> None:
        super().__init__()
        self.handler = CompuTrabajo()

    def get_jobs_info(self):
        jobs_summary = []
        for job in self.jobs:
            job_details = []
            job_summary = {"job_name" : job}
            job_summary["salary_mean"] = 0
            salary_sum = 0
            salary_count = 0
            for location in self.locations:
                print(f"Buscando trabajos para {job} en {location}")
                # Obtiene La información del trabajo en una lista de diccionarios.
                job_details += self.handler.get_jobs_details(job, location)
                job_summary[location] = len(job_details)
                salary, count = self._get_salary_mean_vars(job_details)
                salary_sum += salary
                salary_count += count
            if salary_sum < 1 or salary_count <1:
                job_summary["salary_mean"] = ""
            else:
                job_summary["salary_mean"] = salary_sum / salary_count
            jobs_summary.append(job_summary)
            yield jobs_summary, job_details
        
    def _get_salary_mean_vars(self, job_details: List[Dict[str, Any]]):
        salary_sum = 0
        count = 0
        for job_detail in job_details:
            if not job_detail['salary'] or job_detail['salary'] == "":
                continue
            try:
                salary_sum += job_detail['salary']
                count += 1
            except Exception as e:
                continue

        return salary_sum, count