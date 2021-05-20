import sys
import time
import asyncio
from aiohttp import ClientSession
from cli_argument_restrictions import single_integer

URL = "https://google.gr"


async def async_get_many(arg):
    """
    Performs a(n) (asynchronous) get request <input> amount of times and returns the total times it fetched the site
    and the amount of time it took to do so. Example use: python3? sync_requests.py 12
    """

    async def aio_get_request(session, url):
        await session.get(url)

    if single_integer(arg):
        return -1

    n = int(arg[1])
    start = time.perf_counter()
    async with ClientSession() as ses:
        await asyncio.gather(*[aio_get_request(ses, URL) for _ in range(n)])
    dt = time.perf_counter() - start

    print("get {} sites in {:.2f} seconds".format(n, dt))
    return 0


if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    else:
        asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
    asyncio.run(async_get_many(sys.argv))
