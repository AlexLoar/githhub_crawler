import json
import random
import logging

from bs4 import BeautifulSoup

from requester import Requester

logging.basicConfig(filename='../crawler.log',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console)


class GitHubCrawler:
    base_url = 'https://github.com/search?q={keywords}&type={search_type}'

    def __init__(self):
        self.requester = Requester()

    def search(self, keywords: list, search_type: str, proxies: list) -> list:
        url = self._build_endpoint(keywords, search_type)
        proxy = self._set_proxies(proxies)

        logging.info(f'Crawling URL: "{url}"')
        response = self.requester.get(url, proxy)
        return self._process_response(response)

    def _build_endpoint(self, keywords: list, search_type: str) -> str:
        formatted_keywords = '+'.join(keywords)
        return self.base_url.format(keywords=formatted_keywords, search_type=search_type.lower())

    @staticmethod
    def _set_proxies(proxies: list) -> dict:
        return {'http': random.choice(proxies)}

    @staticmethod
    def _process_response(response: str) -> list:
        result = []
        parsed_response = BeautifulSoup(response, "html.parser")
        entities = parsed_response.find_all('div', {'class': 'f4 text-normal'})
        for entity in entities:
            try:
                entity_url = json.loads(entity.find('a').attrs['data-hydro-click'])['payload']['result']['url']
            except Exception as e:
                logging.warning(f'Error processing entity: "{repr(e)}"')
                continue
            result.append(entity_url)
        return result
