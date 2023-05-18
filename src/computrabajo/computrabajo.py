from typing import Any, Dict, List, Optional, Tuple

from src.http_request_handler import HTTPRequestHandler
from src.computrabajo.scrapper import Scraper
from utils.formats import format_string, salary_to_number
from utils.validations import is_html


class CompuTrabajo:
    """Class specialization of "BolsaDeEmpleo" thta implements all the methods
    to scrap in CompuTrabajo
    """
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

    def get_jobs_details(self, job: str, location: str) -> List[Dict[str, Any]]:
        """Iterate over all the offer links and gets the job details

        Args:
            job (str): Job Name
            location (str): Location

        Returns:
            List[Dict[str, Any]]: List of dictionaries with the job details for each job offer.
        """
        jobs_details = []
        offers_links = self._get_offers_links(job, location)
        for offer_link in offers_links:
            print(offer_link)
            offer_details_html = self._get_offer_details_html(offer_link)
            if offer_details_html is None:
                continue
            offer_details_scraper = Scraper(offer_details_html)
            job_details = {}
            job_details['job_name_searched'] = job
            job_details['location_searched'] = location
            job_details['job_name'] = offer_details_scraper.scrape_job_name()
            job_details['company'] = offer_details_scraper.scrape_company()
            job_details['salary'] = salary_to_number(offer_details_scraper.scrape_salary())
            job_details['job_location'] = offer_details_scraper.scrape_location()
            job_details['requirements'] = offer_details_scraper.scrape_requirements()
            jobs_details.append(job_details)
        return jobs_details


    def _get_offers_links(self, job: str, location: str) -> List[str]:
        """Itearte over the CompuTrabajo page to find all the endpoints.

        Args:
            job (str): Job Name
            location (str): Location

        Returns:
            List[str]: List with the jobb offers endpoints
        """
        formatted_job, formatted_location = self._format_input(job, location)
        jobs_links = []

        for i in range(1, 3000):
            endpoint = f"/trabajo-de-{formatted_job}-en-{formatted_location}?p={i}"
            response = self.request_handler.get(endpoint)
            if response is None or not is_html(response):
                continue

            job_offers_scraper = Scraper(response)
            new_jobs_links = job_offers_scraper.scrape_offers_links()
            if not new_jobs_links:
                break
            jobs_links += new_jobs_links
        return jobs_links


    def _get_offer_details_html(self, endpoint: str) -> Optional[(Dict[str, Any] | str | None)]:
        """Gets the HTML that contains the offer details

        Returns:
            _type_: HTML
        """
        response = self.request_handler.get(endpoint)
        if response is None or not is_html(response):
            return None
        return response


    def _format_input(self, job: str, location: str) -> Tuple[str, str]:
        """Converts the input to the required format.

        Args:
            job (str): Job Name
            location (str): Location

        Returns:
            Tuple[str, str]: Formatted variables
        """
        return format_string(job), format_string(location)