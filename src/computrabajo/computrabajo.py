from typing import Any, Dict, List, Tuple

from src.http_request_handler import HTTPRequestHandler
from src.scrapper import Scraper
from utils.formats import format_string
from utils.validations import is_html


class CompuTrabajo:
    def __init__(self) -> None:
        self.request_handler = HTTPRequestHandler(
            base_url = "https://co.computrabajo.com",
        )
        self.summary = {}
        self.details = {}


    def get_job_details(self, job: str, location: str) -> Dict[str, str]:
        offers_links = self._get_offers_links(job, location)
    



    def _get_offers_links(self, job: str, location: str) -> List[str]:
        # Se estandariza el formato de entrada.
        formatted_job, formatted_location = self._format_input(job, location)
        headers = {
            "authority": "co.computrabajo.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "es-CO,es;q=0.9,es-419;q=0.8,en;q=0.7",
            "cookie": "extrfr=https://www.google.com/; g_state={\"i_p\":1682735181510,\"i_l\":1}; ut=74C22FD820D82E19FD35947839B843240290BA28240A807035B541B3E6DA1C250DE7B94C7F923005; cla=F70C52FB5BD35A3361373E686DCF3405&3C38E355663B6A9361373E686DCF3405&2D7238D4EAA5658C61373E686DCF3405&BF4547AC77FBA3B261373E686DCF3405&79C241E60018F41261373E686DCF3405",
            "referer": "https://co.computrabajo.com/trabajo-de-ingeniero-de-sistemas-en-santander?p=6",
            "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }

        jobs_links = []

        for i in range(1, 3000):
            endpoint = f"/trabajo-de-{formatted_job}-en-{formatted_location}?p={i}"
            # Se realiza la petición HTTP
            response = self.request_handler.get(endpoint, headers)

            if response is not None and not is_html(response):
                continue

            job_offers_scraper = Scraper(response)
            new_jobs_links = job_offers_scraper.scrape_offers_links()

            if not new_jobs_links:
                break

            jobs_links += new_jobs_links

        return jobs_links


    def _get_offer_details(self, edpoint: str):
        #TODO: 
        pass


    def _format_input(self, job: str, location: str) -> Tuple[str, str]:
        return format_string(job), format_string(location)