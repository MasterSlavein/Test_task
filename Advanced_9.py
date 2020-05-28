# Сделать скрипт, который будет делать GET запросы.
# Для каждого запроса должен быть вывод по примеру: "Resource 'google.com.ua', request took 0.23 sec,
# response status - 200." В реализации нет ограничений - можно использовать процессы, потоки, асинхронность.
# Любые вспомагательные механизмы типа Lock, Semaphore, пулы для тредов и потоков.
import sys
import asyncio
import aiohttp
import datetime
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


async def do_request(list_of_urls: list):
     async with aiohttp.ClientSession() as session:
          for url in list_of_urls:
               start_time = datetime.datetime.now().microsecond
               async with session.get(url, ssl=ssl.SSLContext()) as resp:

                    print(f'Resource {url}')
                    print(f'Response status={resp.status}')
                    end_time = datetime.datetime.now().microsecond
                    print(f'Response time {end_time - start_time}')





async def main():
    print(datetime.datetime.now().strftime("%A, %B %d, %I:%M %p"))
    print('---------------------------')
    loop = asyncio.get_running_loop()
    async with aiohttp.ClientSession(loop=loop) as client:
        await asyncio.gather(
               do_request(url_list)
            )
        print(f'Loop time={loop.time()}')

asyncio.run(main())
