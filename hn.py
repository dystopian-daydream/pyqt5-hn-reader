import asyncio, json, requests

from concurrent.futures import ThreadPoolExecutor

base_url = "https://hacker-news.firebaseio.com"

params = dict(print="pretty")

def get(path):
    if path[0] != "/":
        path = f"/{path}"

    if path[:3] != "/v0":
        path = f"/v0{path}"

    if path[-5:] != ".json":
        path = f"{path}.json"

    return requests.get(base_url + path, params=dict(print="pretty")).json()

def get_articles():
    top_articles = dict()

    async_map(
        [dict(id=item, rank=i) for i, item in enumerate(get("topstories"), start=1)],
        lambda i: top_articles.update({ i['rank']: get(f"item/{i['id']}") }),
        MaxWorkers=100,
    )

    return { k: top_articles[k] for k in sorted(top_articles.keys()) }

def async_map(l, func, MaxWorkers=10):
    _executor = ThreadPoolExecutor(max_workers=MaxWorkers)

    async def pool_iterations():
        loop = async_io_loop()

        for response in await asyncio.gather(
            *[loop.run_in_executor(_executor, func, i) for i in l],
        ): pass

    async_io_loop = lambda: asyncio.get_event_loop()
    ensure_future = lambda: asyncio.ensure_future(pool_iterations())

    async_io_loop().run_until_complete(ensure_future())