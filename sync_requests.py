import requests
import time
from cli_arguments import get_int_arg

URL = "https://google.gr"


def sync_get_n(n):
    """
    Performs a (synchronous) get request <input> amount of times and returns the total times it fetched the site and
    the amount of time it took to do so. Example use: python3? sync_requests.py 12
    """

    start = time.perf_counter()
    for i in range(n):
        requests.get(URL)  # response not needed
    dt = time.perf_counter() - start
    print("get {} sites in {:.2f} seconds".format(n, dt))
    return 0


def main():
    n = get_int_arg()
    if n <= 0:
        print("Function takes exactly 1 argument which should be a positive integer. Example use: python3? "
              "sync_requests.py 12")
        return
    sync_get_n(n)


if __name__ == "__main__":
    main()
