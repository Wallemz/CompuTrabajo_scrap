from bs4 import BeautifulSoup
from typing import List

class Scraper:
    """Class that implements all the specific scraping methods for CompuTrabajo.
    """
    def __init__(self, html_doc: str):
        self.soup = BeautifulSoup(html_doc, 'html.parser')

    def scrape_offers_links(self) -> List[str]:
        """Looks in the HTML for all the tags with a link to a job offer.

        Returns:
            List[str]: List of endpoints to a job offer.
        """
        articles = self.soup.find_all('article', class_=['box_offer', 'box_offer sel'])
        # Extract the 'href' attribute of the link within each article and store it in a list
        href_list = [article.find('a', class_='js-o-link')['href'] for article in articles if article.find('a', class_='js-o-link')]
        return href_list

    def scrape_job_name(self) -> str:
        """Extracts the job name in the HTML

        Returns:
            str: Job name or an empty string
        """
        job_name = self.soup.find('p', class_='fwB fs18')
        if not job_name:
            return ""
        return job_name.text
    
    def scrape_company(self) -> str:
        """Extracts the company name if exists in the offer

        Returns:
            str: Company name or an empty string
        """
        company = self.soup.find('a', {'class': 'dIB fs16 js-o-link'})
        if not company:
            return ""
        return company.text
    
    def scrape_salary(self) -> str:
        """Extracts the salary if exists in the offer

        Returns:
            str: Salary or an empty string
        """
        # Looks for the first <div> with class="mt15 mb15"
        div = self.soup.find('div', {'class': 'mt15 mb15'})
        if not div:
            return ""
        # Looks for the first <span> inside if <div>
        salary = div.find('span', {'class': 'tag base mb10'})
        if not salary:
            return ""
        return salary.text
    
    def scrape_requirements(self) -> str:
        """Extarcts all the requerimentts for a job offer

        Returns:
            List[str]: String List of requirements
        """
        # Looks for the first <ul> with class="disc mbB"
        ul = self.soup.find('ul', {'class': 'disc mbB'})
        if not ul:
            return ""
        # Looks for all the <li> inside of <ul>
        lis = ul.find_all('li', {'class': 'mb10'})
        if not lis:
            return ""
        # Creates a list with the content of each <li>
        final_list =  [li.text for li in lis]
        return '\n'.join(final_list)
    
    def scrape_location(self) -> str:
        """Extract the location if exists in the offer

        Returns:
            str: Location or an empty string
        """
        box_resume = self.soup.find('div', {'class': 'fr pt10 box_resume hide_m'})
        box_border_div = box_resume.find('div', {'class': 'box_border'})
        if not box_border_div:
            return ""
        fs16_content = box_border_div.find('p', {'class': 'fs16'})
        if not fs16_content:
            return ""
        return fs16_content.text