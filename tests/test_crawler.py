from unittest import mock

from src.crawler import GitHubCrawler
from src.requester import Requester


@mock.patch('src.crawler.logging')
@mock.patch.object(Requester, '_request')
def test_search_when_malformed_github_response_log_error(mock_requests, mock_logging):
    with open('tests/fixtures/repositories_malformed_response.txt', 'r') as file:
        expected_response = file.read()
    mock_requests.return_value = expected_response

    GitHubCrawler().search(keywords=["openstack", "nova", "css"],
                           search_type='Repositories',
                           proxies=['78.110.174.119:8080'])

    assert mock_logging.warning.called


@mock.patch.object(Requester, '_request')
def test_search_when_valid_github_response_returns_urls(mock_requests):
    with open('tests/fixtures/repositories_success_response.txt', 'r') as file:
        expected_response = file.read()
    mock_requests.return_value = expected_response

    result = GitHubCrawler().search(keywords=["openstack", "nova", "css"],
                                    search_type='Repositories',
                                    proxies=['78.110.174.119:8080'])

    expected_result = ['https://github.com/atuldjadhav/DropBox-Cloud-Storage',
                       'https://github.com/michealbalogun/Horizon-dashboard']
    assert result == expected_result
