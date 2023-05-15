from bs4 import BeautifulSoup, Tag
from typing import Dict, List, Optional, Tuple, Union

class Scraper:
    def __init__(self, html_doc: str):
        self.soup = BeautifulSoup(html_doc, 'html.parser')

    def scrape_text(self, filters: List[Tuple[str, Dict[str, str]]]) -> Optional[str]:
        result: Union[Tag, None] = self.soup

        # Apply each filter in turn
        for filter in filters:
            if result is not None:
                result = result.find(filter[0], filter[1])

        # If the final element was found
        if result is not None:
            return result.text

        # If the final element was not found, return None
        return None
    
    def scrape_offers_links(self) -> List[str]:
        articles = self.soup.find_all('article', class_=['box_offer', 'box_offer sel'])

        # Extract the 'href' attribute of the link within each article and store it in a list
        href_list = [article.find('a', class_='js-o-link')['href'] for article in articles if article.find('a', class_='js-o-link')]

        return href_list