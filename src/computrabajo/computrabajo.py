from typing import Any, Dict, List, Tuple

from src.http_request_handler import HTTPRequestHandler
from src.scrapper import Scraper
from utils.formats import format_string
from utils.validations import is_html


class CompuTrabajo:
    def __init__(self) -> None:
        self.request_handler = HTTPRequestHandler(
            base_url = "https://co.computrabajo.com",
            headers = {
                "authority": "co.computrabajo.com",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-language": "es-CO,es;q=0.9,es-419;q=0.8,en;q=0.7",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
            }
        )
        self.summary = {}
        self.details = {}

    def get_job_details(self, job: str, location: str) -> Dict[str, str]:
        offers_links = self._get_offers_links(job, location)
        for offer_link in offers_links:
            offer_details_html = self._get_offer_details_html(offer_link)

            offer_details_scraper = Scraper(offer_details_html)
            job_name = offer_details_scraper.scrape_job_name()
            company = offer_details_scraper.scrape_company()
            salary = offer_details_scraper.scrape_salary()
            requirements = offer_details_scraper.scrape_requirements()
            print("*" * 50)
            print(f"Job Name: {job_name}")
            print(f"Company Name: {company}")
            print(f"Salary: {salary}")
            print(f"Requirements: {salary}")
            for req in requirements:
                print(f"-- {req}")
            print("*" * 50)


    def _get_offers_links(self, job: str, location: str) -> List[str]:
        # Se estandariza el formato de entrada.
        formatted_job, formatted_location = self._format_input(job, location)

        jobs_links = []

        for i in range(1, 3000):
            endpoint = f"/trabajo-de-{formatted_job}-en-{formatted_location}?p={i}"
            # Se realiza la petición HTTP
            response = self.request_handler.get(endpoint)

            if response is None or not is_html(response):
                continue

            job_offers_scraper = Scraper(response)
            new_jobs_links = job_offers_scraper.scrape_offers_links()

            if not new_jobs_links:
                break

            jobs_links += new_jobs_links

        return jobs_links


    def _get_offer_details_html(self, endpoint: str):
        response = self.request_handler.get(endpoint)
        if response is None or not is_html(response):
            return None
        return response


    def _format_input(self, job: str, location: str) -> Tuple[str, str]:
        return format_string(job), format_string(location)