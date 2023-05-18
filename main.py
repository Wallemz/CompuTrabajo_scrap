import datetime

from src.computrabajo.handler import CompuTrabajoHandler
from src.csv_ import CSV
from utils.validations import ensure_dir


if __name__ == "__main__":
    print("Starting ....")

    print("Checking if Output folder exists")
    if not ensure_dir("output"):
        print("Could not create the output folder, check permissions.")
        exit()

    today = datetime.date.today().strftime("%Y_%m_%d")
    
    # This object has all the CompuTrabajo scrapping implementations
    computrabajo = CompuTrabajoHandler()

    # get_jobs_info is an iterator that returns info for a each job
    for job_summary, jobs_details in computrabajo.get_jobs_info():
        # Write the summary in a CSV
        summary_csv_path = f"output/{today}_summary.csv"
        if job_summary:
            CSV(summary_csv_path).write_to_csv(job_summary)
        
        # Write the detailes info in another CSV
        if jobs_details:
            detailed_csv_path = f"output/{today}_{jobs_details[0]['job_name_searched']}_detailed.csv"
            CSV(detailed_csv_path).write_to_csv(jobs_details)
            print(jobs_details)