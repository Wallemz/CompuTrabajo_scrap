from bs4 import BeautifulSoup, Tag
from typing import Dict, List, Optional, Tuple, Union

class Scraper:
    def __init__(self, html_doc: str):
        self.soup = BeautifulSoup(html_doc, 'html.parser')

    def scrape_offers_links(self) -> List[str]:
        articles = self.soup.find_all('article', class_=['box_offer', 'box_offer sel'])
        # Extract the 'href' attribute of the link within each article and store it in a list
        href_list = [article.find('a', class_='js-o-link')['href'] for article in articles if article.find('a', class_='js-o-link')]
        return href_list

    def scrape_job_name(self):
        job_name = self.soup.find('p', class_='fwB fs18')
        if not job_name:
            return ""
        return job_name.text
    
    def scrape_company(self):
        company = self.soup.find('a', {'class': 'dIB fs16 js-o-link'})
        if not company:
            return ""
        return company.text
    
    def scrape_salary(self):
        # Encontrar el primer <div> con class="mt15 mb15"
        div = self.soup.find('div', {'class': 'mt15 mb15'})
        if not div:
            return ""
        # Encontrar el primer <span> dentro del <div>
        salary = div.find('span', {'class': 'tag base mb10'})
        if not salary:
            return ""
        return salary.text
    
    def scrape_requirements(self):
        # Encontrar el primer <ul> con class="disc mbB"
        ul = self.soup.find('ul', {'class': 'disc mbB'})

        if not ul:
            return []
        # Encontrar todos los <li> dentro del <ul>
        lis = ul.find_all('li', {'class': 'mb10'})

        if not lis:
            return []
        
        # Crear una lista con el contenido de cada <li>
        return [li.text for li in lis]