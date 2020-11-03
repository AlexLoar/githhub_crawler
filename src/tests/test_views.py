from unittest import mock

from fastapi.testclient import TestClient
import requests
from requests.exceptions import ProxyError

from exceptions import CrawlerException
from requester import Requester
from views import app

client = TestClient(app)


def test_crawler_when_bad_argument_in_keywords_returns_error():
    body_data = {
        "keywords": "WRONG",
        "proxies": [
            "194.126.37.94:8080",
            "13.78.125.167:8080"
        ],
        "type": "Repositories"
    }
    response = client.post('/crawler', json=body_data)

    expected_response = {
        'detail':
            [
                {
                    'loc': ['body', 'keywords'],
                    'msg': 'value is not a valid list',
                    'type': 'type_error.list'}
            ]
    }
    assert response.json() == expected_response
    assert response.status_code == 422


def test_crawler_when_bad_argument_in_proxies_returns_error():
    body_data = {
        "keywords": [
            "openstack",
            "nova",
            "css"
        ],
        "proxies": "194.126.37.94:8080",
        "type": "Repositories"
    }
    response = client.post('/crawler', json=body_data)

    expected_response = {
        'detail':
            [
                {
                    'loc': ['body', 'proxies'],
                    'msg': 'value is not a valid list',
                    'type': 'type_error.list'}
            ]
    }
    assert response.json() == expected_response
    assert response.status_code == 422


def test_crawler_when_bad_argument_in_type_returns_error():
    body_data = {
        "keywords": [
            "openstack",
            "nova",
            "css"
        ],
        "proxies": [
            "194.126.37.94:8080",
            "13.78.125.167:8080"
        ],
        "type": "Topics"
    }
    response = client.post('/crawler', json=body_data)

    expected_response = {
        "detail": [
            {
                "loc": [
                    "body",
                    "type"
                ],
                "msg": "value is not a valid enumeration member; permitted: 'Repositories', 'Wikis', 'Issues'",
                "type": "type_error.enum",
                "ctx": {
                    "enum_values": [
                        "Repositories",
                        "Wikis",
                        "Issues"
                    ]
                }
            }
        ]
    }
    assert response.json() == expected_response
    assert response.status_code == 422


@mock.patch.object(Requester, '_request')
def test_crawler_when_valid_body_searching_in_repositories_returns_valid_response(mock_requests):
    with open('tests/fixtures/repositories_success_response.txt', 'r') as file:
        expected_result = file.read()
    mock_requests.return_value = expected_result
    expected_status_code = 200

    body_data = {
        "keywords": [
            "openstack",
            "nova",
            "css"
        ],
        "proxies": [
            "194.126.37.94:8080"
        ],
        "type": "Repositories"
    }
    response = client.post('/crawler', json=body_data)

    expected_response = [
        {
            "url": "https://github.com/atuldjadhav/DropBox-Cloud-Storage"
        },
        {
            "url": "https://github.com/michealbalogun/Horizon-dashboard"
        }
    ]
    assert response.json() == expected_response
    assert response.status_code == expected_status_code


@mock.patch.object(Requester, '_request')
def test_crawler_when_valid_body_searching_in_wikis_returns_valid_response(mock_requests):
    with open('tests/fixtures/wikis_success_response.txt', 'r') as file:
        expected_result = file.read()
    mock_requests.return_value = expected_result
    expected_status_code = 200

    body_data = {
        "keywords": [
            "openstack",
            "nova",
            "css"
        ],
        "proxies": [
            "194.126.37.94:8080"
        ],
        "type": "Wikis"
    }
    response = client.post('/crawler', json=body_data)

    expected_response = [
        {
            "url": "https://github.com//vault-team/vault-website/wiki/Quick-installation-guide"
        },
        {
            "url": "https://github.com//marcosaletta/Juno-CentOS7-Guide/wiki/2.-Controller-and-Network-Node-Installation"
        },
        {
            "url": "https://github.com//escrevebastante/tongue/wiki/Home"
        },
        {
            "url": "https://github.com//rhafer/crowbar/wiki/Release-notes"
        },
        {
            "url": "https://github.com//MirantisDellCrowbar/crowbar/wiki/Release-notes"
        },
        {
            "url": "https://github.com//dellcloudedge/crowbar/wiki/Release-notes"
        },
        {
            "url": "https://github.com//eryeru12/crowbar/wiki/Release-notes"
        },
        {
            "url": "https://github.com//vinayakponangi/crowbar/wiki/Release-notes"
        },
        {
            "url": "https://github.com//jamestyj/crowbar/wiki/Release-notes"
        },
        {
            "url": "https://github.com//opencit/opencit/wiki/Open-CIT-3.2-Product-Guide"
        }
    ]
    assert response.json() == expected_response
    assert response.status_code == expected_status_code


@mock.patch.object(Requester, '_request')
def test_crawler_when_valid_body_searching_in_issues_returns_valid_response(mock_requests):
    with open('tests/fixtures/issues_success_response.txt', 'r') as file:
        expected_result = file.read()
    mock_requests.return_value = expected_result
    expected_status_code = 200

    body_data = {
        "keywords": [
            "openstack",
            "nova",
            "css"
        ],
        "proxies": [
            "194.126.37.94:8080"
        ],
        "type": "Issues"
    }
    response = client.post('/crawler', json=body_data)

    expected_response = [
        {
            "url": "https://github.com/altai/nova-billing/issues/1"
        },
        {
            "url": "https://github.com/sfPPP/openstack-note/issues/8"
        },
        {
            "url": "https://github.com/novnc/websockify/issues/180"
        },
        {
            "url": "https://github.com/rclone/rclone/issues/2713"
        },
        {
            "url": "https://github.com/Rajpratik71/openstack-org/pull/1"
        },
        {
            "url": "https://github.com/dokku/dokku/issues/4171"
        },
        {
            "url": "https://github.com/hellowj/blog/issues/37"
        },
        {
            "url": "https://github.com/suxgkn/myfiles/issues/4"
        },
        {
            "url": "https://github.com/urllib3/urllib3/issues/497"
        },
        {
            "url": "https://github.com/moby/moby/issues/19758"
        }
    ]
    assert response.json() == expected_response
    assert response.status_code == expected_status_code


@mock.patch.object(requests, 'request', side_effect=ProxyError())
def test_crawler_when_cannot_set_connection_through_proxy_returns_error(mock_requests):
    body_data = {
        "keywords": [
            "openstack",
            "nova",
            "css"
        ],
        "proxies": [
            "194.126.37.94:8080"
        ],
        "type": "Repositories"
    }
    response = client.post('/crawler', json=body_data)

    assert response.json() == {"error": "Cannot connect to proxy"}
    assert response.status_code == 424


@mock.patch.object(requests, 'request', side_effect=CrawlerException('Error'))
def test_crawler_when_unexpected_error_in_request_returns_error(mock_request):
    body_data = {
        "keywords": [
            "openstack",
            "nova",
            "css"
        ],
        "proxies": [
            "194.126.37.94:8080"
        ],
        "type": "Repositories"
    }
    response = client.post('/crawler', json=body_data)

    assert response.json() == {'error': "There was a problem in the request: CrawlerException('Error')"}
    assert response.status_code == 424
