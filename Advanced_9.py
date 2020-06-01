# Сделать скрипт, который будет делать GET запросы.
# Для каждого запроса должен быть вывод по примеру: "Resource 'google.com.ua', request took 0.23 sec,
# response status - 200." В реализации нет ограничений - можно использовать процессы, потоки, асинхронность.
# Любые вспомагательные механизмы типа Lock, Semaphore, пулы для тредов и потоков.
import sys
from asyncio import get_event_loop, ensure_future, wait
from aiohttp import ClientSession
from time import time
import ssl

url_list = ["http://docs.python-requests.org/",
            "https://httpbin.org/get",
            "https://httpbin.org/",
            "https://api.github.com/",
            "https://example.com/",
            "https://www.python.org/",
            "https://www.google.com.ua/",
            "https://regex101.com/",
            "https://docs.python.org/3/this-url-will-404.html",
            "https://www.nytimes.com/guides/",
            "https://www.mediamatters.org/",
            "https://1.1.1.1/",
            "https://www.politico.com/tipsheets/morning-money",
            "https://www.bloomberg.com/markets/economics",
            "https://www.ietf.org/rfc/rfc2616.txt"
            ]


async def get_url(session, url):
    start_time = time()
    async with session.request("GET", url, ssl=ssl.SSLContext()) as resp:
        print(f'Resource {url}')
        print(f'Response status={resp.status}')
        end_time = time()
        print(f'Response time {end_time - start_time}')


async def make_request(list_of_urls):
    start_time = time()
    async with ClientSession() as session:
        tasks = [ensure_future(get_url(session, url)) for url in list_of_urls]
        await wait(tasks)
    end_time = time()
    print(f'Loop time={end_time - start_time}')


loop = get_event_loop()
loop.run_until_complete(make_request(url_list))
