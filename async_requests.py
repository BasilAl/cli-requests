import sys
import time
import asyncio
from aiohttp import ClientSession
from cli_arguments import get_int_arg

URL = "https://google.gr"


async def async_get_n(n):
    """
    Performs a(n) (asynchronous) get request <input> amount of times and returns the total times it fetched the site
    and the amount of time it took to do so. Example use: python3? sync_requests.py 12
    """



    async def aio_get_request(session, url):
        await session.get(url)

    start = time.perf_counter()
    async with ClientSession() as ses:
        await asyncio.gather(*[aio_get_request(ses, URL) for _ in range(n)])
    dt = time.perf_counter() - start

    print("get {} sites in {:.2f} seconds".format(n, dt))
    return 0


def main():

    n = get_int_arg()
    if n <= 0:
        print("Function takes exactly 1 argument which should be a positive integer. Example use: python3? "
              "sync_requests.py 12")
        return

    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    else:
        asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
    asyncio.run(async_get_n(n))


if __name__ == "__main__":
    main()
