import datetime

from src.computrabajo.handler import CompuTrabajoHandler
from src.csv_ import CSV


if __name__ == "__main__":
    print("Iniciando ....")

    # Get today's date
    today = datetime.date.today().strftime("%Y_%m_%d")

    computrabajo = CompuTrabajoHandler()
    for job_summary, jobs_details in computrabajo.get_jobs_info():
        summary_csv_path = f"output/{today}_summary.csv"
        CSV(summary_csv_path).write_to_csv(job_summary)
        if jobs_details:
            detailed_csv_path = f"output/{today}_{jobs_details[0]['job_name_searched']}_detailed.csv"
            CSV(detailed_csv_path).write_to_csv(jobs_details)
            print(jobs_details)