import requests
import sys
import time
from cli_argument_restrictions import single_integer

URL = "https://google.gr"


def sync_get_many(arg):
    """
    Performs a (synchronous) get request <input> amount of times and returns the total times it fetched the site and
    the amount of time it took to do so. Example use: python3? sync_requests.py 12
    """

    if single_integer(arg):
        return -1

    n = int(arg[1])
    start = time.perf_counter()

    for i in range(n):
        requests.get(URL)  # response not needed

    dt = time.perf_counter() - start
    print("get {} sites in {:.4f} seconds".format(n, dt))
    return 0


if __name__ == "__main__":
    sync_get_many(sys.argv)
