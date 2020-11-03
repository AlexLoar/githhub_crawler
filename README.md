# GitHub Crawler

This crawler allows you to search in [GitHub](https://github.com "GitHub") repositories, wikis or issues according to the keywords you pass to it and it returns a list of URLs of the found items.

It consists of a single endpoint created with [FastAPI](https://fastapi.tiangolo.com/ "FastAPI") which handle input and carry out the crawling process.

### Usage
To use this crawler, just make use of the Makefile to run the main commands:

Run server
`make up`

Stop server
`make down`

Run the tests
`make test`

### Endpoint documentation

To see the online documentation you can go [here](http://localhost:8000/docs "here") once the proyect is launched.

**POST** `localhost:8000/crawler`
Body example

```json
{
  "keywords": [
    "openstack",
    "nova",
    "css"
  ],
  "proxies": [
    "78.110.174.119:8080"
  ],
  "type": "Wikis"
}
```

keyword: List of keywords to use in the search.

proxies: List of proxies used to make the request to GitHub. One will be picked from the list randomly.

type: Specifies the type of entity where the search will be carried out. May take the following values: Repositories, Wikis or Issues.
