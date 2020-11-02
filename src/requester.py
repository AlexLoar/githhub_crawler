import requests
from requests.exceptions import ProxyError

from src.exceptions import CrawlerException


class Requester:

    def _request(self, method: str, url: str, proxies: dict) -> str:
        if method == 'GET':
            try:
                response = requests.request(method=method, url=url, proxies=proxies)
            except ProxyError:
                raise CrawlerException('Cannot connect to proxy')
            except Exception as e:
                raise CrawlerException(f'There was a problem in the request: {repr(e)}')
        else:
            raise NotImplementedError(f'Method "{method}" not implemented')
        return response.text

    def get(self, url: str, proxies: dict) -> str:
        return self._request('GET', url, proxies)
