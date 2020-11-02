from enum import Enum

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from src.crawler import GitHubCrawler
from src.exceptions import CrawlerException


class TypeEnum(str, Enum):
    repositories = 'Repositories'
    wikis = 'Wikis'
    issues = 'Issues'


class Body(BaseModel):
    keywords: list
    type: TypeEnum
    proxies: list


app = FastAPI()


@app.post('/crawler')
async def github_crawler(body: Body):
    crawler = GitHubCrawler()
    try:
        results = crawler.search(keywords=body.keywords,
                                 search_type=body.type,
                                 proxies=body.proxies)
        response = [{'url': url} for url in results]
    except CrawlerException as e:
        return JSONResponse(content={'error': str(e)}, status_code=424)
    return response
